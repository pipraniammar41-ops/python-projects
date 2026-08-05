

from stock import stocks

def add_product():
    product_id=int(input("Enter product id: "))
    product_name=input("Enter product name: ")
    prices=int(input("Enter price: "))
    quantity=int(input("Enter your quanity: "))
    category=input("Enter your category: ")
    
    stockk={
        "id": product_id,
        "name": product_name,
        "price":prices,
        "quantity": quantity,
        "category": category
    }
    
    stocks.append(stockk)
    print("Product added successfully")

def view_products():
    if len(stocks)==0:
        print("No product found")
        return
    
    for stockk in stocks:
        print("\nAll products\n")
        print(f"Id : {stockk['id']}")
        print(f"Name : {stockk['name']}")
        print(f"Price : {stockk['price']}")
        print(f"Quantity : {stockk['quantity']}")
        print(f"Category : {stockk['category']}")
        
def search_product():
        
    if len(stocks)==0:
        print("No product found")
        return
    
    search_id=int(input("Enter your id: "))
    
    filtered = filter(lambda stock: stock["id"] == search_id, stocks)
    
    for stockk in filtered:
            print(f"Id : {stockk['id']}")
            print(f"Name : {stockk['name']}")
            print(f"Price : {stockk['price']}")
            print(f"Quanity : {stockk['quantity']}")
            print(f"Category : {stockk['category']}")
            return
        
    print("Please enter a valid id.")
    
def update_product():
    if len(stocks)==0:
        print("No product found")
        return
    produ_id=int(input("Enter your product id: "))
    
    
    for stockk in stocks:
        if stockk['id']==produ_id:
            print("\nWhat do you want to update\n")
            print("1.Id")
            print("2.Name")
            print("3.Price")
            print("4.Quanity")
            print("5.Category")
            
            choice=int(input("Enter your choice: "))
            
            if choice==1:
                stockk['id']= int(input("Enter new id: "))
            elif choice==2:
                stockk['name']=input("Enter new name: ")
            elif choice==3:
                stockk['price']=int(input("Enter new price"))
            elif choice==4:
                stockk['quantity']=int(input("Enter new quanity"))
            elif choice==5:
                stockk['category']=input("Enter new category: ")
            else:
                print("Not valid input.")
                return
            
            print("\nProduct added successfully")
            return
                
def delete_product():
    if len(stocks) == 0:
        print("No product found")
        return

    prod_id = int(input("Enter Product ID: "))

    for index, stock in enumerate(stocks):
        if stock["id"] == prod_id:
            deleted_stock = stocks.pop(index)

            print("Product deleted successfully!")
            print(f"Deleted ID       : {deleted_stock['id']}")
            print(f"Deleted Name     : {deleted_stock['name']}")
            print(f"Deleted Price    : {deleted_stock['price']}")
            print(f"Deleted Quantity : {deleted_stock['quantity']}")
            print(f"Deleted Category : {deleted_stock['category']}")
            return

    print("Product ID not found.")
                
def purchase_product():
    if len(stocks)==0:
        print("No product found")
        return
    produc_id=int(input("Enter your product id: "))
    
    
    for stockk in stocks:
        if stockk["id"]==produc_id:
            print(f"Name: {stockk['name']}")
            print(f"Price: {stockk['price']}")
            print(f"Available Quanity: {stockk['quantity']}")
            
            quantityy=int(input("Enter how much quantity you want to purchase: "))
            
            if quantityy > stockk["quantity"]:
                print(f"Available : {stockk['quantity']}")
                print(f"Want : {quantityy}\n")
                print("Insufficeient stock")
                return
            else:
                
                stockk["quantity"]-=quantityy
                print(f"Quantity left: {stockk['quantity']}")
                print("Purchase successfull\n")
                
                print(f"Product name : {stockk['name']}")
                print(f"Purchase quanity: {quantityy}")
                print(f"Total bill : {quantityy * stockk['price']}")
                print(f"Remaining stock: {stockk['quantity']}")
                return
        
        
    print("product id not found")

def restock_product():
    if len(stocks)==0:
        print("No product found")
        return
    
    produc_id=int(input("Enter your product id: "))
    
    for stockk in stocks:
        if stockk["id"]==produc_id:
            print(f"Name : {stockk['name']}")
            print(f"Current stock : {stockk['quantity']}")
            
            restock=int(input("Enter quantity to restock: "))
            
            stockk['quantity']+=restock
            
            print("Restock successfull\n")
            print(f"Product Name : {stockk['name']}")
            print(f"Added quanity: {restock}")
            print(f"Updated stock : {stockk['quantity']}")
            return
            
    print("Product id not found")

def low_stock_alert():
    if len(stocks)==0:
        print("No product found")
        return
    
    low_stock_limit=int(input("Enter your low stock limit: "))
    
    found=False
    for stockk in stocks:
        if stockk["quantity"] <=low_stock_limit:
            found=True
            
            print(f"Id : {stockk['id']}")
            print(f"Name : {stockk['name']}")
            print(f"Quantity : {stockk['quantity']}")
            print(f"Category : {stockk['category']}")
            
        
    if not found:
        print("No low stock products found.")

def total_inventory_value():
    if len(stocks)==0:
        print("No product found")
        return
    
    total_value=0
    
    for stockk in stocks:
        # total_value+=stockk['price']
        product_value=stockk['quantity'] * stockk['price']
        total_value += product_value
    print(f"Total Inventory value : {total_value}")
        
def most_expensive_product():
    if len(stocks)==0:
        print("No product found")
        return
    
    most_expensive=stocks[0]
    
    for stockk in stocks:
        if stockk["price"] > most_expensive["price"]:
            most_expensive=stockk
            
    print("Most expensive products\n")
    print(f"ID : {most_expensive['id']}")
    print(f"Name : {most_expensive['name']}")
    print(f"Price : {most_expensive['price']}")
    print(f"Category : {most_expensive['category']}")

def cheapest_product():
    if len(stocks)==0:
        print("No product found")
        return
    
    cheapest_produ=stocks[0]
    
    for stockk in stocks:
        if stockk["price"] < cheapest_produ["price"]:
            cheapest_produ=stockk
            
    print("Cheapest products\n")
    print(f"ID : {cheapest_produ['id']}")
    print(f"Name : {cheapest_produ['name']}")
    print(f"Price : {cheapest_produ['price']}")
    print(f"Category : {cheapest_produ['category']}")
    
def shorted():
    if len(stocks)==0:
        print("NO Product found")
        return
    
    print("1.Low to high")
    print("2.High to low")
    
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        shortt=sorted(stocks,key=lambda stockk: stockk["price"])
    elif choice==2:
        shortt=sorted(stocks,key=lambda stockk: stockk["price"] ,reverse=True)
    
    else:
        print("Enter a valid choice")
        return
    
    print("\nSorted products\n")
    
    for stock1 in shortt:
        print(f"Id : {stock1['id']}")
        print(f"Name : {stock1['name']}")
        print(f"Price : {stock1['price']}")
        print(f"Quantity : {stock1['quantity']}")
        print(f"Category : {stock1['category']}")
        
def save_file():
    file=open("Data11.txt",'w')
    
    for stockk in stocks:
        
        file.write(
            f"{stockk['id']},{stockk['name']},{stockk['price']},{stockk['quantity']},{stockk['category']}\n"
        )
    
    file.close()
    
    print("File addedd succesfullt")

def load_file():
    file=open("Data11.txt",'r')
    
    # stocks.clear()
    
    for line in file:
        
        line=line.strip()
        
        id,name,price,quantity,category=line.split(",")
        
        stock = {
            "id": int(id),
            "name": name,
            "price": int(price),
            "quantity": int(quantity),
            "category": category
            
        }
        
        stocks.append(stock)
    
    file.close()
    print("Product loaded successfully")
    
def main():

    try:
       load_file()
    except FileNotFoundError:
        print("No saved data found. Using default products.")
        

    while True:

        print("\n========== Inventory & Sales Management ==========")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Purchase Product")
        print("7. Restock Product")
        print("8. Low Stock Alert")
        print("9. Total Inventory Value")
        print("10. Most Expensive Product")
        print("11. Cheapest Product")
        print("12. Sort Products")
        print("13. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            add_product()

        elif choice == 2:
            view_products()

        elif choice == 3:
            search_product()

        elif choice == 4:
            update_product()

        elif choice == 5:
            delete_product()

        elif choice == 6:
            purchase_product()

        elif choice == 7:
            restock_product()

        elif choice == 8:
            low_stock_alert()

        elif choice == 9:
            total_inventory_value()

        elif choice == 10:
            most_expensive_product()

        elif choice == 11:
            cheapest_product()

        elif choice == 12:
            shorted()

        elif choice == 13:
            save_file()
            print("Thank you for using Inventory & Sales Management.")
            break

        else:
            print("Invalid Choice")


main()




        









































































