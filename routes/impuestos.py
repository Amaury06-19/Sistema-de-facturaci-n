from uuid import UUID
from fastapi import APIRouter, Query
from .deps import SessionDep, get_pagination
from schemas import ImpuestoCreate, ImpuestoUpdate, ImpuestoRead
from services import ImpuestoService

router = APIRouter()

@router.get("", response_model=dict)
def listar_impuestos(session: SessionDep, empresa_id: UUID = Query(...), pagination: get_pagination = get_pagination):
    svc = ImpuestoService(session)
    res = svc.list_by_empresa(empresa_id, pagination=pagination)
    return {"items": [ImpuestoRead.model_validate(i) for i in res.items], "total": res.total, "skip": res.skip, "limit": res.limit}

@router.post("", response_model=ImpuestoRead, status_code=201)
def crear_impuesto(payload: ImpuestoCreate, session: SessionDep):
    svc = ImpuestoService(session)
    obj = svc.create(payload)
    session.commit()
    return ImpuestoRead.model_validate(obj)

@router.get("/{id}", response_model=ImpuestoRead)
def obtener_impuesto(id: UUID, session: SessionDep):
    svc = ImpuestoService(session)
    obj = svc.get(id)
    return ImpuestoRead.model_validate(obj)

@router.patch("/{id}", response_model=ImpuestoRead)
def actualizar_impuesto(id: UUID, payload: ImpuestoUpdate, session: SessionDep):
    svc = ImpuestoService(session)
    obj = svc.get(id)
    obj = svc.update(obj, payload)
    session.commit()
    return ImpuestoRead.model_validate(obj)

@router.delete("/{id}", status_code=204)
def eliminar_impuesto(id: UUID, session: SessionDep):
    svc = ImpuestoService(session)
    obj = svc.get(id)
    svc.delete(obj)
    session.commit()
