from __future__ import annotations

from typing import Optional, List
from sqlalchemy import String, Text, ForeignKey, Numeric, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.gasto_adjunto import GastoAdjunto
from .base import Base, TimestampMixin, uuid_pk


class Gasto(TimestampMixin, Base):
    __tablename__ = "gasto"

    id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), primary_key=True, default=uuid_pk)
    empresa_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("empresa.id_empresa"), nullable=False)
    proveedor_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("tercero.id"), nullable=False)
    categoria_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("categoria_gasto.id"), nullable=False)
    fecha: Mapped[Optional[Date]] = mapped_column(Date)
    valor: Mapped[float] = mapped_column(Numeric(18, 2), nullable=False)
    impuesto_id: Mapped[Optional[uuid_pk]] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("impuesto.id"))
    porcentaje_impuesto: Mapped[Optional[float]] = mapped_column(Numeric(9, 4))
    descripcion: Mapped[Optional[str]] = mapped_column(Text)
    comprobante_url: Mapped[Optional[str]] = mapped_column(String(500))

    empresa = relationship("Empresa", back_populates="gastos")
    proveedor = relationship("Tercero", back_populates="gastos_proveedor")
    categoria = relationship("CategoriaGasto", back_populates="gastos")
    impuesto = relationship("Impuesto", back_populates="gastos")
    adjuntos: Mapped[List["GastoAdjunto"]] = relationship(back_populates="gasto", cascade="all, delete-orphan")
