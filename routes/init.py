from fastapi import APIRouter
from .usuarios import router as usuarios_router
from .empresas import router as empresas_router
from .impuestos import router as impuestos_router
from .productos import router as productos_router
from .terceros import router as terceros_router
from .series import router as series_router
from .documentos_venta import router as documentos_venta_router
from .categorias_gasto import router as categorias_gasto_router
from .gastos import router as gastos_router

api_router = APIRouter()
api_router.include_router(usuarios_router, prefix="/usuarios", tags=["usuarios"])
api_router.include_router(empresas_router, prefix="/empresas", tags=["empresas"])
api_router.include_router(impuestos_router, prefix="/impuestos", tags=["impuestos"])
api_router.include_router(productos_router, prefix="/productos", tags=["productos"])
api_router.include_router(terceros_router, prefix="/terceros", tags=["terceros"])
api_router.include_router(series_router, prefix="/series", tags=["series_numeracion"])
api_router.include_router(documentos_venta_router, prefix="/documentos-venta", tags=["documentos_venta"])
api_router.include_router(categorias_gasto_router, prefix="/categorias-gasto", tags=["categorias_gasto"])
api_router.include_router(gastos_router, prefix="/gastos", tags=["gastos"])
