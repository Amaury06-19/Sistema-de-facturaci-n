from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class LogAccesoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    usuario_id: UUID
    evento_at: datetime
    evento: str = Field(..., max_length=50)
    ip: Optional[str] = Field(None, max_length=45)
    user_agent: Optional[str] = Field(None, max_length=500)
