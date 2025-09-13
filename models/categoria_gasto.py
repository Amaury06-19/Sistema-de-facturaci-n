from __future__ import annotations

from typing import List, Optional
from sqlalchemy import String, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.gasto import Gasto
from .base import Base, TimestampMixin, uuid_pk


class CategoriaGasto(Base):
    __tablename__ = "categoria_gasto"
    __table_args__ = (UniqueConstraint("id_empresa_categoria_gasto", "nombre_categoria_gasto", name="uq_categoria_gasto_emp_nombre"),)

    id_categoria_gasto: Mapped[int] = mapped_column("id_categoria_gasto", primary_key=True, autoincrement=True)
    id_empresa_categoria_gasto: Mapped[int] = mapped_column("id_empresa_categoria_gasto", ForeignKey("empresa.id_empresa"), nullable=False)
    nombre_categoria_gasto: Mapped[str] = mapped_column("nombre_categoria_gasto", String(150), nullable=False)
    activo_categoria_gasto: Mapped[bool] = mapped_column("activo_categoria_gasto", Boolean, default=True, nullable=False)
    created_at_categoria_gasto: Mapped[Optional[str]] = mapped_column("created_at_categoria_gasto")
    updated_at_categoria_gasto: Mapped[Optional[str]] = mapped_column("updated_at_categoria_gasto")

    empresa = relationship("Empresa", back_populates="categorias_gasto")
    gastos: Mapped[List["Gasto"]] = relationship(back_populates="categoria")
