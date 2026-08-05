from .user import User

class Admin(User):
    def __init__(self, id, name, email, phone, password,role):
        super().__init__(id, name, email, phone, password)
        self.role=role
    
    def view_profile(self):
        print("\n========== ADMIN ==========")

        print(f"ID      : {self.id}")
        print(f"Name    : {self.name}")
        print(f"Email   : {self.email}")
        print(f"Phone   : {self.phone}")
        print(f"Role    : {self.role}")






    


    