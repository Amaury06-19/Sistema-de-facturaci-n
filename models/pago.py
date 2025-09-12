from __future__ import annotations

from typing import Optional
from datetime import date
from sqlalchemy import String, ForeignKey, Date, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from .base import Base, uuid_pk


class Pago(Base):
    __tablename__ = "pago"

    id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), primary_key=True, default=uuid_pk)
    documento_id: Mapped[uuid_pk] = mapped_column(UNIQUEIDENTIFIER(as_uuid=True), ForeignKey("documento_venta.id"), nullable=False)
    fecha: Mapped[Optional[date]] = mapped_column(Date)
    monto: Mapped[float] = mapped_column(Numeric(18, 2), nullable=False)
    metodo: Mapped[str] = mapped_column(String(40), nullable=False)
    referencia: Mapped[Optional[str]] = mapped_column(String(100))

    documento = relationship("DocumentoVenta", back_populates="pagos")
