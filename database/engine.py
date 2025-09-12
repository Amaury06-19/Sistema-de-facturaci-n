from __future__ import annotations

from sqlalchemy import create_engine, text
from .settings import settings

_engine = None


def get_engine():
    global _engine
    if _engine is None:
        _engine = create_engine(
            settings.sqlalchemy_url(),
            pool_size=settings.DB_POOL_SIZE,
            max_overflow=settings.DB_MAX_OVERFLOW,
            pool_pre_ping=settings.DB_POOL_PRE_PING,
            echo=settings.DB_ECHO,
            future=True,
            fast_executemany=settings.DB_FAST_EXECUTEMANY,
        )
    return _engine


# alias conveniente
engine = get_engine()


def test_connection() -> bool:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return True
