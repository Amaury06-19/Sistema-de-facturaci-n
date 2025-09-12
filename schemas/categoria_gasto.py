from uuid import UUID
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class CategoriaGastoBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    empresa_id: UUID
    nombre: str = Field(..., max_length=120)
    activo: bool = True

class CategoriaGastoCreate(CategoriaGastoBase):
    pass

class CategoriaGastoUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    nombre: Optional[str] = Field(None, max_length=120)
    activo: Optional[bool] = None

class CategoriaGastoRead(CategoriaGastoBase):
    id: UUID
