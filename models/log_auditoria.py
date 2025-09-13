from __future__ import annotations

from sqlalchemy import String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from .base import Base, uuid_pk


class LogAuditoria(Base):
    __tablename__ = "log_auditoria"

    id_log_auditoria: Mapped[int] = mapped_column("id_log_auditoria", primary_key=True, autoincrement=True)
    id_empresa_log_auditoria: Mapped[int] = mapped_column("id_empresa_log_auditoria", ForeignKey("empresa.id_empresa"), nullable=False)
    id_usuario_log_auditoria: Mapped[int] = mapped_column("id_usuario_log_auditoria", ForeignKey("usuario.id_usuario"), nullable=False)
    evento_at_log_auditoria: Mapped[DateTime] = mapped_column("evento_at_log_auditoria", DateTime, nullable=False)
    tabla_log_auditoria: Mapped[str] = mapped_column("tabla_log_auditoria", String(150), nullable=True)
    operacion_log_auditoria: Mapped[str] = mapped_column("operacion_log_auditoria", String(50), nullable=True)
    registro_id_log_auditoria: Mapped[str] = mapped_column("registro_id_log_auditoria", String(200), nullable=True)
    before_data_log_auditoria: Mapped[str] = mapped_column("before_data_log_auditoria", Text, nullable=True)
    after_data_log_auditoria: Mapped[str] = mapped_column("after_data_log_auditoria", Text, nullable=True)

    empresa = relationship("Empresa", back_populates="auditorias")
