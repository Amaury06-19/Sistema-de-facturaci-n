
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class SerieNumeracionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_empresa_serie: int
    tipo_documento_serie: str = Field(..., max_length=50)
    prefijo_serie: Optional[str] = Field(None, max_length=20)
    proximo_consecutivo_serie: int = 1
    habilitada_serie: bool = True
    vigente_desde_serie: Optional[datetime] = None
    vigente_hasta_serie: Optional[datetime] = None

class SerieNumeracionCreate(SerieNumeracionBase):
    pass

class SerieNumeracionUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    tipo_documento_serie: Optional[str] = Field(None, max_length=50)
    prefijo_serie: Optional[str] = Field(None, max_length=20)
    proximo_consecutivo_serie: Optional[int] = None
    habilitada_serie: Optional[bool] = None
    vigente_desde_serie: Optional[datetime] = None
    vigente_hasta_serie: Optional[datetime] = None

class SerieNumeracionRead(SerieNumeracionBase):
    id_serie_numeracion: int
