from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class SerieNumeracionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    empresa_id: UUID
    tipo_documento: str = Field(..., max_length=30)
    prefijo: str = Field(..., max_length=10)
    proximo_consecutivo: int = 1
    habilitada: bool = True
    vigente_desde: Optional[datetime] = None
    vigente_hasta: Optional[datetime] = None

class SerieNumeracionCreate(SerieNumeracionBase):
    pass

class SerieNumeracionUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    tipo_documento: Optional[str] = Field(None, max_length=30)
    prefijo: Optional[str] = Field(None, max_length=10)
    proximo_consecutivo: Optional[int] = None
    habilitada: Optional[bool] = None
    vigente_desde: Optional[datetime] = None
    vigente_hasta: Optional[datetime] = None

class SerieNumeracionRead(SerieNumeracionBase):
    id: UUID
