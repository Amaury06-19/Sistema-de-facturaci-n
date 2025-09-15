from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime

class TerceroBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_empresa_tercero: int
    tipo_tercero_tercero: Optional[str] = Field(None, max_length=50)
    nombre_tercero: str = Field(..., max_length=200)
    identificacion_tercero: Optional[str] = Field(None, max_length=100)
    email_tercero: Optional[EmailStr] = None
    telefono_tercero: Optional[str] = Field(None, max_length=50)
    direccion_tercero: Optional[str] = None
    condiciones_pago_dias_tercero: Optional[int] = None

class TerceroCreate(TerceroBase):
    pass

class TerceroUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    tipo_tercero_tercero: Optional[str] = Field(None, max_length=50)
    nombre_tercero: Optional[str] = Field(None, max_length=200)
    identificacion_tercero: Optional[str] = Field(None, max_length=100)
    email_tercero: Optional[EmailStr] = None
    telefono_tercero: Optional[str] = Field(None, max_length=50)
    direccion_tercero: Optional[str] = None
    condiciones_pago_dias_tercero: Optional[int] = None

class TerceroRead(TerceroBase):
    id_tercero: int
    created_at_tercero: Optional[datetime] = None
    updated_at_tercero: Optional[datetime] = None
