from uuid import UUID
from decimal import Decimal
from typing import Optional
from datetime import date
from pydantic import BaseModel, ConfigDict, Field

class PagoBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    documento_id: UUID
    fecha: Optional[date] = None
    monto: Decimal = Field(..., max_digits=18, decimal_places=2)
    metodo: str = Field(..., max_length=40)
    referencia: Optional[str] = Field(None, max_length=100)

class PagoCreate(PagoBase):
    pass

class PagoUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    fecha: Optional[date] = None
    monto: Optional[Decimal] = Field(None, max_digits=18, decimal_places=2)
    metodo: Optional[str] = Field(None, max_length=40)
    referencia: Optional[str] = Field(None, max_length=100)

class PagoRead(PagoBase):
    id: UUID
