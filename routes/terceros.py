from uuid import UUID
from fastapi import APIRouter, Query
from .deps import SessionDep, get_pagination
from schemas import TerceroCreate, TerceroUpdate, TerceroRead
from services import TerceroService

router = APIRouter()

@router.get("", response_model=dict)
def listar_terceros(empresa_id: UUID = Query(...), tipo: str | None = Query(None), session: SessionDep = None, pagination: get_pagination = get_pagination):
    svc = TerceroService(session)
    res = svc.list_by_empresa(empresa_id, tipo=tipo, pagination=pagination)
    return {"items": [TerceroRead.model_validate(i) for i in res.items], "total": res.total, "skip": res.skip, "limit": res.limit}

@router.post("", response_model=TerceroRead, status_code=201)
def crear_tercero(payload: TerceroCreate, session: SessionDep):
    svc = TerceroService(session)
    obj = svc.create(payload)
    session.commit()
    return TerceroRead.model_validate(obj)

@router.get("/{id}", response_model=TerceroRead)
def obtener_tercero(id: UUID, session: SessionDep):
    svc = TerceroService(session)
    obj = svc.get(id)
    return TerceroRead.model_validate(obj)

@router.patch("/{id}", response_model=TerceroRead)
def actualizar_tercero(id: UUID, payload: TerceroUpdate, session: SessionDep):
    svc = TerceroService(session)
    obj = svc.get(id)
    obj = svc.update(obj, payload)
    session.commit()
    return TerceroRead.model_validate(obj)

@router.delete("/{id}", status_code=204)
def eliminar_tercero(id: UUID, session: SessionDep):
    svc = TerceroService(session)
    obj = svc.get(id)
    svc.delete(obj)
    session.commit()
