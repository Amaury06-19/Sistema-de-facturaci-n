from __future__ import annotations

from typing import Generator
from sqlalchemy.orm import sessionmaker, Session
from .engine import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    future=True,
)


def get_session() -> Generator[Session, None, None]:
    session: Session = SessionLocal()
    try:
        yield session
        # El commit lo manejan explícitamente los endpoints/servicios
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
