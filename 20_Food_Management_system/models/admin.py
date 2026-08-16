from .user import User


class Admin(User):
    def __init__(self, id, name, email, phone, password,role):
        super().__init__(id, name, email, phone, password)
        self.role=role
        