from __future__ import annotations

from typing import List
from sqlalchemy import String, Boolean, ForeignKey, Numeric, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.documento_venta_linea import DocumentoVentaLinea
from models.gasto import Gasto
from models.producto import Producto
from .base import Base, TimestampMixin, uuid_pk


class Impuesto(Base):
    __tablename__ = "impuesto"

    id_impuesto: Mapped[int] = mapped_column("id_impuesto", primary_key=True, autoincrement=True)
    id_empresa_impuesto: Mapped[int] = mapped_column("id_empresa_impuesto", Integer, ForeignKey("empresa.id_empresa"), nullable=False)
    nombre_impuesto: Mapped[str] = mapped_column("nombre_impuesto", String(100), nullable=False)
    porcentaje_impuesto: Mapped[float] = mapped_column("porcentaje_impuesto", Numeric(9, 4), nullable=False)
    activo_impuesto: Mapped[bool] = mapped_column("activo_impuesto", Boolean, default=True, nullable=False)
    created_at_impuesto: Mapped[str] = mapped_column("created_at_impuesto")
    updated_at_impuesto: Mapped[str] = mapped_column("updated_at_impuesto")

    empresa = relationship("Empresa", back_populates="impuestos")
    productos: Mapped[List["Producto"]] = relationship(back_populates="impuesto")
    lineas_venta: Mapped[List["DocumentoVentaLinea"]] = relationship(back_populates="impuesto")
    gastos: Mapped[List["Gasto"]] = relationship(back_populates="impuesto")
