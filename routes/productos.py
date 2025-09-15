from fastapi import APIRouter, Query, HTTPException
from .deps import SessionDep, get_pagination
from schemas import ProductoCreate, ProductoUpdate, ProductoRead
from services import ProductoService

router = APIRouter()

@router.get("", response_model=list[ProductoRead])
def listar_productos(id_empresa: int = Query(...), session: SessionDep = None):
    svc = ProductoService(session)
    res = svc.list_by_empresa(id_empresa)
    return [ProductoRead.model_validate(i) for i in res.items]

@router.post("", response_model=ProductoRead, status_code=201)
def crear_producto(payload: ProductoCreate, session: SessionDep):
    svc = ProductoService(session)
    obj = svc.create(payload)
    session.commit()
    return ProductoRead.model_validate(obj)

@router.get("/{id}", response_model=ProductoRead)
def obtener_producto(id: int, id_empresa: int = Query(...), session: SessionDep = None):
    svc = ProductoService(session)
    obj = svc.get(id)
    if obj.id_empresa_producto != id_empresa:
        raise HTTPException(status_code=404, detail="Producto no pertenece a la empresa")
    return ProductoRead.model_validate(obj)

@router.patch("/{id}", response_model=ProductoRead)
def actualizar_producto(id: int, id_empresa: int = Query(...), payload: ProductoUpdate = None, session: SessionDep = None):
    svc = ProductoService(session)
    obj = svc.get(id)
    if obj.id_empresa_producto != id_empresa:
        raise HTTPException(status_code=404, detail="Producto no pertenece a la empresa")
    obj = svc.update(obj, payload)
    session.commit()
    return ProductoRead.model_validate(obj)

@router.delete("/{id}", status_code=204)
def eliminar_producto(id: int, id_empresa: int = Query(...), session: SessionDep = None):
    svc = ProductoService(session)
    obj = svc.get(id)
    if obj.id_empresa_producto != id_empresa:
        raise HTTPException(status_code=404, detail="Producto no pertenece a la empresa")
    svc.delete(obj)
    session.commit()
