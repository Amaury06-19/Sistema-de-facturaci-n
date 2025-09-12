# Este archivo permite que la carpeta routes sea tratada como un paquete Python.

from .categorias_gasto import *
from .deps import *
from .documentos_venta import *
from .empresas import *
from .gastos import *
from .handlers import *
from .impuestos import *
from .productos import *
from .series import *
from .terceros import *
from .usuarios import *


# Exportar api_router para main.py
from .init import api_router
