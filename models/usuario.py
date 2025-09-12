from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.log_acceso import LogAcceso
from models.usuario_empresa import UsuarioEmpresa
from .base import Base, TimestampMixin, uuid_pk



class Usuario(Base):
    @property
    def id(self):
        return self.id_usuario
    __tablename__ = "usuario"
    id = mapped_column("id_usuario", String(36), primary_key=True, default=uuid_pk)
    nombre = mapped_column("nombre_usuario", String(150), nullable=False)
    email = mapped_column("email_usuario", String(150), unique=True, nullable=False)
    password_hash = mapped_column("password_hash_usuario", String(255), nullable=False)
    activo = mapped_column("activo_usuario", Boolean, default=True)
    is_superadmin = mapped_column("is_superadmin_usuario", Boolean, default=False)
    last_login_at = mapped_column("last_login_at_usuario", DateTime)
    created_at = mapped_column("created_at_usuario", DateTime)
    updated_at = mapped_column("updated_at_usuario", DateTime)
    deleted_at = mapped_column("deleted_at_usuario", DateTime)

    accesos: Mapped[List["LogAcceso"]] = relationship("LogAcceso", back_populates="usuario")
