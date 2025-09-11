class User:

    def __init__(self, id: str, name: str, password: str):

        self.id = id
        self.name = name
        self._password = password

    