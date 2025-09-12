from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class TerceroBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    empresa_id: UUID
    tipo: str = Field(..., max_length=30)
    nombre: str = Field(..., max_length=200)
    identificacion: Optional[str] = Field(None, max_length=50)
    email: Optional[EmailStr] = None
    telefono: Optional[str] = Field(None, max_length=50)
    direccion: Optional[str] = Field(None, max_length=300)
    condiciones_pago_dias: Optional[int] = None

class TerceroCreate(TerceroBase):
    pass

class TerceroUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    tipo: Optional[str] = Field(None, max_length=30)
    nombre: Optional[str] = Field(None, max_length=200)
    identificacion: Optional[str] = Field(None, max_length=50)
    email: Optional[EmailStr] = None
    telefono: Optional[str] = Field(None, max_length=50)
    direccion: Optional[str] = Field(None, max_length=300)
    condiciones_pago_dias: Optional[int] = None

class TerceroRead(TerceroBase):
    id: UUID
