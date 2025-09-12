from uuid import UUID
from fastapi import APIRouter
from .deps import SessionDep, get_pagination
from schemas import SerieNumeracionCreate, SerieNumeracionUpdate, SerieNumeracionRead
from services import SerieNumeracionService
from models import SerieNumeracion

router = APIRouter()

@router.get("", response_model=dict)
def listar_series(session: SessionDep, pagination: get_pagination = get_pagination):
    from sqlalchemy import select
    stmt = select(SerieNumeracion).offset(pagination.skip).limit(pagination.limit)
    items = list(session.execute(stmt).scalars().all())
    # Total “rápido”: si vas a usar mucho, mejor haz un COUNT separado
    total = len(items)
    return {"items": [SerieNumeracionRead.model_validate(i) for i in items], "total": total, "skip": pagination.skip, "limit": pagination.limit}

@router.post("", response_model=SerieNumeracionRead, status_code=201)
def crear_serie(payload: SerieNumeracionCreate, session: SessionDep):
    obj = SerieNumeracion(**payload.model_dump(exclude_unset=True))
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return SerieNumeracionRead.model_validate(obj)

@router.get("/{id}", response_model=SerieNumeracionRead)
def obtener_serie(id: UUID, session: SessionDep):
    svc = SerieNumeracionService(session)
    obj = svc.get_or_404(id)
    return SerieNumeracionRead.model_validate(obj)

@router.patch("/{id}", response_model=SerieNumeracionRead)
def actualizar_serie(id: UUID, payload: SerieNumeracionUpdate, session: SessionDep):
    svc = SerieNumeracionService(session)
    obj = svc.get_or_404(id)
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    session.commit()
    session.refresh(obj)
    return SerieNumeracionRead.model_validate(obj)
