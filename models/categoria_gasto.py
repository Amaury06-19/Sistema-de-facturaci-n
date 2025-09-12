from __future__ import annotations

from typing import List
from sqlalchemy import String, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.gasto import Gasto
from .base import Base, TimestampMixin, uuid_pk


class CategoriaGasto(TimestampMixin, Base):
    __tablename__ = "categoria_gasto"
    __table_args__ = (UniqueConstraint("empresa_id", "nombre", name="uq_categoria_gasto_emp_nombre"),)

    id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), primary_key=True, default=uuid_pk)
    empresa_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("empresa.id_empresa"), nullable=False)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    activo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    empresa = relationship("Empresa", back_populates="categorias_gasto")
    gastos: Mapped[List["Gasto"]] = relationship(back_populates="categoria")
