from __future__ import annotations

from typing import Optional
from datetime import date
from sqlalchemy import String, ForeignKey, Date, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from .base import Base, uuid_pk


class Pago(Base):
    __tablename__ = "pago"

    id_pago: Mapped[int] = mapped_column("id_pago", primary_key=True, autoincrement=True)
    id_documento_venta: Mapped[int] = mapped_column("id_documento_venta", ForeignKey("documento_venta.id_documento_venta"), nullable=False)
    fecha_pago: Mapped[Optional[date]] = mapped_column("fecha_pago", Date)
    monto_pago: Mapped[float] = mapped_column("monto_pago", Numeric(18, 2), nullable=False)
    metodo_pago: Mapped[str] = mapped_column("metodo_pago", String(40), nullable=False)
    referencia_pago: Mapped[Optional[str]] = mapped_column("referencia_pago", String(100))

    documento = relationship("DocumentoVenta", back_populates="pagos")
