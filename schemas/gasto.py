from uuid import UUID
from decimal import Decimal
from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field
from .gasto_adjunto import GastoAdjuntoRead

class GastoBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    empresa_id: UUID
    proveedor_id: UUID
    categoria_id: UUID
    fecha: Optional[date] = None
    valor: Decimal = Field(..., max_digits=18, decimal_places=2)
    impuesto_id: Optional[UUID] = None
    porcentaje_impuesto: Optional[Decimal] = Field(None, max_digits=9, decimal_places=4)
    descripcion: Optional[str] = None
    comprobante_url: Optional[str] = Field(None, max_length=500)

class GastoCreate(GastoBase):
    pass

class GastoUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    proveedor_id: Optional[UUID] = None
    categoria_id: Optional[UUID] = None
    fecha: Optional[date] = None
    valor: Optional[Decimal] = Field(None, max_digits=18, decimal_places=2)
    impuesto_id: Optional[UUID] = None
    porcentaje_impuesto: Optional[Decimal] = Field(None, max_digits=9, decimal_places=4)
    descripcion: Optional[str] = None
    comprobante_url: Optional[str] = Field(None, max_length=500)

class GastoRead(GastoBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    adjuntos: List[GastoAdjuntoRead] = []
