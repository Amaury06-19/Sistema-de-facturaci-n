from uuid import UUID
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class DocumentoVentaLineaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    documento_id: UUID
    producto_id: UUID
    descripcion: Optional[str] = None
    cantidad: Decimal = Field(..., max_digits=18, decimal_places=4)
    precio_unitario: Decimal = Field(..., max_digits=18, decimal_places=2)
    impuesto_id: Optional[UUID] = None
    porcentaje_impuesto: Optional[Decimal] = Field(None, max_digits=9, decimal_places=4)
    total_linea: Decimal = Field(..., max_digits=18, decimal_places=2)

class DocumentoVentaLineaCreate(DocumentoVentaLineaBase):
    pass

class DocumentoVentaLineaUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    descripcion: Optional[str] = None
    cantidad: Optional[Decimal] = Field(None, max_digits=18, decimal_places=4)
    precio_unitario: Optional[Decimal] = Field(None, max_digits=18, decimal_places=2)
    impuesto_id: Optional[UUID] = None
    porcentaje_impuesto: Optional[Decimal] = Field(None, max_digits=9, decimal_places=4)
    total_linea: Optional[Decimal] = Field(None, max_digits=18, decimal_places=2)

class DocumentoVentaLineaRead(DocumentoVentaLineaBase):
    id: UUID
