from typing import Annotated
from fastapi import Depends, Query
from sqlalchemy.orm import Session
from services.base import Pagination
from database.session import get_session

SessionDep = Annotated[Session, Depends(get_session)]

def get_pagination(
    skip: int = Query(0, ge=0, description="Offset de la consulta"),
    limit: int = Query(50, ge=1, le=200, description="Límite de filas"),
) -> Pagination:
    return Pagination(skip=skip, limit=limit)
