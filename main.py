from __future__ import annotations

import os
from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from loguru import logger

from routes import api_router
from routes.handlers import register_exception_handlers
from database import test_connection

API_TITLE = "Cashly API"
API_VERSION = "0.1.0"

tags_metadata = [
    {"name": "usuarios", "description": "Gestión de usuarios"},
    {"name": "empresas", "description": "Gestión de empresas"},
    {"name": "impuestos", "description": "Configuración de impuestos"},
    {"name": "productos", "description": "Catálogo de productos"},
    {"name": "terceros", "description": "Clientes y proveedores"},
    {"name": "series_numeracion", "description": "Series y consecutivos"},
    {"name": "documentos_venta", "description": "Facturas y recibos"},
    {"name": "categorias_gasto", "description": "Categorías de gasto"},
    {"name": "gastos", "description": "Gastos y adjuntos"},
]

def _parse_origins() -> List[str]:
    raw = os.getenv("CORS_ORIGINS", "")
    if not raw:
        # valores útiles en dev; ajusta según tu frontend
        return [
            "http://localhost:3000",
            "http://localhost:5173",
            "http://127.0.0.1:3000",
            "http://127.0.0.1:5173",
        ]
    return [o.strip() for o in raw.split(",") if o.strip()]

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        test_connection()
        logger.info("Conexión a SQL Server verificada correctamente.")
        if os.getenv("APP_CREATE_ALL", "").lower() in ("1", "true", "yes"):
            from .database.init_db import create_all
            create_all()
            logger.warning("APP_CREATE_ALL activo: metadata creada en la BD.")
        yield
    finally:
        logger.info("Apagando aplicación...")

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    default_response_class=ORJSONResponse,
    openapi_tags=tags_metadata,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=_parse_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)
app.include_router(api_router, prefix="/api")

@app.get("/", include_in_schema=False)
def root():
    return {"name": API_TITLE, "version": API_VERSION}

@app.get("/healthz", include_in_schema=False)
def healthz():
    return {"status": "ok"}

@app.get("/readyz", include_in_schema=False)
def readyz():
    # Verificación rápida de readiness con DB
    test_connection()
    return {"status": "ready"}
