from models.customer import Customer
from models.admin import Admin
from models.product import Product
from models.order import Order
from models.payment import Payment
from models.address import Address

customers = []
admins = []
products = []
orders = []
payments = []


def load_sample_admin():

    admin = Admin(
        1,
        "Sameer Admin",
        "admin@gmail.com",
        "9876543210",
        "admin123",
        "Super Admin"
    )

    admins.append(admin)


def load_sample_customers():

    customer1 = Customer(
        101,
        "Rahul Sharma",
        "rahul@gmail.com",
        "9876543211",
        "rahul123"
    )

    customer2 = Customer(
        102,
        "Priya Patel",
        "priya@gmail.com",
        "9876543212",
        "priya123"
    )

    customer3 = Customer(
        103,
        "Aman Verma",
        "aman@gmail.com",
        "9876543213",
        "aman123"
    )

    customers.append(customer1)
    customers.append(customer2)
    customers.append(customer3)


def load_sample_products():

    product1 = Product(
        1,
        "Wooden Wall Clock",
        "HomeCraft",
        "Wall Decor",
        "Premium wooden wall clock",
        1499,
        20,
        "Brown",
        4.7,
        185,
        "3 Days",
        "7 Days"
    )

    product2 = Product(
        2,
        "Ceramic Flower Vase",
        "DecorArt",
        "Vases",
        "Elegant ceramic flower vase",
        899,
        30,
        "White",
        4.5,
        240,
        "2 Days",
        "7 Days"
    )

    product3 = Product(
        3,
        "LED Table Lamp",
        "BrightHome",
        "Lighting",
        "Modern LED table lamp",
        1999,
        15,
        "Black",
        4.8,
        520,
        "2 Days",
        "10 Days"
    )

    products.append(product1)
    products.append(product2)
    products.append(product3)
    
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
        password
    )
    customers.append(customer)
    
    print("\nAccount created successfully.")
    print(f"Your Customer ID : {customer.id}")
    
    return customer
    
def login():
    
    print("\n========== LOGIN ==========\n")
    
    email = input("Enter your email : ")
    password = input("Enter your password : ")
    
    for customer in customers:
        if customer.email == email and customer.password == password:
            print("\nLogin Successful.")
            print(f"Welcome {customer.name}")
            
            return customer
        
    print("\nInvalid Email or Password.")
    
    return None

def search_product():
    keyword = input("\nEnter product name : ").lower()
    found = False
    
    for product in products:
        
        if keyword in product.name.lower():
            product.display_details()
            
            found = True
            
    if not found:
        print("\nProduct not found.")
    
def add_to_cart(customer):

    print("\n========== ADD TO CART ==========\n")

    product_id = int(input("Enter Product ID : "))
    quantity = int(input("Enter Quantity : "))

    for product in products:

        if product.id == product_id:

            customer.cart.add_product(product, quantity)

            return

    print("Product not found.")

def add_address(customer):

    print("\n========== ADD ADDRESS ==========\n")

    house = input("House No / Flat No : ")
    area = input("Area : ")
    city = input("City : ")
    state = input("State : ")
    country = input("Country : ")
    pincode = input("Pincode : ")

    address = Address(
        len(customer.addresses) + 1,
        customer.name,
        customer.phone,
        house,
        area,
        city,
        state,
        country,
        pincode
    )

    customer.addresses.append(address)

    print("\nAddress added successfully.")
    

    
def checkout(customer):

    print("\n========== CHECKOUT ==========\n")

    
    if len(customer.cart.products) == 0:
        print("Your cart is empty.")
        return

    
    if len(customer.addresses) == 0:
        print("Please add an address first.")
        return

   
    print("\nSelect Delivery Address\n")

    for i, address in enumerate(customer.addresses, start=1):
        print(f"Address {i}")
        address.display()

    
    choice = int(input("Enter Address Number : "))

    if choice < 1 or choice > len(customer.addresses):
        print("Invalid Address.")
        return

    selected_address = customer.addresses[choice - 1]

    
    print("\n========== PAYMENT ==========\n")

    print("1. UPI")
    print("2. Card")
    print("3. Cash On Delivery")

    payment_choice = input("Enter your choice : ")

    if payment_choice == "1":
        payment_method = "UPI"

    elif payment_choice == "2":
        payment_method = "Card"

    elif payment_choice == "3":
        payment_method = "Cash On Delivery"

    else:
        print("Invalid Payment Method.")
        return

    
    total_amount = customer.cart.calculate_total()

   
    payment = Payment(
        len(payments) + 1,
        None,
        total_amount,
        payment_method,
        "Paid",
        "05-08-2026"
    )

    payments.append(payment)

    
    order = Order(
        len(orders) + 1,
        customer,
        customer.cart.products.copy(),
        selected_address,
        total_amount,
        payment,
        "Pending",
        "05-08-2026",
        "08-08-2026"
    )

   
    payment.order = order

    
    order.place_order()

    
    orders.append(order)
    customer.orders.append(order)

    
    customer.cart.clear_cart()

    print("\n===================================")
    print("Order Placed Successfully 🎉")
    print(f"Order ID : {order.order_id}")
    print(f"Total Amount : ₹{total_amount}")
    print(f"Payment Method : {payment_method}")
    print("===================================")

def view_orders(customer):

    print("\n========== MY ORDERS ==========\n")

    if len(customer.orders) == 0:
        print("No orders found.")
        return

    for order in customer.orders:

        order.view_order_details()

        print("-" * 40)
        
def track_order(customer):

    print("\n========== TRACK ORDER ==========\n")

    if len(customer.orders) == 0:
        print("No orders found.")
        return

    order_id = int(input("Enter Order ID : "))

    for order in customer.orders:

        if order.order_id == order_id:

            order.track_order()
            return

    print("Order not found.")

def cancel_order(customer):

    print("\n========== CANCEL ORDER ==========\n")

    if len(customer.orders) == 0:
        print("No orders found.")
        return

    order_id = int(input("Enter Order ID : "))

    for order in customer.orders:

        if order.order_id == order_id:

            order.cancel_order()
            return

    print("Order not found.")

def admin_login():

    print("\n========== ADMIN LOGIN ==========\n")

    email = input("Enter Email : ")
    password = input("Enter Password : ")

    for admin in admins:

        if admin.email == email and admin.password == password:

            print(f"\nWelcome {admin.name}")
            return admin

    print("Invalid Email or Password.")

    return None

def add_product():

    print("\n========== ADD PRODUCT ==========\n")

    product_id = len(products) + 1

    name = input("Enter Product Name : ")
    brand = input("Enter Brand Name : ")
    category = input("Enter Category : ")
    description = input("Enter Description : ")

    price = float(input("Enter Price : "))
    stock = int(input("Enter Stock Quantity : "))

    variant = input("Enter Variant : ")

    rating = float(input("Enter Rating : "))
    reviews = int(input("Enter Number of Reviews : "))

    delivery_days = input("Enter Delivery Days : ")
    return_days = input("Enter Return Policy : ")

    product = Product(
        product_id,
        name,
        brand,
        category,
        description,
        price,
        stock,
        variant,
        rating,
        reviews,
        delivery_days,
        return_days
    )

    products.append(product)

    print("\n===================================")
    print("Product Added Successfully ✅")
    print(f"Product ID : {product.id}")
    print(f"Product Name : {product.name}")
    print("===================================")

def update_product():

    print("\n========== UPDATE PRODUCT ==========\n")

    product_id = int(input("Enter Product ID : "))

    for product in products:

        if product.id == product_id:

            print("\nLeave blank if you don't want to change a value.\n")

            name = input(f"Product Name ({product.name}) : ")
            brand = input(f"Brand ({product.brand}) : ")
            category = input(f"Category ({product.category}) : ")
            description = input(f"Description ({product.description}) : ")
            price = input(f"Price ({product.price}) : ")
            stock = input(f"Stock ({product.stock}) : ")
            variant = input(f"Variant ({product.variant}) : ")
            delivery = input(f"Delivery Days ({product.delivery_days}) : ")
            returns = input(f"Return Days ({product.return_days}) : ")

            if name:
                product.name = name

            if brand:
                product.brand = brand

            if category:
                product.category = category

            if description:
                product.description = description

            if price:
                product.price = float(price)

            if stock:
                product.stock = int(stock)

            if variant:
                product.variant = variant

            if delivery:
                product.delivery_days = delivery

            if returns:
                product.return_days = returns

            print("\nProduct Updated Successfully.")
            return

    print("Product Not Found.")

def delete_product():

    print("\n========== DELETE PRODUCT ==========\n")

    product_id = int(input("Enter Product ID : "))

    for product in products:

        if product.id == product_id:

            products.remove(product)

            print("\nProduct Deleted Successfully.")
            return

    print("Product Not Found.")

def view_all_products():

    print("\n========== ALL PRODUCTS ==========\n")

    if len(products) == 0:
        print("No products available.")
        return

    for product in products:

        product.display_details()
    
def manage_stock():

    print("\n========== MANAGE STOCK ==========\n")

    product_id = int(input("Enter Product ID : "))

    for product in products:

        if product.id == product_id:

            print(f"\nCurrent Stock : {product.stock}")

            print("\n1. Increase Stock")
            print("2. Decrease Stock")

            choice = input("Enter Choice : ")

            quantity = int(input("Enter Quantity : "))

            if choice == "1":

                product.increase_stock(quantity)

            elif choice == "2":

                product.decrease_stock(quantity)

            else:

                print("Invalid Choice.")

            return

    print("Product Not Found.")

def view_all_orders():

    print("\n========== ALL ORDERS ==========\n")

    if len(orders) == 0:

        print("No Orders Found.")
        return

    for order in orders:

        order.view_order_details()

        print("-" * 50)
    
def view_customers():

    print("\n========== ALL CUSTOMERS ==========\n")

    if len(customers) == 0:

        print("No Customers Found.")
        return

    for customer in customers:

        print(f"Customer ID : {customer.id}")
        print(f"Name        : {customer.name}")
        print(f"Email       : {customer.email}")
        print(f"Phone       : {customer.phone}")
        print(f"Orders      : {len(customer.orders)}")
        print(f"Addresses   : {len(customer.addresses)}")

        print("-" * 50)

 
def customer_dashboard(customer):
    
    while True:
        
        print("\n" + "=" * 50)
        print(f"      Welcome {customer.name}")
        print("=" * 50)
        
        print("1. View Products")
        print("2. Search Product")
        print("3. Add Product to Cart")
        print("4. View Cart")
        print("5. Add Address")
        print("6. Checkout")
        print("7. View Orders")
        print("8. Track order")
        print("9. Cancel order")
        print("10. Logout")
        
        choice = input("\nEnter your choice : ")
        
        if choice == "1":
            
            print("\n========== PRODUCTS ==========\n")
            
            for product in products:
                product.display_details()
                
        elif choice == "2":
            search_product()
                
        elif choice == "3":

            add_to_cart(customer)
        
        elif choice == "4":

            customer.cart.view_cart()
        
        elif choice == "5":

            add_address(customer)
            
        elif choice == "6":
            checkout(customer)
        
        elif choice == "7":
            view_orders(customer)
            
        elif choice == "8":
            track_order(customer)
            
        elif choice == "9":
            cancel_order(customer)
            
        elif choice == "10":
            print("Logged out successfully.")
            break
    
        else:

            print("Invalid Choice.")
    

def admin_dashboard(admin):

    while True:

        print("\n" + "=" * 50)
        print(f"      Welcome {admin.name}")
        print("=" * 50)

        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Products")
        print("5. Manage Stock")
        print("6. View Orders")
        print("7. View Customers")
        print("8. Logout")

        choice = input("\nEnter your choice : ")

        if choice == "1":

            add_product()

        elif choice == "2":

            update_product()

        elif choice == "3":

            delete_product()

        elif choice == "4":

            view_all_products()

        elif choice == "5":

            manage_stock()

        elif choice == "6":
            

            view_all_orders()

        elif choice == "7":

            view_customers()

        elif choice == "8":

            print("Admin Logged Out Successfully.")
            break

        else:

            print("Invalid Choice.")
    
    
def main():
    load_sample_admin()
    load_sample_customers()
    load_sample_products()
    
    while True:
        
        
        print("\n===================================")
        print("         AMAZON INDIA")
        print("===================================")
        
        print("1. Register")
        print("2.Customer Login")
        print("3.Admin login")
        print("4.Exit")
        
        choice = input("\nEnter your choice : ")
        
        if choice == "1":
            customer = register()
            
            if customer:
                customer_dashboard(customer)
            
            
        
        elif choice== "2":
            customer = login()
            
            if customer:
                customer_dashboard(customer)
                
        
        elif choice == "3":
            admin = admin_login()
            
            if admin:
                admin_dashboard(admin)
           
        elif choice == "4":
            print("Thank you for visiting Amazon.")
            break     
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
    