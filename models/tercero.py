from __future__ import annotations

from typing import Optional, List
from sqlalchemy import String, Integer, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.documento_venta import DocumentoVenta
from models.gasto import Gasto
from .base import Base, TimestampMixin, uuid_pk


class Tercero(TimestampMixin, Base):
    __tablename__ = "tercero"

    id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), primary_key=True, default=uuid_pk)
    empresa_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("empresa.id_empresa"), nullable=False)
    tipo: Mapped[str] = mapped_column(String(30), nullable=False)
    nombre: Mapped[str] = mapped_column(String(200), nullable=False)
    identificacion: Mapped[Optional[str]] = mapped_column(String(50))
    email: Mapped[Optional[str]] = mapped_column(String(320))
    telefono: Mapped[Optional[str]] = mapped_column(String(50))
    direccion: Mapped[Optional[str]] = mapped_column(String(300))
    condiciones_pago_dias: Mapped[Optional[int]] = mapped_column(Integer)

    empresa = relationship("Empresa", back_populates="terceros")
    documentos_cliente: Mapped[List["DocumentoVenta"]] = relationship(back_populates="cliente")
    gastos_proveedor: Mapped[List["Gasto"]] = relationship(back_populates="proveedor")

    __table_args__ = (
        Index("ix_tercero_empresa_tipo_ident", "empresa_id", "tipo", "identificacion"),
    )
