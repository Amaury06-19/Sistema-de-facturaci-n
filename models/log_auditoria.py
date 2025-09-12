from __future__ import annotations

from sqlalchemy import String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from .base import Base, uuid_pk


class LogAuditoria(Base):
    __tablename__ = "log_auditoria"

    id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), primary_key=True, default=uuid_pk)
    empresa_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("empresa.id_empresa"), nullable=False)
    usuario_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("usuario.id"), nullable=True)
    evento_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.sysdatetime(), nullable=False)
    tabla: Mapped[str] = mapped_column(String(128), nullable=False)
    operacion: Mapped[str] = mapped_column(String(16), nullable=False)
    registro_id: Mapped[str] = mapped_column(String(64), nullable=False)
    before_data: Mapped[str] = mapped_column(Text, nullable=True)
    after_data: Mapped[str] = mapped_column(Text, nullable=True)

    empresa = relationship("Empresa", back_populates="auditorias")
