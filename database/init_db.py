from __future__ import annotations

from .engine import engine
from ..models import Base


def create_all() -> None:
    Base.metadata.create_all(bind=engine)


def drop_all() -> None:
    Base.metadata.drop_all(bind=engine)


if __name__ == "__main__":
    create_all()
    print("Tablas creadas.")
