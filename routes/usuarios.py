 
from fastapi import APIRouter
from .deps import SessionDep, get_pagination
from fastapi import Depends
from services.base import Pagination
from schemas import UsuarioCreate, UsuarioUpdate, UsuarioRead
from services import UsuarioService

router = APIRouter()

@router.get("", response_model=dict)
def listar_usuarios(session: SessionDep, pagination: Pagination = Depends(get_pagination)):
    svc = UsuarioService(session)
    res = svc.list(pagination=pagination)
    return {"items": [UsuarioRead.model_validate(i) for i in res.items], "total": res.total, "skip": res.skip, "limit": res.limit}

@router.post("", response_model=UsuarioRead, status_code=201)
def crear_usuario(payload: UsuarioCreate, session: SessionDep):
    svc = UsuarioService(session)
    obj = svc.create(payload)
    session.commit()
    return UsuarioRead.model_validate(obj)

@router.get("/{id}", response_model=UsuarioRead)
def obtener_usuario(id: int, session: SessionDep):
    svc = UsuarioService(session)
    obj = svc.get(id)
    return UsuarioRead.model_validate(obj)

@router.patch("/{id}", response_model=UsuarioRead)
def actualizar_usuario(id: int, payload: UsuarioUpdate, session: SessionDep):
    svc = UsuarioService(session)
    obj = svc.get(id)
    obj = svc.update(obj, payload)
    session.commit()
    return UsuarioRead.model_validate(obj)

@router.delete("/{id}", status_code=204)
def eliminar_usuario(id: int, session: SessionDep):
    svc = UsuarioService(session)
    obj = svc.get(id)
    svc.delete(obj)
    session.commit()
