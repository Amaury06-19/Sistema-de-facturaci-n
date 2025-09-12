from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class EmpresaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    nombre: str = Field(..., max_length=200)
    nit: str = Field(..., max_length=30)
    email: Optional[EmailStr] = None
    telefono: Optional[str] = Field(None, max_length=50)
    direccion: Optional[str] = Field(None, max_length=300)
    moneda: str = Field(..., max_length=10)

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    nombre: Optional[str] = Field(None, max_length=200)
    nit: Optional[str] = Field(None, max_length=30)
    email: Optional[EmailStr] = None
    telefono: Optional[str] = Field(None, max_length=50)
    direccion: Optional[str] = Field(None, max_length=300)
    moneda: Optional[str] = Field(None, max_length=10)

class EmpresaRead(EmpresaBase):
    id: UUID
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
