from __future__ import annotations

from typing import List
from sqlalchemy import String, Boolean, ForeignKey, UniqueConstraint, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.documento_venta import DocumentoVenta
from .base import Base, uuid_pk


class SerieNumeracion(Base):
    __tablename__ = "serie_numeracion"

    id_serie_numeracion: Mapped[int] = mapped_column("id_serie_numeracion", primary_key=True, autoincrement=True)
    id_empresa_serie: Mapped[int] = mapped_column("id_empresa_serie", Integer, ForeignKey("empresa.id_empresa"), nullable=False)
    tipo_documento_serie: Mapped[str] = mapped_column("tipo_documento_serie", String(50), nullable=False)
    prefijo_serie: Mapped[str] = mapped_column("prefijo_serie", String(20), nullable=True)
    proximo_consecutivo_serie: Mapped[int] = mapped_column("proximo_consecutivo_serie", Integer, nullable=False, default=1)
    habilitada_serie: Mapped[bool] = mapped_column("habilitada_serie", Boolean, default=True, nullable=False)
    vigente_desde_serie: Mapped[DateTime] = mapped_column("vigente_desde_serie", DateTime, nullable=True)
    vigente_hasta_serie: Mapped[DateTime] = mapped_column("vigente_hasta_serie", DateTime, nullable=True)

    empresa = relationship("Empresa", back_populates="series")
    documentos: Mapped[List["DocumentoVenta"]] = relationship(back_populates="serie")
