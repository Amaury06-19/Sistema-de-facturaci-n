from uuid import UUID
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class ImpuestoBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    empresa_id: UUID
    nombre: str = Field(..., max_length=100)
    porcentaje: Decimal = Field(..., max_digits=9, decimal_places=4)
    activo: bool = True

class ImpuestoCreate(ImpuestoBase):
    pass

class ImpuestoUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    nombre: Optional[str] = Field(None, max_length=100)
    porcentaje: Optional[Decimal] = Field(None, max_digits=9, decimal_places=4)
    activo: Optional[bool] = None

class ImpuestoRead(ImpuestoBase):
    id: UUID
