from __future__ import annotations

from decimal import Decimal
from sqlalchemy.orm import Session
from models import Gasto, GastoAdjunto, Impuesto, Tercero, CategoriaGasto
from schemas import GastoCreate, GastoUpdate, GastoAdjuntoCreate
from .base import CRUDService
from .exceptions import BadRequestError

class GastoService(CRUDService[Gasto, GastoCreate, GastoUpdate]):
    model = Gasto

    def create(self, obj_in: GastoCreate) -> Gasto:
        # Validaciones de pertenencia
        proveedor = self.session.get(Tercero, obj_in.proveedor_id)
        if not proveedor or proveedor.empresa_id != obj_in.empresa_id:
            raise BadRequestError("El proveedor no pertenece a la empresa")
        categoria = self.session.get(CategoriaGasto, obj_in.categoria_id)
        if not categoria or categoria.empresa_id != obj_in.empresa_id:
            raise BadRequestError("La categoría no pertenece a la empresa")

        data = obj_in.model_dump(exclude_unset=True)
        if data.get("impuesto_id") and data.get("porcentaje_impuesto") is None:
            imp = self.session.get(Impuesto, data["impuesto_id"])
            if imp:
                data["porcentaje_impuesto"] = Decimal(imp.porcentaje)
        gasto = Gasto(**data)
        self.session.add(gasto)
        self.session.flush()
        return gasto

class GastoAdjuntoService:
    def __init__(self, session: Session):
        self.session = session

    def add(self, obj_in: GastoAdjuntoCreate) -> GastoAdjunto:
        adj = GastoAdjunto(**obj_in.model_dump(exclude_unset=True))
        self.session.add(adj)
        self.session.flush()
        return adj

    def delete(self, adjunto_id) -> None:
        adj = self.session.get(GastoAdjunto, adjunto_id)
        if not adj:
            from .exceptions import NotFoundError
            raise NotFoundError("GastoAdjunto", str(adjunto_id))
        self.session.delete(adj)
        self.session.flush()
