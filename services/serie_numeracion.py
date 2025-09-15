from __future__ import annotations

from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from models import SerieNumeracion
from .exceptions import NotFoundError, ConflictError

class SerieNumeracionService:
    def __init__(self, session: Session):
        self.session = session

    def get_or_404(self, id_):
        obj = self.session.get(SerieNumeracion, id_)
        if not obj:
            raise NotFoundError("SerieNumeracion", str(id_))
        return obj

    def list_by_empresa(self, id_empresa: int):
        from .base import ListResult
        q = self.session.query(SerieNumeracion).filter(SerieNumeracion.id_empresa_serie == id_empresa)
        items = q.all()
        return ListResult(items=items, total=len(items), skip=0, limit=len(items))

    def assign_next_number(self, serie_id) -> str:
        serie = self.get_or_404(serie_id)
        if not serie.habilitada_serie:
            raise ConflictError("La serie de numeración está deshabilitada")
        numero_int = serie.proximo_consecutivo_serie
        serie.proximo_consecutivo_serie = numero_int + 1
        self.session.flush()
        return f"{serie.prefijo_serie}{numero_int}"
