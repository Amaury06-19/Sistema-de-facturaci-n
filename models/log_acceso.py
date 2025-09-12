from __future__ import annotations

from sqlalchemy import String, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from .base import Base, uuid_pk


class LogAcceso(Base):
    __tablename__ = "log_acceso"

    id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), primary_key=True, default=uuid_pk)
    usuario_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=False)
    evento_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.sysdatetime(), nullable=False)
    evento: Mapped[str] = mapped_column(String(50), nullable=False)
    ip: Mapped[str] = mapped_column(String(45), nullable=True)
    user_agent: Mapped[str] = mapped_column(String(500), nullable=True)

    usuario = relationship("Usuario", back_populates="accesos")
