from __future__ import annotations

from typing import Optional
from sqlalchemy import String, Text, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from .base import Base, uuid_pk


class DocumentoVentaLinea(Base):
    __tablename__ = "documento_venta_linea"

    id_documento_venta_linea: Mapped[int] = mapped_column("id_documento_venta_linea", primary_key=True, autoincrement=True)
    id_documento_venta: Mapped[int] = mapped_column("id_documento_venta", ForeignKey("documento_venta.id_documento_venta"), nullable=False)
    id_producto_documento_venta_linea: Mapped[int] = mapped_column("id_producto_documento_venta_linea", ForeignKey("producto.id_producto"), nullable=False)
    descripcion_documento_venta_linea: Mapped[Optional[str]] = mapped_column("descripcion_documento_venta_linea", Text)
    cantidad_documento_venta_linea: Mapped[float] = mapped_column("cantidad_documento_venta_linea", Numeric(18, 4), nullable=False)
    precio_unitario_documento_venta_linea: Mapped[float] = mapped_column("precio_unitario_documento_venta_linea", Numeric(18, 2), nullable=False)
    id_impuesto_documento_venta_linea: Mapped[Optional[int]] = mapped_column("id_impuesto_documento_venta_linea", ForeignKey("impuesto.id_impuesto"))
    porcentaje_impuesto_documento_venta_linea: Mapped[Optional[float]] = mapped_column("porcentaje_impuesto_documento_venta_linea", Numeric(9, 4))
    total_linea_documento_venta_linea: Mapped[float] = mapped_column("total_linea_documento_venta_linea", Numeric(18, 2), nullable=False)

    documento = relationship("DocumentoVenta", back_populates="lineas")
    producto = relationship("Producto", back_populates="lineas_venta")
    impuesto = relationship("Impuesto", back_populates="lineas_venta")
