from uuid import UUID
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class GastoAdjuntoBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    gasto_id: UUID
    filename: str = Field(..., max_length=260)
    content_type: str = Field(..., max_length=120)
    size_bytes: int
    storage_path: str = Field(..., max_length=500)

class GastoAdjuntoCreate(GastoAdjuntoBase):
    pass

class GastoAdjuntoRead(GastoAdjuntoBase):
    id: UUID
