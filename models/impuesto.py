from __future__ import annotations

from typing import List
from sqlalchemy import String, Boolean, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.documento_venta_linea import DocumentoVentaLinea
from models.gasto import Gasto
from models.producto import Producto
from .base import Base, TimestampMixin, uuid_pk


class Impuesto(TimestampMixin, Base):
    __tablename__ = "impuesto"

    id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), primary_key=True, default=uuid_pk)
    empresa_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("empresa.id_empresa"), nullable=False)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    porcentaje: Mapped[float] = mapped_column(Numeric(9, 4), nullable=False)
    activo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    empresa = relationship("Empresa", back_populates="impuestos")
    productos: Mapped[List["Producto"]] = relationship(back_populates="impuesto")
    lineas_venta: Mapped[List["DocumentoVentaLinea"]] = relationship(back_populates="impuesto")
    gastos: Mapped[List["Gasto"]] = relationship(back_populates="impuesto")
