from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class EmpresaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    nombre_empresa: str = Field(..., max_length=200)
    nit_empresa: str = Field(..., max_length=50)
    email_empresa: Optional[EmailStr] = None
    telefono_empresa: Optional[str] = Field(None, max_length=50)
    direccion_empresa: Optional[str] = Field(None, max_length=300)
    moneda_empresa: str = Field(..., max_length=10)

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    nombre_empresa: Optional[str] = Field(None, max_length=200)
    nit_empresa: Optional[str] = Field(None, max_length=50)
    email_empresa: Optional[EmailStr] = None
    telefono_empresa: Optional[str] = Field(None, max_length=50)
    direccion_empresa: Optional[str] = Field(None, max_length=300)
    moneda_empresa: Optional[str] = Field(None, max_length=10)

class EmpresaRead(EmpresaBase):
    id_empresa: int
    created_at_empresa: Optional[str] = None
    updated_at_empresa: Optional[str] = None
