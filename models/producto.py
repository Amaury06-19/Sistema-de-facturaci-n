from __future__ import annotations

from typing import List, Optional
from sqlalchemy import String, Boolean, ForeignKey, UniqueConstraint, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.documento_venta_linea import DocumentoVentaLinea
from .base import Base, TimestampMixin, uuid_pk


class Producto(TimestampMixin, Base):
    __tablename__ = "producto"
    __table_args__ = (UniqueConstraint("empresa_id", "codigo", name="uq_producto_empresa_codigo"),)

    id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), primary_key=True, default=uuid_pk)
    empresa_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("empresa.id_empresa"), nullable=False)
    codigo: Mapped[str] = mapped_column(String(60), nullable=False)
    nombre: Mapped[str] = mapped_column(String(200), nullable=False)
    precio_unitario: Mapped[float] = mapped_column(Numeric(18, 2), nullable=False)
    impuesto_id: Mapped[Optional[uuid_pk]] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("impuesto.id"))
    activo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    empresa = relationship("Empresa", back_populates="productos")
    impuesto = relationship("Impuesto", back_populates="productos")
    lineas_venta: Mapped[List["DocumentoVentaLinea"]] = relationship(back_populates="producto")
