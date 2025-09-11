from database.database import get_connection

class ReservationService:

    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor(dictionary=True)

    def create_reservation(self, id_user:str, id_place:int, start_hour:str, end_hour: str):

        #Verificar usuario
        self.cursor.execute("SELECT tiene_reserva FROM usuario WHERE id_user = %s", (id_user,))
        user = self.cursor.fetchone()
        if not user:
            return {"error": f"ID recibido: '{id_user}'"}
        if user["tiene_reserva"]:
            return {"error": "Usuario ya tiene una reserva activa"}

        #Verificar espacio
        self.cursor.execute("SELECT disponible FROM espacio WHERE id_place = %s", (id_place,))
        espacio = self.cursor.fetchone()
        if not espacio:
            return {"error": "Espacio no existe"}
        if not espacio["disponible"]:
            return {"error": "Espacio no disponible"}

        #Crear reserva
        self.cursor.execute("""
            INSERT INTO reserva (start_hour, end_hour, id_user, id_place)
            VALUES (%s, %s, %s, %s)
        """, (start_hour, end_hour, id_user, id_place))
        self.conn.commit()
        id_reserv = self.cursor.lastrowid

        #Actualizar usuario y espacio
        self.cursor.execute("UPDATE usuario SET tiene_reserva = TRUE WHERE id_user = %s", (id_user,))
        self.cursor.execute("UPDATE espacio SET disponible = FALSE WHERE id_place = %s", (id_place,))
        self.conn.commit()

        return {"success": True, "id_reserva": id_reserv}
    
    def read_Reservation(self, id_user:str):
        self.cursor.execute("SELECT * FROM reserva WHERE id_user = %s", (id_user,))
        result = self.cursor.fetchall()
        return result
    
    def delete_Reservation(self, id_user: str):

        self.cursor.execute("SELECT id_place FROM reserva WHERE id_user = %s", (id_user,))
        reserva = self.cursor.fetchone()
        if reserva is None:
            self.cursor.close()
            return {"error": "No existe una reserva asociada a este usuario"}

        id_place = reserva["id_place"]

        self.cursor.execute("UPDATE usuario SET tiene_reserva = FALSE WHERE id_user = %s", (id_user,))

        self.cursor.execute("UPDATE espacio SET disponible = TRUE WHERE id_place = %s", (id_place,))

        self.cursor.execute("DELETE FROM reserva WHERE id_user = %s", (id_user,))
        self.conn.commit()
        self.cursor.close()

        return {"success": True, "message": f"Reserva eliminada y espacio {id_place} liberado"}
