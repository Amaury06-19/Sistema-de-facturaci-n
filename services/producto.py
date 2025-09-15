from __future__ import annotations

from sqlalchemy.orm import Session
from sqlalchemy import and_
from models import Producto
from schemas import ProductoCreate, ProductoUpdate
from .base import CRUDService, Pagination, ListResult


from datetime import datetime

class ProductoService(CRUDService[Producto, ProductoCreate, ProductoUpdate]):
    model = Producto

    def create(self, obj_in: ProductoCreate) -> Producto:
        payload = obj_in.model_dump(exclude_unset=True)
        # Si id_impuesto_producto es 0 o falsy, ponerlo en None
        if not payload.get("id_impuesto_producto"):
            payload["id_impuesto_producto"] = None
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        payload["created_at_producto"] = now
        payload["updated_at_producto"] = now
        obj = self.model(**payload)
        self.session.add(obj)
        try:
            self.session.flush()
        except Exception as e:
            self.session.rollback()
            raise
        return obj

    def list_by_empresa(self, empresa_id, *, q: str | None = None, pagination: Pagination = Pagination()) -> ListResult[Producto]:
        where = [Producto.id_empresa_producto == empresa_id]
        if q:
            from sqlalchemy import or_
            where.append(or_(Producto.codigo_producto.ilike(f"%{q}%"), Producto.nombre_producto.ilike(f"%{q}%")))
        return self.list(pagination=pagination, where=where, order_by=[Producto.nombre_producto.asc()])
