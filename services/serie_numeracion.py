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

    def assign_next_number(self, serie_id) -> str:
        serie = self.get_or_404(serie_id)
        if not serie.habilitada:
            raise ConflictError("La serie de numeración está deshabilitada")
        numero_int = serie.proximo_consecutivo
        serie.proximo_consecutivo = numero_int + 1
        self.session.flush()
        return f"{serie.prefijo}{numero_int}"
