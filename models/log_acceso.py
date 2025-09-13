from __future__ import annotations

from sqlalchemy import String, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from .base import Base, uuid_pk


class LogAcceso(Base):
    __tablename__ = "log_acceso"

    id: Mapped[int] = mapped_column("id_log_acceso", primary_key=True, autoincrement=True)
    usuario_id: Mapped[int] = mapped_column("id_usuario_log_acceso", ForeignKey("usuario.id_usuario"), nullable=False)
    evento_at: Mapped[DateTime] = mapped_column("evento_at_log_acceso", DateTime(timezone=True), server_default=func.sysdatetime(), nullable=False)
    evento: Mapped[str] = mapped_column("evento_log_acceso", String(100), nullable=False)
    ip: Mapped[str] = mapped_column("ip_log_acceso", String(50), nullable=True)
    user_agent: Mapped[str] = mapped_column("user_agent_log_acceso", String(255), nullable=True)

    usuario = relationship("Usuario", back_populates="accesos")
