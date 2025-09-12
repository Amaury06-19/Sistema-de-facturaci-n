from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class LogAuditoriaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    empresa_id: UUID
    usuario_id: Optional[UUID] = None
    evento_at: datetime
    tabla: str = Field(..., max_length=128)
    operacion: str = Field(..., max_length=16)
    registro_id: str = Field(..., max_length=64)
    before_data: Optional[str] = None
    after_data: Optional[str] = None
