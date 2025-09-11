from models.User import User

class Admin(User):

    def __init__(self, id, name, password):
        super().__init__(id, name, password)

        pass