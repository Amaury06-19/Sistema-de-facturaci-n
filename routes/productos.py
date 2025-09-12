from uuid import UUID
from fastapi import APIRouter, Query
from .deps import SessionDep, get_pagination
from schemas import ProductoCreate, ProductoUpdate, ProductoRead
from services import ProductoService

router = APIRouter()

@router.get("", response_model=dict)
def listar_productos(empresa_id: UUID = Query(...), q: str | None = Query(None), session: SessionDep = None, pagination: get_pagination = get_pagination):
    svc = ProductoService(session)
    res = svc.list_by_empresa(empresa_id, q=q, pagination=pagination)
    return {"items": [ProductoRead.model_validate(i) for i in res.items], "total": res.total, "skip": res.skip, "limit": res.limit}

@router.post("", response_model=ProductoRead, status_code=201)
def crear_producto(payload: ProductoCreate, session: SessionDep):
    svc = ProductoService(session)
    obj = svc.create(payload)
    session.commit()
    return ProductoRead.model_validate(obj)

@router.get("/{id}", response_model=ProductoRead)
def obtener_producto(id: UUID, session: SessionDep):
    svc = ProductoService(session)
    obj = svc.get(id)
    return ProductoRead.model_validate(obj)

@router.patch("/{id}", response_model=ProductoRead)
def actualizar_producto(id: UUID, payload: ProductoUpdate, session: SessionDep):
    svc = ProductoService(session)
    obj = svc.get(id)
    obj = svc.update(obj, payload)
    session.commit()
    return ProductoRead.model_validate(obj)

@router.delete("/{id}", status_code=204)
def eliminar_producto(id: UUID, session: SessionDep):
    svc = ProductoService(session)
    obj = svc.get(id)
    svc.delete(obj)
    session.commit()
