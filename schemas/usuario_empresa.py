from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field

class UsuarioEmpresaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    usuario_id: UUID
    empresa_id: UUID
    rol: str = Field(..., max_length=50)
    activo: bool = True

class UsuarioEmpresaCreate(UsuarioEmpresaBase):
    pass

class UsuarioEmpresaUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    rol: Optional[str] = Field(None, max_length=50)
    activo: Optional[bool] = None

class UsuarioEmpresaRead(UsuarioEmpresaBase):
    id: UUID
