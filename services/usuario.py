from __future__ import annotations

from typing import Optional
from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Usuario
from schemas import UsuarioCreate, UsuarioUpdate
from .base import CRUDService
from .security import hash_password

class UsuarioService(CRUDService[Usuario, UsuarioCreate, UsuarioUpdate]):
    model = Usuario

    def create(self, obj_in: UsuarioCreate) -> Usuario:
        payload = obj_in.model_dump(exclude={"password"}, exclude_unset=True)
        payload["password_hash"] = hash_password(obj_in.password)
        obj = self.model(**payload)
        self.session.add(obj)
        self.session.flush()
        return obj

    def set_password(self, user_id: UUID, new_password: str) -> Usuario:
        user = self.get(user_id)
        user.password_hash = hash_password(new_password)
        self.session.flush()
        return user

    def get_by_email(self, email: str) -> Optional[Usuario]:
        stmt = select(self.model).where(self.model.email == email)
        return self.session.execute(stmt).scalar_one_or_none()
