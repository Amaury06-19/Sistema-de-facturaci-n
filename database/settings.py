from __future__ import annotations

from urllib.parse import quote_plus
from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    DB_DRIVER: str = "ODBC Driver 18 for SQL Server"
    DB_HOST: str = "nodossolutions.com"
    DB_PORT: int = 1435
    DB_NAME: str = "Facturacion_db"
    DB_USER: str = "talento"
    DB_PASSWORD: str = "cartagena"
    DB_ENCRYPT: bool = True
    DB_TRUST_SERVER_CERT: bool = True
    DB_TIMEOUT: int = 30

    DB_POOL_SIZE: int = 10
    DB_MAX_OVERFLOW: int = 20
    DB_POOL_PRE_PING: bool = True
    DB_ECHO: bool = False
    DB_FAST_EXECUTEMANY: bool = True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    def odbc_dsn(self) -> str:
        # Formato DSN-less para pyodbc
        parts = [
            f"Driver={{{self.DB_DRIVER}}}",
            f"Server={self.DB_HOST},{self.DB_PORT}",
            f"Database={self.DB_NAME}",
            f"Uid={self.DB_USER}",
            f"Pwd={self.DB_PASSWORD}",
            f"Encrypt={'yes' if self.DB_ENCRYPT else 'no'}",
            f"TrustServerCertificate={'yes' if self.DB_TRUST_SERVER_CERT else 'no'}",
            f"Connection Timeout={self.DB_TIMEOUT}",
            "ApplicationIntent=ReadWrite",
            "MultiSubnetFailover=Yes",
        ]
        return ";".join(parts)

    def sqlalchemy_url(self) -> str:
        return f"mssql+pyodbc:///?odbc_connect={quote_plus(self.odbc_dsn())}"


settings = DBSettings()
