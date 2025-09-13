from __future__ import annotations

from typing import List, Optional
from sqlalchemy import String, Text, ForeignKey, UniqueConstraint, Date, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.documento_venta_linea import DocumentoVentaLinea
from models.pago import Pago
from .base import Base, TimestampMixin, uuid_pk


class DocumentoVenta(Base):
    __tablename__ = "documento_venta"
    __table_args__ = (UniqueConstraint("id_empresa_documento_venta", "tipo_documento_documento_venta", "numero_documento_documento_venta", name="uq_documento_venta_emp_tipo_num"),)

    id_documento_venta: Mapped[int] = mapped_column("id_documento_venta", primary_key=True, autoincrement=True)
    id_empresa_documento_venta: Mapped[int] = mapped_column("id_empresa_documento_venta", ForeignKey("empresa.id_empresa"), nullable=False)
    id_tercero_documento_venta: Mapped[Optional[int]] = mapped_column("id_tercero_documento_venta", ForeignKey("tercero.id_tercero"))
    id_serie_documento_venta: Mapped[Optional[int]] = mapped_column("id_serie_documento_venta", ForeignKey("serie_numeracion.id_serie_numeracion"))
    tipo_documento_documento_venta: Mapped[Optional[str]] = mapped_column("tipo_documento_documento_venta", String(50))
    numero_documento_documento_venta: Mapped[Optional[str]] = mapped_column("numero_documento_documento_venta", String(100))
    fecha_emision_documento_venta: Mapped[Optional[Date]] = mapped_column("fecha_emision_documento_venta", Date)
    fecha_vencimiento_documento_venta: Mapped[Optional[Date]] = mapped_column("fecha_vencimiento_documento_venta", Date)
    moneda_documento_venta: Mapped[Optional[str]] = mapped_column("moneda_documento_venta", String(10))
    estado_documento_venta: Mapped[Optional[str]] = mapped_column("estado_documento_venta", String(50))
    subtotal_documento_venta: Mapped[float] = mapped_column("subtotal_documento_venta", Numeric(14, 2), default=0.00)
    impuestos_documento_venta: Mapped[float] = mapped_column("impuestos_documento_venta", Numeric(14, 2), default=0.00)
    total_documento_venta: Mapped[float] = mapped_column("total_documento_venta", Numeric(14, 2), default=0.00)
    saldo_documento_venta: Mapped[float] = mapped_column("saldo_documento_venta", Numeric(14, 2), default=0.00)
    notas_documento_venta: Mapped[Optional[str]] = mapped_column("notas_documento_venta", Text)
    created_by_id_usuario_documento_venta: Mapped[Optional[int]] = mapped_column("created_by_id_usuario_documento_venta", ForeignKey("usuario.id_usuario"))
    created_at_documento_venta: Mapped[Optional[str]] = mapped_column("created_at_documento_venta")
    updated_at_documento_venta: Mapped[Optional[str]] = mapped_column("updated_at_documento_venta")
    deleted_at_documento_venta: Mapped[Optional[str]] = mapped_column("deleted_at_documento_venta")

    empresa = relationship("Empresa", back_populates="documentos_venta")
    cliente = relationship("Tercero", back_populates="documentos_cliente")
    serie = relationship("SerieNumeracion", back_populates="documentos")
    lineas: Mapped[List["DocumentoVentaLinea"]] = relationship(back_populates="documento", cascade="all, delete-orphan")
    pagos: Mapped[List["Pago"]] = relationship(back_populates="documento", cascade="all, delete-orphan")
