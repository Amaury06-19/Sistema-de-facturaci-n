from uuid import UUID
from fastapi import APIRouter, Query
from .deps import SessionDep, get_pagination
from schemas import GastoCreate, GastoUpdate, GastoRead, GastoAdjuntoCreate, GastoAdjuntoRead
from services import GastoService, GastoAdjuntoService
from models import Gasto

router = APIRouter()

@router.get("", response_model=dict)
def listar_gastos(empresa_id: UUID = Query(...), session: SessionDep = None, pagination: get_pagination = get_pagination):
    svc = GastoService(session)
    from sqlalchemy import select
    stmt = select(Gasto).where(Gasto.empresa_id == empresa_id).offset(pagination.skip).limit(pagination.limit)
    items = list(session.execute(stmt).scalars().all())
    total = len(items)
    return {"items": [GastoRead.model_validate(i) for i in items], "total": total, "skip": pagination.skip, "limit": pagination.limit}

@router.post("", response_model=GastoRead, status_code=201)
def crear_gasto(payload: GastoCreate, session: SessionDep):
    svc = GastoService(session)
    obj = svc.create(payload)
    session.commit()
    session.refresh(obj)
    return GastoRead.model_validate(obj)

@router.get("/{id}", response_model=GastoRead)
def obtener_gasto(id: UUID, session: SessionDep):
    svc = GastoService(session)
    obj = svc.get(id)
    return GastoRead.model_validate(obj)

@router.patch("/{id}", response_model=GastoRead)
def actualizar_gasto(id: UUID, payload: GastoUpdate, session: SessionDep):
    svc = GastoService(session)
    obj = svc.get(id)
    obj = svc.update(obj, payload)
    session.commit()
    session.refresh(obj)
    return GastoRead.model_validate(obj)

@router.delete("/{id}", status_code=204)
def eliminar_gasto(id: UUID, session: SessionDep):
    svc = GastoService(session)
    obj = svc.get(id)
    svc.delete(obj)
    session.commit()

@router.post("/{id}/adjuntos", response_model=GastoAdjuntoRead, status_code=201)
def agregar_adjunto(id: UUID, payload: GastoAdjuntoCreate, session: SessionDep):
    if payload.gasto_id != id:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="gasto_id en payload no coincide con la ruta")
    svc = GastoAdjuntoService(session)
    adj = svc.add(payload)
    session.commit()
    session.refresh(adj)
    return GastoAdjuntoRead.model_validate(adj)

@router.delete("/adjuntos/{adjunto_id}", status_code=204)
def eliminar_adjunto(adjunto_id: UUID, session: SessionDep):
    svc = GastoAdjuntoService(session)
    svc.delete(adjunto_id)
    session.commit()
