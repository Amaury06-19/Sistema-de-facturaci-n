from __future__ import annotations

from typing import List, Optional
from sqlalchemy import String, Text, ForeignKey, UniqueConstraint, Date, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.documento_venta_linea import DocumentoVentaLinea
from models.pago import Pago
from .base import Base, TimestampMixin, uuid_pk


class DocumentoVenta(TimestampMixin, Base):
    __tablename__ = "documento_venta"
    __table_args__ = (UniqueConstraint("empresa_id", "tipo", "numero", name="uq_documento_venta_emp_tipo_num"),)

    id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), primary_key=True, default=uuid_pk)
    empresa_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("empresa.id_empresa"), nullable=False)
    cliente_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("tercero.id"), nullable=False)
    serie_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("serie_numeracion.id"), nullable=False)
    tipo: Mapped[str] = mapped_column(String(30), nullable=False)
    numero: Mapped[str] = mapped_column(String(40), nullable=False)
    fecha_emision: Mapped[Optional[Date]] = mapped_column(Date)
    fecha_vencimiento: Mapped[Optional[Date]] = mapped_column(Date)
    moneda: Mapped[str] = mapped_column(String(10), nullable=False)
    estado: Mapped[str] = mapped_column(String(30), nullable=False, default="borrador")
    subtotal: Mapped[float] = mapped_column(Numeric(18, 2), nullable=False, default=0)
    impuestos: Mapped[float] = mapped_column(Numeric(18, 2), nullable=False, default=0)
    total: Mapped[float] = mapped_column(Numeric(18, 2), nullable=False, default=0)
    saldo: Mapped[float] = mapped_column(Numeric(18, 2), nullable=False, default=0)
    notas: Mapped[Optional[str]] = mapped_column(Text)

    empresa = relationship("Empresa", back_populates="documentos_venta")
    cliente = relationship("Tercero", back_populates="documentos_cliente")
    serie = relationship("SerieNumeracion", back_populates="documentos")
    lineas: Mapped[List["DocumentoVentaLinea"]] = relationship(back_populates="documento", cascade="all, delete-orphan")
    pagos: Mapped[List["Pago"]] = relationship(back_populates="documento", cascade="all, delete-orphan")
