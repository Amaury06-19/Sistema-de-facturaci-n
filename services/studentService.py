from database.database import get_connection

def create_user(id_user: str, name_user: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuario (id_user, name_user, tiene_reserva)
        VALUES (%s, %s, FALSE)
    """, (id_user, name_user))
    conn.commit()
    cursor.close()
    conn.close()
    return {"success": True, "id_user": id_user}
