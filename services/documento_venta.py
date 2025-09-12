from __future__ import annotations

from decimal import Decimal
from typing import Iterable
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from models import (
    DocumentoVenta, DocumentoVentaLinea, Pago, Producto, Impuesto, Tercero, Empresa, SerieNumeracion
)
from schemas import (
    DocumentoVentaCreate, DocumentoVentaUpdate,
    DocumentoVentaLineaCreate, DocumentoVentaLineaUpdate,
    PagoCreate
)
from .base import CRUDService
from .exceptions import BadRequestError, NotFoundError, ConflictError
from .serie_numeracion import SerieNumeracionService

class DocumentoVentaService(CRUDService[DocumentoVenta, DocumentoVentaCreate, DocumentoVentaUpdate]):
    model = DocumentoVenta

    def _assert_same_empresa(self, empresa_id, cliente_id, serie_id):
        cli = self.session.get(Tercero, cliente_id)
        if not cli or cli.empresa_id != empresa_id:
            raise BadRequestError("El cliente no pertenece a la empresa")
        serie = self.session.get(SerieNumeracion, serie_id)
        if not serie or serie.empresa_id != empresa_id:
            raise BadRequestError("La serie no pertenece a la empresa")

    def create(self, obj_in: DocumentoVentaCreate) -> DocumentoVenta:
        self._assert_same_empresa(obj_in.empresa_id, obj_in.cliente_id, obj_in.serie_id)
        doc = self.model(**obj_in.model_dump(exclude_unset=True))
        self.session.add(doc)
        self.session.flush()
        return doc

    def add_line(self, documento_id, line_in: DocumentoVentaLineaCreate) -> DocumentoVentaLinea:
        doc = self.get(documento_id)
        if line_in.documento_id != doc.id:
            raise BadRequestError("documento_id de la línea no coincide con el documento")
        prod = self.session.get(Producto, line_in.producto_id)
        if not prod or prod.empresa_id != doc.empresa_id:
            raise BadRequestError("El producto no pertenece a la empresa del documento")

        payload = line_in.model_dump(exclude_unset=True)
        # Si no nos envían porcentaje_impuesto explícito, tomar del producto/impuesto
        if payload.get("impuesto_id") and payload.get("porcentaje_impuesto") is None:
            imp = self.session.get(Impuesto, payload["impuesto_id"])
            if not imp:
                raise BadRequestError("Impuesto no válido")
            payload["porcentaje_impuesto"] = Decimal(imp.porcentaje)

        linea = DocumentoVentaLinea(**payload)
        self.session.add(linea)
        self.session.flush()
        self.recalc_totals(doc)
        return linea

    def update_line(self, line_id, line_in: DocumentoVentaLineaUpdate) -> DocumentoVentaLinea:
        linea = self.session.get(DocumentoVentaLinea, line_id)
        if not linea:
            raise NotFoundError("DocumentoVentaLinea", str(line_id))
        data = line_in.model_dump(exclude_unset=True)
        for k, v in data.items():
            setattr(linea, k, v)
        self.session.flush()
        self.recalc_totals(linea.documento)
        return linea

    def delete_line(self, line_id) -> None:
        linea = self.session.get(DocumentoVentaLinea, line_id)
        if not linea:
            raise NotFoundError("DocumentoVentaLinea", str(line_id))
        doc = linea.documento
        self.session.delete(linea)
        self.session.flush()
        self.recalc_totals(doc)

    def recalc_totals(self, doc: DocumentoVenta) -> DocumentoVenta:
        # Calcular subtotal, impuestos y total desde líneas
        stmt = select(
            func.coalesce(func.sum(DocumentoVentaLinea.cantidad * DocumentoVentaLinea.precio_unitario), 0),
            func.coalesce(func.sum(
                (DocumentoVentaLinea.cantidad * DocumentoVentaLinea.precio_unitario) *
                (DocumentoVentaLinea.porcentaje_impuesto / 100.0)
            ), 0),
        ).where(DocumentoVentaLinea.documento_id == doc.id)
        subtotal, impuestos = self.session.execute(stmt).one()
        doc.subtotal = Decimal(subtotal).quantize(Decimal("0.01"))
        doc.impuestos = Decimal(impuestos).quantize(Decimal("0.01"))
        doc.total = (doc.subtotal + doc.impuestos).quantize(Decimal("0.01"))

        # Recalcular saldo = total - pagos
        stmt2 = select(func.coalesce(func.sum(Pago.monto), 0)).where(Pago.documento_id == doc.id)
        pagos = self.session.execute(stmt2).scalar_one()
        doc.saldo = (doc.total - Decimal(pagos)).quantize(Decimal("0.01"))

        # Actualizar estado simple
        if doc.saldo <= Decimal("0.00") and doc.total > Decimal("0.00"):
            doc.estado = "pagado"
        elif doc.total > Decimal("0.00"):
            doc.estado = "emitido"
        else:
            doc.estado = "borrador"

        self.session.flush()
        return doc

    def confirm_and_assign_number(self, documento_id) -> DocumentoVenta:
        doc = self.get(documento_id)
        if doc.estado not in ("borrador", "emitido"):
            raise ConflictError("El documento no está en estado confirmable")
        serie_svc = SerieNumeracionService(self.session)
        numero = serie_svc.assign_next_number(doc.serie_id)
        doc.numero = numero
        self.recalc_totals(doc)
        return doc

    def register_payment(self, pago_in: PagoCreate) -> Pago:
        doc = self.get(pago_in.documento_id)
        pago = Pago(**pago_in.model_dump(exclude_unset=True))
        self.session.add(pago)
        self.session.flush()
        self.recalc_totals(doc)
        return pago
