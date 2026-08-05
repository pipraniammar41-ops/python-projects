from .user import User
from .cart import Cart

class Customer(User):
    def __init__(self, id, name, email, phone, password):
        super().__init__(id, name, email, phone, password)
        self.addresses=[]
        self.cart=Cart(self)
        self.orders=[]
        
    
    


