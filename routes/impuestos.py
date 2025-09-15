from uuid import UUID
from fastapi import APIRouter, Query
from .deps import SessionDep, get_pagination
from schemas import ImpuestoCreate, ImpuestoUpdate, ImpuestoRead
from services import ImpuestoService

router = APIRouter()

from fastapi import HTTPException

@router.get("", response_model=list[ImpuestoRead])
def listar_impuestos(session: SessionDep, id_empresa: int = Query(...)):
    svc = ImpuestoService(session)
    res = svc.list_by_empresa(id_empresa)
    return [ImpuestoRead.model_validate(i) for i in res.items]

@router.post("", response_model=ImpuestoRead, status_code=201)
def crear_impuesto(payload: ImpuestoCreate, session: SessionDep):
    svc = ImpuestoService(session)
    obj = svc.create(payload)
    session.commit()
    return ImpuestoRead.model_validate(obj)

@router.get("/{id}", response_model=ImpuestoRead)
def obtener_impuesto(id: int, id_empresa: int = Query(...), session: SessionDep = None):
    svc = ImpuestoService(session)
    obj = svc.get(id)
    if obj.id_empresa_impuesto != id_empresa:
        raise HTTPException(status_code=404, detail="Impuesto no pertenece a la empresa")
    return ImpuestoRead.model_validate(obj)


@router.patch("/{id}", response_model=ImpuestoRead)
def actualizar_impuesto(id: int, id_empresa: int = Query(...), payload: ImpuestoUpdate = None, session: SessionDep = None):
    svc = ImpuestoService(session)
    obj = svc.get(id)
    if obj.id_empresa_impuesto != id_empresa:
        raise HTTPException(status_code=404, detail="Impuesto no pertenece a la empresa")
    obj = svc.update(obj, payload)
    session.commit()
    return ImpuestoRead.model_validate(obj)


@router.delete("/{id}", status_code=204)
def eliminar_impuesto(id: int, id_empresa: int = Query(...), session: SessionDep = None):
    svc = ImpuestoService(session)
    obj = svc.get(id)
    if obj.id_empresa_impuesto != id_empresa:
        raise HTTPException(status_code=404, detail="Impuesto no pertenece a la empresa")
    svc.delete(obj)
    session.commit()
