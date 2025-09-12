from __future__ import annotations

from typing import Optional
from sqlalchemy import String, Text, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from .base import Base, uuid_pk


class DocumentoVentaLinea(Base):
    __tablename__ = "documento_venta_linea"

    id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), primary_key=True, default=uuid_pk)
    documento_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("documento_venta.id"), nullable=False)
    producto_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("producto.id"), nullable=False)
    descripcion: Mapped[Optional[str]] = mapped_column(Text)
    cantidad: Mapped[float] = mapped_column(Numeric(18, 4), nullable=False)
    precio_unitario: Mapped[float] = mapped_column(Numeric(18, 2), nullable=False)
    impuesto_id: Mapped[Optional[uuid_pk]] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("impuesto.id"))
    porcentaje_impuesto: Mapped[Optional[float]] = mapped_column(Numeric(9, 4))
    total_linea: Mapped[float] = mapped_column(Numeric(18, 2), nullable=False)

    documento = relationship("DocumentoVenta", back_populates="lineas")
    producto = relationship("Producto", back_populates="lineas_venta")
    impuesto = relationship("Impuesto", back_populates="lineas_venta")
