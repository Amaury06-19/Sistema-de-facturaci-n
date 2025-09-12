from __future__ import annotations

from sqlalchemy.orm import Session
from models import Empresa
from schemas import EmpresaCreate, EmpresaUpdate
from .base import CRUDService

class EmpresaService(CRUDService[Empresa, EmpresaCreate, EmpresaUpdate]):
    model = Empresa
