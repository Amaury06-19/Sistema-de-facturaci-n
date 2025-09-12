from __future__ import annotations

from sqlalchemy.orm import Session
from sqlalchemy import and_
from models import Tercero
from schemas import TerceroCreate, TerceroUpdate
from .base import CRUDService, Pagination, ListResult

class TerceroService(CRUDService[Tercero, TerceroCreate, TerceroUpdate]):
    model = Tercero

    def list_by_empresa(self, empresa_id, tipo: str | None = None, *, pagination: Pagination = Pagination()) -> ListResult[Tercero]:
        conds = [Tercero.empresa_id == empresa_id]
        if tipo:
            conds.append(Tercero.tipo == tipo)
        return self.list(pagination=pagination, where=conds, order_by=[Tercero.nombre.asc()])
