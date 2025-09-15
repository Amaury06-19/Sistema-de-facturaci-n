from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class ProductoBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_empresa_producto: int
    codigo_producto: str = Field(..., max_length=60)
    nombre_producto: str = Field(..., max_length=200)
    precio_unitario_producto: Decimal = Field(..., max_digits=18, decimal_places=2)
    id_impuesto_producto: Optional[int] = Field(default=None)
    activo_producto: bool = True

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    codigo_producto: Optional[str] = Field(None, max_length=60)
    nombre_producto: Optional[str] = Field(None, max_length=200)
    precio_unitario_producto: Optional[Decimal] = Field(None, max_digits=18, decimal_places=2)
    id_impuesto_producto: Optional[int] = None
    activo_producto: Optional[bool] = None

from datetime import datetime

class ProductoRead(ProductoBase):
    id_producto: int
    created_at_producto: Optional[datetime] = None
    updated_at_producto: Optional[datetime] = None
