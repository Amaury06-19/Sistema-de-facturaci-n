from uuid import UUID
from fastapi import APIRouter, Query
from .deps import SessionDep, get_pagination
from schemas import (
    DocumentoVentaCreate, DocumentoVentaUpdate, DocumentoVentaRead,
    DocumentoVentaLineaCreate, DocumentoVentaLineaUpdate, DocumentoVentaLineaRead,
    PagoCreate, PagoRead
)
from services import DocumentoVentaService

router = APIRouter()

@router.get("", response_model=dict)
def listar_documentos(empresa_id: UUID | None = Query(None), session: SessionDep = None, pagination: get_pagination = get_pagination):
    svc = DocumentoVentaService(session)
    where = []
    if empresa_id:
        from models import DocumentoVenta
        where.append(DocumentoVenta.empresa_id == empresa_id)
    res = svc.list(pagination=pagination, where=where or None)
    return {"items": [DocumentoVentaRead.model_validate(i) for i in res.items], "total": res.total, "skip": res.skip, "limit": res.limit}

@router.post("", response_model=DocumentoVentaRead, status_code=201)
def crear_documento(payload: DocumentoVentaCreate, session: SessionDep):
    svc = DocumentoVentaService(session)
    obj = svc.create(payload)
    session.commit()
    session.refresh(obj)
    return DocumentoVentaRead.model_validate(obj)

@router.get("/{id}", response_model=DocumentoVentaRead)
def obtener_documento(id: UUID, session: SessionDep):
    svc = DocumentoVentaService(session)
    obj = svc.get(id)
    return DocumentoVentaRead.model_validate(obj)

@router.patch("/{id}", response_model=DocumentoVentaRead)
def actualizar_documento(id: UUID, payload: DocumentoVentaUpdate, session: SessionDep):
    svc = DocumentoVentaService(session)
    obj = svc.get(id)
    obj = svc.update(obj, payload)
    session.commit()
    session.refresh(obj)
    return DocumentoVentaRead.model_validate(obj)

@router.post("/{id}/confirmar", response_model=DocumentoVentaRead)
def confirmar_y_asignar_numero(id: UUID, session: SessionDep):
    svc = DocumentoVentaService(session)
    obj = svc.confirm_and_assign_number(id)
    session.commit()
    session.refresh(obj)
    return DocumentoVentaRead.model_validate(obj)

@router.post("/{id}/lineas", response_model=DocumentoVentaLineaRead, status_code=201)
def agregar_linea(id: UUID, payload: DocumentoVentaLineaCreate, session: SessionDep):
    svc = DocumentoVentaService(session)
    linea = svc.add_line(id, payload)
    session.commit()
    session.refresh(linea)
    return DocumentoVentaLineaRead.model_validate(linea)

@router.patch("/lineas/{linea_id}", response_model=DocumentoVentaLineaRead)
def actualizar_linea(linea_id: UUID, payload: DocumentoVentaLineaUpdate, session: SessionDep):
    svc = DocumentoVentaService(session)
    linea = svc.update_line(linea_id, payload)
    session.commit()
    session.refresh(linea)
    return DocumentoVentaLineaRead.model_validate(linea)

@router.delete("/lineas/{linea_id}", status_code=204)
def eliminar_linea(linea_id: UUID, session: SessionDep):
    svc = DocumentoVentaService(session)
    svc.delete_line(linea_id)
    session.commit()

@router.post("/{id}/pagos", response_model=PagoRead, status_code=201)
def registrar_pago(id: UUID, payload: PagoCreate, session: SessionDep):
    if payload.documento_id != id:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="documento_id en payload no coincide con la ruta")
    svc = DocumentoVentaService(session)
    pago = svc.register_payment(payload)
    session.commit()
    session.refresh(pago)
    return PagoRead.model_validate(pago)
