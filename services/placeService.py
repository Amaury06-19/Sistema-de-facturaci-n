from database.database import get_connection

class placeService:

    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()


    def create_place(self, id_place: str):

        self.cursor.execute("""
            INSERT INTO espacio (id_place, disponible)
            VALUES (%s, TRUE)
        """, (id_place,))
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        return {"success": True, "id_place": id_place}

    def read_available_place(self):

        self.cursor.execute("SELECT * FROM espacio WHERE disponible = TRUE")
        result = self.cursor.fetchall()

        return result