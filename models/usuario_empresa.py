from __future__ import annotations

from sqlalchemy import String, UniqueConstraint, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from .base import Base, uuid_pk



class UsuarioEmpresa(Base):
    __tablename__ = "usuario_empresa"
    __table_args__ = (UniqueConstraint("id_usuario_usuario_empresa", "id_empresa_usuario_empresa", name="uq_usuario_empresa"),)

    id = mapped_column("id_usuario_empresa", String(15), primary_key=True)
    usuario_id = mapped_column("id_usuario_usuario_empresa", String(15), ForeignKey("usuario.id_usuario"), nullable=False)
    empresa_id = mapped_column("id_empresa_usuario_empresa", String(15), ForeignKey("empresa.id_empresa"), nullable=False)
    rol = mapped_column("rol_usuario_empresa", String(100))
    activo = mapped_column("activo_usuario_empresa", Boolean, default=True)
    created_at = mapped_column("created_at_usuario_empresa", DateTime)
    updated_at = mapped_column("updated_at_usuario_empresa", DateTime)
