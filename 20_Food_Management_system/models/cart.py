
class Cart:
    def __init__(self):
        self.items=[]
        
    
    def add_food(self, food, quantity):
        
        self.items.append((food, quantity))
        print(f"{food.name} added to cart successfully.")
        
    def remove_food(self,food_id):
        
        for item in self.items:
            food=item[0]
            
            if food.food_id == food_id:
                self.items.remove(item)
                
                print(f"{food.name} removed from cart.")
                return
        
        print("Food not found in cart.")
        
    def view_cart(self):
        if len(self.items)==0:
            print("\nYour cart is empty")
            return
        
        print("\n========My cart========")
        
        for food,quantity in self.items:
            print(f"Food ID  : {food.food_id}")
            print(f"Name     : {food.name}")
            print(f"Price    : ₹{food.price}")
            print(f"Quantity : {quantity}")
            print(f"Total    : ₹{food.price * quantity}")
            print("-----------------------------")
        
    def calculate_total(self):
        
        total=0
        
        for food, quantity in self.items:
            total += food.price * quantity
            
        return total
    
    def clear_cart(self):
        self.items.clear()
        print("Cart cleared successfully")


        
        
        
        
        