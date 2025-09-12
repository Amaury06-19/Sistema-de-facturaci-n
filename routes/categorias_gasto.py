from uuid import UUID
from fastapi import APIRouter, Query
from .deps import SessionDep, get_pagination
from schemas import CategoriaGastoCreate, CategoriaGastoUpdate, CategoriaGastoRead
from services import CategoriaGastoService
from models import CategoriaGasto

router = APIRouter()

@router.get("", response_model=dict)
def listar_categorias(empresa_id: UUID = Query(...), session: SessionDep = None, pagination: get_pagination = get_pagination):
    svc = CategoriaGastoService(session)
    from sqlalchemy import select
    stmt = select(CategoriaGasto).where(CategoriaGasto.empresa_id == empresa_id).offset(pagination.skip).limit(pagination.limit)
    items = list(session.execute(stmt).scalars().all())
    total = len(items)
    return {"items": [CategoriaGastoRead.model_validate(i) for i in items], "total": total, "skip": pagination.skip, "limit": pagination.limit}

@router.post("", response_model=CategoriaGastoRead, status_code=201)
def crear_categoria(payload: CategoriaGastoCreate, session: SessionDep):
    svc = CategoriaGastoService(session)
    obj = svc.create(payload)
    session.commit()
    return CategoriaGastoRead.model_validate(obj)

@router.patch("/{id}", response_model=CategoriaGastoRead)
def actualizar_categoria(id: UUID, payload: CategoriaGastoUpdate, session: SessionDep):
    svc = CategoriaGastoService(session)
    obj = svc.get(id)
    obj = svc.update(obj, payload)
    session.commit()
    return CategoriaGastoRead.model_validate(obj)

@router.delete("/{id}", status_code=204)
def eliminar_categoria(id: UUID, session: SessionDep):
    svc = CategoriaGastoService(session)
    obj = svc.get(id)
    svc.delete(obj)
    session.commit()
