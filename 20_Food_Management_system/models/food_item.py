
class FoodItem:
    def __init__(self,food_id,name,price,category,is_veg,spicy,ingredients,available):
        self.food_id=food_id
        self.name=name
        self.price=price
        self.category=category
        self.is_veg=is_veg
        self.spicy=spicy
        self.ingredients=ingredients
        self.available=available
        
    def display_details(self):
        print(f"Food ID      : {self.food_id}")
        print(f"Name         : {self.name}")
        print(f"Price        : ₹{self.price}")
        print(f"Category     : {self.category}")

        if self.is_veg:
            print("Veg          : Yes")
        else:
            print("Veg          : No")

        if self.spicy:
            print("Spicy        : Yes")
        else:
            print("Spicy        : No")

        print(f"Ingredients  : {self.ingredients}")

        if self.available:
            print("Available    : Yes")
        else:
            print("Available    : No")

        print("----------------------------")
        
    def display_short(self):
        print(f"Food ID : {self.food_id}")
        print(f"Name    : {self.name}")
        print(f"Price   : ₹{self.price}")

        if self.is_veg:
            print("Type    : Veg")
        else:
            print("Type    : Non Veg")

        print("----------------------------")
        