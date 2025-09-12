from __future__ import annotations

from sqlalchemy.orm import Session
from sqlalchemy import and_
from models import Producto
from schemas import ProductoCreate, ProductoUpdate
from .base import CRUDService, Pagination, ListResult

class ProductoService(CRUDService[Producto, ProductoCreate, ProductoUpdate]):
    model = Producto

    def list_by_empresa(self, empresa_id, *, q: str | None = None, pagination: Pagination = Pagination()) -> ListResult[Producto]:
        where = [Producto.empresa_id == empresa_id]
        if q:
            # Filtro simple por código o nombre
            from sqlalchemy import or_
            where.append(or_(Producto.codigo.ilike(f"%{q}%"), Producto.nombre.ilike(f"%{q}%")))
        return self.list(pagination=pagination, where=where, order_by=[Producto.nombre.asc()])
