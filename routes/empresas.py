from fastapi import APIRouter
from .deps import SessionDep, get_pagination
from schemas import EmpresaCreate, EmpresaUpdate, EmpresaRead
from services import EmpresaService

router = APIRouter()

@router.get("", response_model=dict)
def listar_empresas(session: SessionDep):
    svc = EmpresaService(session)
    empresas = session.query(svc.model).all()
    return {"items": [EmpresaRead.model_validate(i) for i in empresas]}

@router.post("", response_model=EmpresaRead, status_code=201)
def crear_empresa(payload: EmpresaCreate, session: SessionDep):
    svc = EmpresaService(session)
    obj = svc.create(payload)
    session.commit()
    return EmpresaRead.model_validate(obj)

@router.get("/{id}", response_model=EmpresaRead)
def obtener_empresa(id: int, session: SessionDep):
    svc = EmpresaService(session)
    obj = svc.get(id)
    return EmpresaRead.model_validate(obj)

@router.patch("/{id}", response_model=EmpresaRead)
def actualizar_empresa(id: int, payload: EmpresaUpdate, session: SessionDep):
    svc = EmpresaService(session)
    obj = svc.get(id)
    obj = svc.update(obj, payload)
    session.commit()
    return EmpresaRead.model_validate(obj)

@router.delete("/{id}", status_code=204)
def eliminar_empresa(id: int, session: SessionDep):
    svc = EmpresaService(session)
    obj = svc.get(id)
    svc.delete_with_children(obj)
