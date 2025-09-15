
from fastapi import APIRouter, Query, HTTPException
from .deps import SessionDep
from schemas import SerieNumeracionCreate, SerieNumeracionUpdate, SerieNumeracionRead
from services import SerieNumeracionService
from models import SerieNumeracion

router = APIRouter()

@router.get("", response_model=list[SerieNumeracionRead])
def listar_series(id_empresa: int = Query(...), session: SessionDep = None):
    svc = SerieNumeracionService(session)
    res = svc.list_by_empresa(id_empresa)
    return [SerieNumeracionRead.model_validate(i) for i in res.items]


@router.post("", response_model=SerieNumeracionRead, status_code=201)
def crear_serie(payload: SerieNumeracionCreate, session: SessionDep):
    obj = SerieNumeracion(**payload.model_dump(exclude_unset=True))
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return SerieNumeracionRead.model_validate(obj)


@router.get("/{id}", response_model=SerieNumeracionRead)
def obtener_serie(id: int, id_empresa: int = Query(...), session: SessionDep = None):
    svc = SerieNumeracionService(session)
    obj = svc.get_or_404(id)
    if obj.id_empresa_serie_numeracion != id_empresa:
        raise HTTPException(status_code=404, detail="Serie no pertenece a la empresa")
    return SerieNumeracionRead.model_validate(obj)


@router.patch("/{id}", response_model=SerieNumeracionRead)
def actualizar_serie(id: int, id_empresa: int = Query(...), payload: SerieNumeracionUpdate = None, session: SessionDep = None):
    svc = SerieNumeracionService(session)
    obj = svc.get_or_404(id)
    if obj.id_empresa_serie_numeracion != id_empresa:
        raise HTTPException(status_code=404, detail="Serie no pertenece a la empresa")
    for k, v in payload.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    session.commit()
    session.refresh(obj)
    return SerieNumeracionRead.model_validate(obj)
