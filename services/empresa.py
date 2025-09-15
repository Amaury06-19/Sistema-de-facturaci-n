from __future__ import annotations

from sqlalchemy.orm import Session
from models import Empresa
from schemas import EmpresaCreate, EmpresaUpdate
from .base import CRUDService

class EmpresaService(CRUDService[Empresa, EmpresaCreate, EmpresaUpdate]):
    model = Empresa

    def delete_with_children(self, empresa_obj):
        # Eliminar hijos relacionados
        for producto in list(empresa_obj.productos):
            self.session.delete(producto)
        for impuesto in list(empresa_obj.impuestos):
            self.session.delete(impuesto)
        for tercero in list(empresa_obj.terceros):
            self.session.delete(tercero)
        for gasto in list(empresa_obj.gastos):
            self.session.delete(gasto)
        for categoria in list(empresa_obj.categorias_gasto):
            self.session.delete(categoria)
        for doc in list(empresa_obj.documentos_venta):
            self.session.delete(doc)
        for serie in list(empresa_obj.series):
            self.session.delete(serie)
        for log in list(empresa_obj.auditorias):
            self.session.delete(log)
        self.session.delete(empresa_obj)
        self.session.commit()
