from __future__ import annotations

from typing import Optional, List
from sqlalchemy import String, Text, ForeignKey, Numeric, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.gasto_adjunto import GastoAdjunto
from .base import Base, TimestampMixin, uuid_pk


class Gasto(Base):
    __tablename__ = "gasto"

    id_gasto: Mapped[int] = mapped_column("id_gasto", primary_key=True, autoincrement=True)
    id_empresa_gasto: Mapped[int] = mapped_column("id_empresa_gasto", ForeignKey("empresa.id_empresa"), nullable=False)
    id_tercero_gasto: Mapped[Optional[int]] = mapped_column("id_tercero_gasto", ForeignKey("tercero.id_tercero"))
    id_categoria_gasto: Mapped[Optional[int]] = mapped_column("id_categoria_gasto", ForeignKey("categoria_gasto.id_categoria_gasto"))
    fecha_gasto: Mapped[Optional[Date]] = mapped_column("fecha_gasto", Date)
    valor_gasto: Mapped[float] = mapped_column("valor_gasto", Numeric(14, 2), nullable=False, default=0.00)
    id_impuesto_gasto: Mapped[Optional[int]] = mapped_column("id_impuesto_gasto", ForeignKey("impuesto.id_impuesto"))
    porcentaje_impuesto_gasto: Mapped[Optional[float]] = mapped_column("porcentaje_impuesto_gasto", Numeric(5, 2), default=0.00)
    descripcion_gasto: Mapped[Optional[str]] = mapped_column("descripcion_gasto", Text)
    comprobante_url_gasto: Mapped[Optional[str]] = mapped_column("comprobante_url_gasto", String(255))
    created_by_id_usuario_gasto: Mapped[Optional[int]] = mapped_column("created_by_id_usuario_gasto", ForeignKey("usuario.id_usuario"))
    created_at_gasto: Mapped[Optional[str]] = mapped_column("created_at_gasto")
    updated_at_gasto: Mapped[Optional[str]] = mapped_column("updated_at_gasto")
    deleted_at_gasto: Mapped[Optional[str]] = mapped_column("deleted_at_gasto")

    empresa = relationship("Empresa", back_populates="gastos")
    tercero = relationship("Tercero", back_populates="gastos_proveedor", foreign_keys=[id_tercero_gasto])
    categoria = relationship("CategoriaGasto", back_populates="gastos")
    impuesto = relationship("Impuesto", back_populates="gastos", foreign_keys=[id_impuesto_gasto])
    usuario_creador = relationship("Usuario", foreign_keys=[created_by_id_usuario_gasto])
    adjuntos: Mapped[List["GastoAdjunto"]] = relationship(back_populates="gasto", cascade="all, delete-orphan")
