from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class DocumentoVentaLineaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_documento_venta_linea_fk: int
    id_producto_documento_venta_linea: Optional[int] = None
    descripcion_documento_venta_linea: Optional[str] = None
    cantidad_documento_venta_linea: Decimal = Field(..., max_digits=12, decimal_places=4)
    precio_unitario_documento_venta_linea: Decimal = Field(..., max_digits=14, decimal_places=4)
    id_impuesto_documento_venta_linea: Optional[int] = None
    porcentaje_impuesto_documento_venta_linea: Optional[Decimal] = Field(None, max_digits=5, decimal_places=2)
    total_linea_documento_venta_linea: Decimal = Field(..., max_digits=14, decimal_places=2)

class DocumentoVentaLineaCreate(DocumentoVentaLineaBase):
    pass

class DocumentoVentaLineaUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    descripcion_documento_venta_linea: Optional[str] = None
    cantidad_documento_venta_linea: Optional[Decimal] = Field(None, max_digits=12, decimal_places=4)
    precio_unitario_documento_venta_linea: Optional[Decimal] = Field(None, max_digits=14, decimal_places=4)
    id_impuesto_documento_venta_linea: Optional[int] = None
    porcentaje_impuesto_documento_venta_linea: Optional[Decimal] = Field(None, max_digits=5, decimal_places=2)
    total_linea_documento_venta_linea: Optional[Decimal] = Field(None, max_digits=14, decimal_places=2)

class DocumentoVentaLineaRead(DocumentoVentaLineaBase):
    id_documento_venta_linea: int
