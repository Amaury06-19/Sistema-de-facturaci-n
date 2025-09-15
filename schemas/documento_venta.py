from decimal import Decimal
from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field
from .documento_venta_linea import DocumentoVentaLineaRead
from .pago import PagoRead

class DocumentoVentaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_empresa_documento_venta: int
    id_tercero_documento_venta: Optional[int] = None
    id_serie_documento_venta: Optional[int] = None
    tipo_documento_documento_venta: Optional[str] = Field(None, max_length=50)
    numero_documento_documento_venta: Optional[str] = Field(None, max_length=100)
    fecha_emision_documento_venta: Optional[date] = None
    fecha_vencimiento_documento_venta: Optional[date] = None
    moneda_documento_venta: Optional[str] = Field(None, max_length=10)
    estado_documento_venta: Optional[str] = Field(None, max_length=50)
    subtotal_documento_venta: Decimal = Field(default=0, max_digits=14, decimal_places=2)
    impuestos_documento_venta: Decimal = Field(default=0, max_digits=14, decimal_places=2)
    total_documento_venta: Decimal = Field(default=0, max_digits=14, decimal_places=2)
    saldo_documento_venta: Decimal = Field(default=0, max_digits=14, decimal_places=2)
    notas_documento_venta: Optional[str] = None

class DocumentoVentaCreate(DocumentoVentaBase):
    pass

class DocumentoVentaUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_tercero_documento_venta: Optional[int] = None
    id_serie_documento_venta: Optional[int] = None
    tipo_documento_documento_venta: Optional[str] = Field(None, max_length=50)
    numero_documento_documento_venta: Optional[str] = Field(None, max_length=100)
    fecha_emision_documento_venta: Optional[date] = None
    fecha_vencimiento_documento_venta: Optional[date] = None
    moneda_documento_venta: Optional[str] = Field(None, max_length=10)
    estado_documento_venta: Optional[str] = Field(None, max_length=50)
    subtotal_documento_venta: Optional[Decimal] = Field(None, max_digits=14, decimal_places=2)
    impuestos_documento_venta: Optional[Decimal] = Field(None, max_digits=14, decimal_places=2)
    total_documento_venta: Optional[Decimal] = Field(None, max_digits=14, decimal_places=2)
    saldo_documento_venta: Optional[Decimal] = Field(None, max_digits=14, decimal_places=2)
    notas_documento_venta: Optional[str] = None

class DocumentoVentaRead(DocumentoVentaBase):
    id_documento_venta: int
    created_at_documento_venta: Optional[datetime] = None
    updated_at_documento_venta: Optional[datetime] = None
    lineas: List[DocumentoVentaLineaRead] = []
    pagos: List[PagoRead] = []
