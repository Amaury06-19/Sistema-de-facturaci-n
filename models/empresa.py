from __future__ import annotations

from typing import List, Optional
from sqlalchemy import String, UniqueConstraint, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from models.categoria_gasto import CategoriaGasto
from models.documento_venta import DocumentoVenta
from models.gasto import Gasto
from models.impuesto import Impuesto
from models.log_auditoria import LogAuditoria
from models.producto import Producto
from models.serie_numeracion import SerieNumeracion
from models.tercero import Tercero
from models.usuario_empresa import UsuarioEmpresa
from .base import Base, TimestampMixin, uuid_pk



class Empresa(Base):
    __tablename__ = "empresa"
    id_empresa: Mapped[int] = mapped_column("id_empresa", primary_key=True, autoincrement=True)
    nombre_empresa: Mapped[str] = mapped_column("nombre_empresa", String(200), nullable=False)
    nit_empresa: Mapped[str] = mapped_column("nit_empresa", String(50), unique=True)
    email_empresa: Mapped[Optional[str]] = mapped_column("email_empresa", String(150))
    telefono_empresa: Mapped[Optional[str]] = mapped_column("telefono_empresa", String(50))
    direccion_empresa: Mapped[Optional[str]] = mapped_column("direccion_empresa", String)
    moneda_empresa: Mapped[str] = mapped_column("moneda_empresa", String(10))
    created_at_empresa: Mapped[Optional[str]] = mapped_column("created_at_empresa", DateTime)
    created_by_id_usuario_empresa: Mapped[Optional[int]] = mapped_column("created_by_id_usuario_empresa", Integer)
    updated_at_empresa: Mapped[Optional[str]] = mapped_column("updated_at_empresa", DateTime)
    updated_by_id_usuario_empresa: Mapped[Optional[int]] = mapped_column("updated_by_id_usuario_empresa", Integer)
    deleted_at_empresa: Mapped[Optional[str]] = mapped_column("deleted_at_empresa", DateTime)

    gastos: Mapped[List["Gasto"]] = relationship("Gasto", back_populates="empresa")
    categorias_gasto: Mapped[List["CategoriaGasto"]] = relationship("CategoriaGasto", back_populates="empresa")
    documentos_venta: Mapped[List["DocumentoVenta"]] = relationship("DocumentoVenta", back_populates="empresa")
    productos: Mapped[List["Producto"]] = relationship("Producto", back_populates="empresa")
    impuestos: Mapped[List["Impuesto"]] = relationship("Impuesto", back_populates="empresa")
    series: Mapped[List["SerieNumeracion"]] = relationship("SerieNumeracion", back_populates="empresa")
    auditorias: Mapped[List["LogAuditoria"]] = relationship("LogAuditoria", back_populates="empresa")
    terceros: Mapped[List["Tercero"]] = relationship("Tercero", back_populates="empresa")
