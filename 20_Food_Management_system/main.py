from models.admin import Admin
from models.customer import Customer
from models.restaurant import Restuarant
from models.food_item import FoodItem
from models.orders import Order
from models.cart import Cart

customers=[]
admins=[]
restaurants=[]
orders = []

def load_sample_admin():
    
    admin=Admin(
        1,
        "Sameer",
        "Admin@gmail.com",
        "9839203849",
        "admin@321",
        "Super admin"
    )
    
    admins.append(admin)
    
def register():
    
    
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phone=int(input("Enter your phone number: "))
    password=input("Enter your password: ")
    customer_id = len(customers) + 101
    
    customer=Customer(
        customer_id,
        name,
        email,
        phone,
        password,
        
    )
    
    customers.append(customer)
    
    print("Registeration done successfully")
    print(f"Your Customer ID : {customer.id}")
    
        
def customer_login():
    
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    
    print(customers)
    
    for customer in customers:
        print(customer.email, customer.password)
        
        if customer.email==email and customer.password==password:
            print("Login succesfully")
            # print(f"Welcome {customer.name}")
            return customer
    print("Invalid Email or Password")
    return None

def admin_login():
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    
    for admin in admins:
        if admin.email==email and admin.password==password:
            print("Login successfully")
            print(f"Welcome {admin.name}")
            print(f"Role : {admin.role}")
            return admin
    
    print("Invalid email or password")
    return None
            
 
def load_sample_restaurants():
    
    restaurant1 = Restuarant(
        1,
        "Domino's",
        "Ahmedabad",
        4.5,
        "Farmhouse Pizza",
        "20% OFF",
        "FREE100",
        True,
        True,
        []
    )
    
    restaurants.append(restaurant1)

def view_restaurants():
    
    print("\n========== RESTAURANTS ==========\n")
    
    for restaurant in restaurants:
        print(f"Restaurant ID : {restaurant.restaurant_id}")
        print(f"Name          : {restaurant.name}")
        print(f"Address       : {restaurant.address}")
        print(f"Rating        : ⭐ {restaurant.rating}")
        print(f"Discount      : {restaurant.discount}")
        print(f"Coupon        : {restaurant.coupon}")
        print("----------------------------")
        
def select_restaurant():
    restaurant_id = int(input("Enter Restaurant ID: "))
    
    for restaurant in restaurants:
        if restaurant.restaurant_id==restaurant_id:
            print(f"{restaurant.name} selected.")
            return restaurant
    print("Restaurant not found.")
    return None

def view_menu(restaurant):
    
    print(f"\n========== {restaurant.name} MENU ==========\n")
    
    for food in restaurant.menu:
        food.display_short()
        

def add_to_cart(customer, restaurant):
    food_id = int(input("Enter Food ID: "))
    quantity = int(input("Enter Quantity: "))
    
    for food in restaurant.menu:
        if food.food_id== food_id:
            customer.cart.add_food(food,quantity)
            
            return
        
    print("ood not found")
        
def place_order(customer, restaurant):
    if len(customer.cart.items) == 0:
        print("Your cart is empty.")
        return
    
    total = customer.cart.calculate_total()
    
    order_id = len(orders) + 1001
    
    order = Order(
        order_id,
        customer,
        restaurant,
        customer.cart.items.copy(),
        total,
        "Preparing"
    )
    
    orders.append(order)
    
    customer.cart.clear_cart()
    
    print("\nOrder placed successfully!")
    print(f"Order ID : {order.order_id}")
    print(f"Total Bill : ₹{order.total}")
    print(f"Status : {order.status}")
    
def view_orders(customer):

    found = False

    print("\n========== MY ORDERS ==========\n")

    for order in orders:

        if order.customer == customer:

            found = True

            print(f"Order ID   : {order.order_id}")
            print(f"Restaurant : {order.restaurant.name}")
            print(f"Total      : ₹{order.total}")
            print(f"Status     : {order.status}")
            print("-------------------------------")

    if not found:
        print("No orders found.")
        
def add_restaurant():

    restaurant_id = len(restaurants) + 1

    name = input("Enter Restaurant Name: ")
    address = input("Enter Address: ")
    rating = float(input("Enter Rating: "))
    special_dishes = input("Enter Special Dish: ")
    discount = input("Enter Discount: ")
    coupon = input("Enter Coupon Code: ")

    veg_available = input("Veg Available (yes/no): ").lower() == "yes"
    non_veg_available = input("Non Veg Available (yes/no): ").lower() == "yes"

    restaurant = Restuarant(
        restaurant_id,
        name,
        address,
        rating,
        special_dishes,
        discount,
        coupon,
        veg_available,
        non_veg_available,
        []
    )

    restaurants.append(restaurant)

    print("\nRestaurant Added Successfully.")

def admin_view_orders():

    if len(orders) == 0:
        print("\nNo orders available.")
        return

    print("\n========== ALL ORDERS ==========\n")

    for order in orders:

        print(f"Order ID      : {order.order_id}")
        print(f"Customer      : {order.customer.name}")
        print(f"Restaurant    : {order.restaurant.name}")

        print("\nItems:")

        for food, quantity in order.items:
            print(f"{food.name} x {quantity} = ₹{food.price * quantity}")

        print(f"\nTotal Amount  : ₹{order.total}")
        print(f"Status        : {order.status}")
        print("----------------------------------------")
        
        
def admin_dashboard(admin):

    while True:

        print("\n========== ADMIN DASHBOARD ==========\n")
        print(f"Welcome {admin.name}")
        print("1. View Restaurants")
        print("2. Add Restaurant")
        print("3. View Orders")
        print("4. Logout")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_restaurants()
        
        elif choice == "2":
            add_restaurant()
        elif choice == "3":
            admin_view_orders()
        elif choice == "4":
            print("Logged out succesfully")
            break
        else:
            print("Invalid choice")
    
def load_sample_food():

    pizza = FoodItem(
        1,
        "Farmhouse Pizza",
        399,
        "Pizza",
        True,
        False,
        "Cheese, Onion, Capsicum, Tomato",
        True
    )

    burger = FoodItem(
        2,
        "Veg Burger",
        199,
        "Burger",
        True,
        False,
        "Bun, Patty, Cheese",
        True
    )

    garlic_bread = FoodItem(
        3,
        "Garlic Bread",
        149,
        "Starter",
        True,
        False,
        "Bread, Garlic, Butter",
        True
    )

    coke = FoodItem(
        4,
        "Coca Cola",
        60,
        "Drink",
        True,
        False,
        "Carbonated Drink",
        True
    )
    
    restaurants[0].menu.append(pizza)
    restaurants[0].menu.append(burger)
    restaurants[0].menu.append(garlic_bread)
    restaurants[0].menu.append(coke)
    
    
    
            
            

def customer_dashboard(customer):
    
    while True:
        
        print("\n========== CUSTOMER DASHBOARD ==========\n")
        print(f"Welcome {customer.name}")
        print()
        print("1. View Restaurants")
        print("2.View cart")
        print("3.Place Order")
        print("4. View Orders")
        print("5. Logout")
        
        choice=input("Enter your choice")
        
        if choice == "1":
            view_restaurants()
            restaurant=select_restaurant()
            
            if restaurant:
                view_menu(restaurant)
                add_to_cart(customer, restaurant)
                
        elif choice =="2":
            customer.cart.view_cart()
        elif choice == "3":
            place_order(customer, restaurant)
        elif choice == "4":
            view_orders(customer)
        elif choice=="5":
            print("Thank you for using our system.")
            break
  

def main():
    
    load_sample_admin()
    load_sample_restaurants()
    load_sample_food()
    while True:
        
        print("=========================\n")
        print("SWIGGY\n")
        print("=========================\n")
        print("1.Register")
        print("2.Customer login")
        print("3.Admin login")
        print("4.Exit")
        
        choice=input("Enter your choice: ")
        
        if choice == "1":
            register()
        elif choice =="2":
            customer=customer_login()
            
            if customer:
                customer_dashboard(customer)
        elif choice=="3":
            admin=admin_login()
            if admin:
                admin_dashboard(admin)
        elif choice == "4":
            print("Thank you for using Swiggy.")
            break
        else:
            print("Invalid choice")
            break
            

main()
        
        