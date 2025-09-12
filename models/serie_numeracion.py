from __future__ import annotations

from typing import List
from sqlalchemy import String, Boolean, ForeignKey, UniqueConstraint, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.documento_venta import DocumentoVenta
from .base import Base, uuid_pk


class SerieNumeracion(Base):
    __tablename__ = "serie_numeracion"
    __table_args__ = (UniqueConstraint("empresa_id", "tipo_documento", "prefijo", name="uq_serie_empresa_tipo_prefijo"),)

    id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), primary_key=True, default=uuid_pk)
    empresa_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("empresa.id_empresa"), nullable=False)
    tipo_documento: Mapped[str] = mapped_column(String(30), nullable=False)
    prefijo: Mapped[str] = mapped_column(String(10), nullable=False)
    proximo_consecutivo: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    habilitada: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    vigente_desde: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=True)
    vigente_hasta: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=True)

    empresa = relationship("Empresa", back_populates="series")
    documentos: Mapped[List["DocumentoVenta"]] = relationship(back_populates="serie")
