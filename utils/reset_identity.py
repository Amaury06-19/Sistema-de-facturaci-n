from sqlalchemy import text
from database.session import get_session

def reset_identity(tabla: str, nuevo_valor: int = 0):
    """
    Reinicia el contador IDENTITY de la tabla especificada.
    Si la tabla está vacía y nuevo_valor=0, el próximo id será 1.
    """
    session = next(get_session())
    session.execute(text(f"DBCC CHECKIDENT ('{tabla}', RESEED, {nuevo_valor})"))
    session.commit()
    session.close()

def reset_all_identities():
    """
    Reinicia el identity de todas las tablas principales según el valor máximo de su columna ID.
    """
    session = next(get_session())
    tablas_columnas = [
        ("usuario", "id_usuario"),
        ("empresa", "id_empresa"),
        ("tercero", "id_tercero"),
        ("producto", "id_producto"),
        ("impuesto", "id_impuesto"),
        ("serie_numeracion", "id_serie_numeracion"),
        ("categoria_gasto", "id_categoria_gasto"),
        ("documento_venta", "id_documento_venta"),
        ("documento_venta_linea", "id_documento_venta_linea"),
        ("pago", "id_pago"),
        ("gasto", "id_gasto"),
        ("gasto_adjunto", "id_gasto_adjunto"),
        ("usuario_empresa", "id_usuario_empresa"),
        ("log_auditoria", "id_log_auditoria"),
        ("log_acceso", "id_log_acceso"),
        ("recuperacion_acceso", "id_recuperacion_acceso"),
        ("pais", "id_pais"),
        ("ciudad", "id_ciudad"),
        ("tipo_cliente", "id_tipo_cliente"),
        ("vendedor", "id_vendedor"),
        ("medio_pago", "id_medio_pago"),
    ]
    for tabla, columna in tablas_columnas:
        max_id = session.execute(text(f"SELECT ISNULL(MAX([{columna}]), 0) FROM [{tabla}]"))
        max_id = max_id.scalar() or 0
        session.execute(text(f"DBCC CHECKIDENT ('{tabla}', RESEED, {max_id})"))
    session.commit()
    session.close()

# Ejemplo de uso para una tabla:
# reset_identity('empresa')
# Ejemplo de uso para todas:
# reset_all_identities()
