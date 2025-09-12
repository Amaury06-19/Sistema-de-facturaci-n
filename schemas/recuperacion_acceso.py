from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class RecuperacionAccesoCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    usuario_id: UUID

class RecuperacionAccesoUseToken(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    token: str = Field(..., min_length=32)

class RecuperacionAccesoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    usuario_id: UUID
    token_hash: str
    expires_at: Optional[datetime] = None
    used_at: Optional[datetime] = None
    ip_solicitud: Optional[str] = Field(None, max_length=45)
