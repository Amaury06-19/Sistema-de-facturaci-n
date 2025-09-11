from models.User import User

class Student(User):

    def __init__(self, id, name, password):
        super().__init__(id, name, password)

        self.can_reserv = True
