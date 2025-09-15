from uuid import UUID
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class ImpuestoBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_empresa_impuesto: int
    nombre_impuesto: str = Field(..., max_length=100)
    porcentaje_impuesto: Decimal = Field(..., max_digits=9, decimal_places=4)
    activo_impuesto: bool = True

class ImpuestoCreate(ImpuestoBase):
    pass

class ImpuestoUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    nombre_impuesto: Optional[str] = Field(None, max_length=100)
    porcentaje_impuesto: Optional[Decimal] = Field(None, max_digits=9, decimal_places=4)
    activo_impuesto: Optional[bool] = None

class ImpuestoRead(ImpuestoBase):
    id_impuesto: int
