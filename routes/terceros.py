from fastapi import APIRouter, Query, HTTPException
from .deps import SessionDep
from schemas import TerceroCreate, TerceroUpdate, TerceroRead
from services import TerceroService

router = APIRouter()

@router.get("", response_model=list[TerceroRead])
def listar_terceros(id_empresa: int = Query(...), tipo: str | None = Query(None), session: SessionDep = None):
    svc = TerceroService(session)
    res = svc.list_by_empresa(id_empresa, tipo=tipo)
    return [TerceroRead.model_validate(i) for i in res.items]

@router.post("", response_model=TerceroRead, status_code=201)
def crear_tercero(payload: TerceroCreate, session: SessionDep):
    svc = TerceroService(session)
    obj = svc.create(payload)
    session.commit()
    return TerceroRead.model_validate(obj)

@router.get("/{id}", response_model=TerceroRead)
def obtener_tercero(id: int, id_empresa: int = Query(...), session: SessionDep = None):
    svc = TerceroService(session)
    obj = svc.get(id)
    if obj.id_empresa_tercero != id_empresa:
        raise HTTPException(status_code=404, detail="Tercero no pertenece a la empresa")
    return TerceroRead.model_validate(obj)

@router.patch("/{id}", response_model=TerceroRead)
def actualizar_tercero(id: int, id_empresa: int = Query(...), payload: TerceroUpdate = None, session: SessionDep = None):
    svc = TerceroService(session)
    obj = svc.get(id)
    if obj.id_empresa_tercero != id_empresa:
        raise HTTPException(status_code=404, detail="Tercero no pertenece a la empresa")
    obj = svc.update(obj, payload)
    session.commit()
    return TerceroRead.model_validate(obj)

@router.delete("/{id}", status_code=204)
def eliminar_tercero(id: int, id_empresa: int = Query(...), session: SessionDep = None):
    svc = TerceroService(session)
    obj = svc.get(id)
    if obj.id_empresa_tercero != id_empresa:
        raise HTTPException(status_code=404, detail="Tercero no pertenece a la empresa")
    svc.delete(obj)
    session.commit()
