from __future__ import annotations

from models import CategoriaGasto
from schemas import CategoriaGastoCreate, CategoriaGastoUpdate
from .base import CRUDService

class CategoriaGastoService(CRUDService[CategoriaGasto, CategoriaGastoCreate, CategoriaGastoUpdate]):
    model = CategoriaGasto
