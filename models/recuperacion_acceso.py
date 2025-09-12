from __future__ import annotations

from typing import Optional
from sqlalchemy import String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from .base import Base, uuid_pk


class RecuperacionAcceso(Base):
    __tablename__ = "recuperacion_acceso"
    __table_args__ = (UniqueConstraint("token_hash", name="uq_recuperacion_token"),)

    id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), primary_key=True, default=uuid_pk)
    usuario_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("usuario.id_usuario"), nullable=False)
    token_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    expires_at: Mapped[Optional[DateTime]] = mapped_column(DateTime(timezone=True))
    used_at: Mapped[Optional[DateTime]] = mapped_column(DateTime(timezone=True))
    ip_solicitud: Mapped[Optional[str]] = mapped_column(String(45))
