from __future__ import annotations

from typing import List, Optional
from sqlalchemy import String, Boolean, ForeignKey, UniqueConstraint, Numeric, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.documento_venta_linea import DocumentoVentaLinea
from .base import Base, TimestampMixin, uuid_pk


class Producto(Base):
    __tablename__ = "producto"
    __table_args__ = (UniqueConstraint("id_empresa_producto", "codigo_producto", name="uq_producto_empresa_codigo"),)

    id_producto: Mapped[int] = mapped_column("id_producto", primary_key=True, autoincrement=True)
    id_empresa_producto: Mapped[int] = mapped_column("id_empresa_producto", Integer, ForeignKey("empresa.id_empresa"), nullable=False)
    codigo_producto: Mapped[str] = mapped_column("codigo_producto", String(60), nullable=False)
    nombre_producto: Mapped[str] = mapped_column("nombre_producto", String(200), nullable=False)
    precio_unitario_producto: Mapped[float] = mapped_column("precio_unitario_producto", Numeric(18, 2), nullable=False)
    id_impuesto_producto: Mapped[Optional[int]] = mapped_column("id_impuesto_producto", Integer, ForeignKey("impuesto.id_impuesto"))
    activo_producto: Mapped[bool] = mapped_column("activo_producto", Boolean, default=True, nullable=False)
    created_at_producto: Mapped[Optional[str]] = mapped_column("created_at_producto")
    updated_at_producto: Mapped[Optional[str]] = mapped_column("updated_at_producto")

    empresa = relationship("Empresa", back_populates="productos")
    impuesto = relationship("Impuesto", back_populates="productos")
    lineas_venta: Mapped[List["DocumentoVentaLinea"]] = relationship(back_populates="producto")
