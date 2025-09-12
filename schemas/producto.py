from uuid import UUID
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class ProductoBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    empresa_id: UUID
    codigo: str = Field(..., max_length=60)
    nombre: str = Field(..., max_length=200)
    precio_unitario: Decimal = Field(..., max_digits=18, decimal_places=2)
    impuesto_id: Optional[UUID] = None
    activo: bool = True

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    codigo: Optional[str] = Field(None, max_length=60)
    nombre: Optional[str] = Field(None, max_length=200)
    precio_unitario: Optional[Decimal] = Field(None, max_digits=18, decimal_places=2)
    impuesto_id: Optional[UUID] = None
    activo: Optional[bool] = None

class ProductoRead(ProductoBase):
    id: UUID
