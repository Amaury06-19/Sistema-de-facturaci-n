from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Generic, Iterable, Sequence, TypeVar
from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import select

from models.base import Base
from .exceptions import NotFoundError, ConflictError

ModelT = TypeVar("ModelT", bound=Base)
CreateT = TypeVar("CreateT")
UpdateT = TypeVar("UpdateT")

@dataclass
class Pagination:
    skip: int = 0
    limit: int = 50

@dataclass
class ListResult(Generic[ModelT]):
    items: list[ModelT]
    total: int
    skip: int
    limit: int

class CRUDService(Generic[ModelT, CreateT, UpdateT]):
    model: type[ModelT]

    def __init__(self, session: Session):
        self.session = session

    def _apply_updates(self, db_obj: ModelT, data: dict[str, Any]) -> ModelT:
        for k, v in data.items():
            if v is not None:
                setattr(db_obj, k, v)
        return db_obj


    def get(self, id_: UUID) -> ModelT:
        pk_attr = getattr(self.model, 'id', None)
        if pk_attr is None:
            # Buscar el primer atributo que sea primary_key=True
            for c in self.model.__table__.columns:
                if c.primary_key:
                    pk_attr = getattr(self.model, c.name)
                    break
        obj = self.session.query(self.model).filter(pk_attr == id_).first()
        if not obj:
            raise NotFoundError(self.model.__name__, str(id_))
        return obj

    def list(
        self,
        *,
        pagination: Pagination = Pagination(),
        where: Iterable[Any] | None = None,
        order_by: Sequence[Any] | None = None,
    ) -> ListResult[ModelT]:
        stmt = select(self.model)
        if where:
            for cond in where:
                stmt = stmt.where(cond)
        # Detectar el nombre de la columna PK
        pk_attr = getattr(self.model, 'id', None)
        if pk_attr is None:
            for c in self.model.__table__.columns:
                if c.primary_key:
                    pk_attr = getattr(self.model, c.name)
                    break
        count_stmt = select(pk_attr).select_from(self.model)
        if where:
            for cond in where:
                count_stmt = count_stmt.where(cond)
        total = self.session.execute(count_stmt).unique().scalar() if pk_attr is not None else 0
        if order_by:
            stmt = stmt.order_by(*order_by)
        stmt = stmt.offset(pagination.skip).limit(pagination.limit)
        items = self.session.execute(stmt).scalars().all()
        return ListResult(
            items=items,
            total=total,
            skip=pagination.skip,
            limit=pagination.limit,
        )

    def create(self, obj_in: CreateT) -> ModelT:
        payload = obj_in.model_dump(exclude_unset=True)
        obj = self.model(**payload)  # type: ignore[arg-type]
        self.session.add(obj)
        try:
            self.session.flush()
        except IntegrityError as e:
            self.session.rollback()
            raise ConflictError(str(e.orig)) from e
        return obj

    def update(self, db_obj: ModelT, obj_in: UpdateT | dict[str, Any]) -> ModelT:
        data = obj_in if isinstance(obj_in, dict) else obj_in.model_dump(exclude_unset=True)
        self._apply_updates(db_obj, data)
        try:
            self.session.flush()
        except IntegrityError as e:
            self.session.rollback()
            raise ConflictError(str(e.orig)) from e
        return db_obj

    def delete(self, db_obj: ModelT) -> None:
        self.session.delete(db_obj)
        try:
            self.session.flush()
        except IntegrityError as e:
            self.session.rollback()
            raise ConflictError(str(e.orig)) from e
