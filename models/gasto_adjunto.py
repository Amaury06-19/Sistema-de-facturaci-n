from __future__ import annotations

from sqlalchemy import String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from .base import Base, uuid_pk


class GastoAdjunto(Base):
    __tablename__ = "gasto_adjunto"

    id: Mapped[int] = mapped_column("id_gasto_adjunto", primary_key=True, autoincrement=True)
    gasto_id: Mapped[int] = mapped_column("id_gasto", ForeignKey("gasto.id_gasto"), nullable=False)
    filename: Mapped[str] = mapped_column(String(260), nullable=False)
    content_type: Mapped[str] = mapped_column(String(120), nullable=False)
    size_bytes: Mapped[int] = mapped_column(Integer, nullable=False)
    storage_path: Mapped[str] = mapped_column(String(500), nullable=False)
    uploaded_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.sysdatetime(), nullable=False)

    gasto = relationship("Gasto", back_populates="adjuntos")
