from uuid import UUID
from decimal import Decimal
from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field
from .documento_venta_linea import DocumentoVentaLineaRead
from .pago import PagoRead

class DocumentoVentaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    empresa_id: UUID
    cliente_id: UUID
    serie_id: UUID
    tipo: str = Field(..., max_length=30)
    numero: str = Field(..., max_length=40)
    fecha_emision: Optional[date] = None
    fecha_vencimiento: Optional[date] = None
    moneda: str = Field(..., max_length=10)
    estado: str = Field(default="borrador", max_length=30)
    subtotal: Decimal = Field(default=0, max_digits=18, decimal_places=2)
    impuestos: Decimal = Field(default=0, max_digits=18, decimal_places=2)
    total: Decimal = Field(default=0, max_digits=18, decimal_places=2)
    saldo: Decimal = Field(default=0, max_digits=18, decimal_places=2)
    notas: Optional[str] = None

class DocumentoVentaCreate(DocumentoVentaBase):
    pass

class DocumentoVentaUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    cliente_id: Optional[UUID] = None
    serie_id: Optional[UUID] = None
    tipo: Optional[str] = Field(None, max_length=30)
    numero: Optional[str] = Field(None, max_length=40)
    fecha_emision: Optional[date] = None
    fecha_vencimiento: Optional[date] = None
    moneda: Optional[str] = Field(None, max_length=10)
    estado: Optional[str] = Field(None, max_length=30)
    subtotal: Optional[Decimal] = Field(None, max_digits=18, decimal_places=2)
    impuestos: Optional[Decimal] = Field(None, max_digits=18, decimal_places=2)
    total: Optional[Decimal] = Field(None, max_digits=18, decimal_places=2)
    saldo: Optional[Decimal] = Field(None, max_digits=18, decimal_places=2)
    notas: Optional[str] = None

class DocumentoVentaRead(DocumentoVentaBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    lineas: List[DocumentoVentaLineaRead] = []
    pagos: List[PagoRead] = []
