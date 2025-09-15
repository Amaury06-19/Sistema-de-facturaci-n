
from fastapi import APIRouter, Query, HTTPException
from .deps import SessionDep
from schemas import (
    DocumentoVentaCreate, DocumentoVentaUpdate, DocumentoVentaRead,
    DocumentoVentaLineaCreate, DocumentoVentaLineaUpdate, DocumentoVentaLineaRead,
    PagoCreate, PagoRead
)
from services import DocumentoVentaService

router = APIRouter()

@router.get("", response_model=list[DocumentoVentaRead])
def listar_documentos(id_empresa: int = Query(...), session: SessionDep = None):
    svc = DocumentoVentaService(session)
    res = svc.list_by_empresa(id_empresa)
    return [DocumentoVentaRead.model_validate(i) for i in res.items]


@router.post("", response_model=DocumentoVentaRead, status_code=201)
def crear_documento(payload: DocumentoVentaCreate, session: SessionDep):
    svc = DocumentoVentaService(session)
    obj = svc.create(payload)
    session.commit()
    session.refresh(obj)
    return DocumentoVentaRead.model_validate(obj)


@router.get("/{id}", response_model=DocumentoVentaRead)
def obtener_documento(id: int, id_empresa: int = Query(...), session: SessionDep = None):
    svc = DocumentoVentaService(session)
    obj = svc.get(id)
    if obj.id_empresa_documento_venta != id_empresa:
        raise HTTPException(status_code=404, detail="Documento no pertenece a la empresa")
    return DocumentoVentaRead.model_validate(obj)


@router.patch("/{id}", response_model=DocumentoVentaRead)
def actualizar_documento(id: int, id_empresa: int = Query(...), payload: DocumentoVentaUpdate = None, session: SessionDep = None):
    svc = DocumentoVentaService(session)
    obj = svc.get(id)
    if obj.id_empresa_documento_venta != id_empresa:
        raise HTTPException(status_code=404, detail="Documento no pertenece a la empresa")
    obj = svc.update(obj, payload)
    session.commit()
    session.refresh(obj)
    return DocumentoVentaRead.model_validate(obj)


@router.post("/{id}/confirmar", response_model=DocumentoVentaRead)
def confirmar_y_asignar_numero(id: int, id_empresa: int = Query(...), session: SessionDep = None):
    svc = DocumentoVentaService(session)
    obj = svc.get(id)
    if obj.id_empresa_documento_venta != id_empresa:
        raise HTTPException(status_code=404, detail="Documento no pertenece a la empresa")
    obj = svc.confirm_and_assign_number(id)
    session.commit()
    session.refresh(obj)
    return DocumentoVentaRead.model_validate(obj)

@router.post("/{id}/lineas", response_model=DocumentoVentaLineaRead, status_code=201)
def agregar_linea(id: int, payload: DocumentoVentaLineaCreate, session: SessionDep):
    svc = DocumentoVentaService(session)
    linea = svc.add_line(id, payload)
    session.commit()
    session.refresh(linea)
    return DocumentoVentaLineaRead.model_validate(linea)

@router.patch("/lineas/{linea_id}", response_model=DocumentoVentaLineaRead)
def actualizar_linea(linea_id: int, payload: DocumentoVentaLineaUpdate, session: SessionDep):
    svc = DocumentoVentaService(session)
    linea = svc.update_line(linea_id, payload)
    session.commit()
    session.refresh(linea)
    return DocumentoVentaLineaRead.model_validate(linea)

@router.delete("/lineas/{linea_id}", status_code=204)
def eliminar_linea(linea_id: int, session: SessionDep):
    svc = DocumentoVentaService(session)
    svc.delete_line(linea_id)
    session.commit()

@router.post("/{id}/pagos", response_model=PagoRead, status_code=201)
def registrar_pago(id: int, payload: PagoCreate, session: SessionDep):
    if payload.documento_id != id:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="documento_id en payload no coincide con la ruta")
    svc = DocumentoVentaService(session)
    pago = svc.register_payment(payload)
    session.commit()
    session.refresh(pago)
    return PagoRead.model_validate(pago)
