from __future__ import annotations

from typing import Optional, List
from sqlalchemy import String, Integer, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.documento_venta import DocumentoVenta
from models.gasto import Gasto
from .base import Base, TimestampMixin, uuid_pk


class Tercero(Base):
    __tablename__ = "tercero"

    id_tercero: Mapped[int] = mapped_column("id_tercero", primary_key=True, autoincrement=True)
    id_empresa_tercero: Mapped[int] = mapped_column("id_empresa_tercero", Integer, ForeignKey("empresa.id_empresa"), nullable=False)
    tipo_tercero_tercero: Mapped[Optional[str]] = mapped_column("tipo_tercero_tercero", String(50))
    nombre_tercero: Mapped[str] = mapped_column("nombre_tercero", String(200), nullable=False)
    identificacion_tercero: Mapped[Optional[str]] = mapped_column("identificacion_tercero", String(100), unique=True)
    email_tercero: Mapped[Optional[str]] = mapped_column("email_tercero", String(150))
    telefono_tercero: Mapped[Optional[str]] = mapped_column("telefono_tercero", String(50))
    direccion_tercero: Mapped[Optional[str]] = mapped_column("direccion_tercero", String)
    condiciones_pago_dias_tercero: Mapped[Optional[int]] = mapped_column("condiciones_pago_dias_tercero", Integer)
    created_at_tercero: Mapped[Optional[str]] = mapped_column("created_at_tercero")
    created_by_id_usuario_tercero: Mapped[Optional[int]] = mapped_column("created_by_id_usuario_tercero", Integer)
    updated_at_tercero: Mapped[Optional[str]] = mapped_column("updated_at_tercero")
    updated_by_id_usuario_tercero: Mapped[Optional[int]] = mapped_column("updated_by_id_usuario_tercero", Integer)
    deleted_at_tercero: Mapped[Optional[str]] = mapped_column("deleted_at_tercero")

    empresa = relationship("Empresa", back_populates="terceros")
    documentos_cliente: Mapped[List["DocumentoVenta"]] = relationship(back_populates="cliente")
    gastos_proveedor: Mapped[List["Gasto"]] = relationship(back_populates="tercero")
