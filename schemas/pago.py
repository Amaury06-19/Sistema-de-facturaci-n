
from decimal import Decimal
from typing import Optional
from datetime import date
from pydantic import BaseModel, ConfigDict, Field

class PagoBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_documento_venta: int
    fecha_pago: Optional[date] = None
    monto_pago: Decimal = Field(..., max_digits=18, decimal_places=2)
    metodo_pago: str = Field(..., max_length=40)
    referencia_pago: Optional[str] = Field(None, max_length=100)

class PagoCreate(PagoBase):
    pass

class PagoUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    fecha_pago: Optional[date] = None
    monto_pago: Optional[Decimal] = Field(None, max_digits=18, decimal_places=2)
    metodo_pago: Optional[str] = Field(None, max_length=40)
    referencia_pago: Optional[str] = Field(None, max_length=100)

class PagoRead(PagoBase):
    id_pago: int
