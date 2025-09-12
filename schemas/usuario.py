from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class UsuarioBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    nombre: str = Field(..., max_length=200)
    email: EmailStr
    activo: bool = True
    is_superadmin: bool = False

class UsuarioCreate(UsuarioBase):
    password: str = Field(..., min_length=8, max_length=128)

class UsuarioUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    nombre: Optional[str] = Field(None, max_length=200)
    email: Optional[EmailStr] = None
    activo: Optional[bool] = None
    is_superadmin: Optional[bool] = None
    password: Optional[str] = Field(None, min_length=8, max_length=128)

class UsuarioRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    nombre: str
    email: EmailStr
    activo: bool
    is_superadmin: bool
    last_login_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime

class AuthUserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    nombre: str
    email: EmailStr
    is_superadmin: bool
