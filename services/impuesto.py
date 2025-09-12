from __future__ import annotations

from sqlalchemy.orm import Session
from sqlalchemy import and_
from models import Impuesto
from schemas import ImpuestoCreate, ImpuestoUpdate
from .base import CRUDService, Pagination, ListResult

class ImpuestoService(CRUDService[Impuesto, ImpuestoCreate, ImpuestoUpdate]):
    model = Impuesto

    def list_by_empresa(self, empresa_id, *, pagination: Pagination = Pagination()) -> ListResult[Impuesto]:
        where = [Impuesto.empresa_id == empresa_id]
        return self.list(pagination=pagination, where=where, order_by=[Impuesto.nombre.asc()])
