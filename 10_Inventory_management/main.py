#Inventory management system

def add_product():
    product_id=int(input("Enter your product id: "))
    product_name=input("Enter your product name: ")
    price=int(input("Enter price of product"))
    quantiy=int(input("Enter your products quantity"))
    
    with open("inventory.txt",'a') as file:
        # file.write(f"Product id: {product_id},Product name: {product_name},Price: {price}, Quantity: {quantiy}")
        file.write(f"{product_id},{product_name},{price},{quantiy}\n")
    print("Your product has been addedd succesfully")

def view_products():
    
    try:
       file=open("inventory.txt",'r')
       data=file.readlines()
       file.close()
    except FileNotFoundError:
        print("Inventory file not found")
        return
    
    
    
    for line in data:
        line=line.strip()
        part=line.split(",")
        # print(f"Product id: {part[0]}\n prodcut name: {part[1]}\n price: {part[2]}\n Quanity: {part[3]}")
        print(f"Product ID : {part[0]}")
        print(f"Name       : {part[1]}")
        print(f"Price      : ₹{part[2]}")
        print(f"Quantity   : {part[3]}")
    
    
    

def search_product():
    search_id=int(input("Enter product id: "))
    try:
        file=open("inventory.txt",'r')
        data=file.readlines()
        file.close()
    except FileNotFoundError:
        print("Inventory file not found")
        return
    
    found=False
    
    for line  in data:
        line=line.strip()
        part=line.split(",")
        
        if search_id == int(part[0]):
            print(f"Product ID : {part[0]}")
            print(f"Name       : {part[1]}")
            print(f"Price      : ₹{part[2]}")
            print(f"Quantity   : {part[3]}")
            found=True
            break
    if not found:
        
        print("Product not found")
            
    
    

def update_product():
    product_id=input("Enter your product id:")
     
    try:
        file=open("inventory.txt",'r')
        data=file.readlines()
        file.close()
    except FileNotFoundError:
        print("Inventory file not found")
        return
        
    updated_data=[]
    found=False
    
    for line in data:
        line=line.strip()
        part=line.split(",")
        
        if product_id == part[0]:
            
            found=True
            
            print(f"Product ID : {part[0]}")
            print(f"Name       : {part[1]}")
            print(f"Price      : ₹{part[2]}")
            print(f"Quantity   : {part[3]}")
            
            print("\nWhat do you want to update?")
            print("1. Product ID")
            print("2. Product Name")
            print("3. Price")
            print("4. Quantity")
            print("5. Everything")

            choice = int(input("Enter your choice: "))
            
            if choice==1:
                new_product_id=input("Enter new product id: ")
                updated_data.append(f"{new_product_id},{part[1]},{part[2]},{part[3]}\n")
            elif choice ==2:
                new_product_name=input("Enter product name: ")
                updated_data.append(f"{part[0]},{new_product_name},{part[2]},{part[3]}\n")
            elif choice ==3:
                new_price=int(input("Enter new price: "))
                updated_data.append(f"{part[0]},{part[1]},{new_price},{part[3]}\n")
            elif choice ==4:
                new_quantity=input("enter new quanityt: ")
                updated_data.append(f"{part[0]},{part[1]},{part[2]},{new_quantity}\n")
            elif choice ==5:
                new_product_id = input("Enter new product ID: ")
                new_product_name = input("Enter new product name: ")
                new_price = input("Enter new price: ")
                new_quantity = input("Enter new quantity: ")
                
                updated_data.append(f"{new_product_id},{new_product_name},{new_price},{new_quantity}\n")
                
            else:
                print("Invalid choice")
                updated_data.append(line + "\n")
                
        else:
            updated_data.append(line + "\n")
                
    if found:
        file=open("inventory.txt",'w')
        
            
        for line in updated_data:
            
            file.write(line)
        file.close()
        print("product updated succesfully")
    else:
        print("Product not found")
                
def sell_product():
    product_id = input("Enter Product ID: ")
    quantity_sell = int(input("Enter quantity to sell: "))

    try:
        file = open("inventory.txt", "r")
        data = file.readlines()
        file.close()
    except FileNotFoundError:
        print("Inventory file not found.")
        return

    updated_data = []
    found = False

    for line in data:
        line = line.strip()
        part = line.split(",")

        if product_id == part[0]:
            current_quantity = int(part[3])

            if quantity_sell <= current_quantity:
                new_quantity = current_quantity - quantity_sell

                updated_data.append(
                    f"{part[0]},{part[1]},{part[2]},{new_quantity}\n"
                )

                print("Product sold successfully.")
                found = True

            else:
                print("Not enough stock available.")
                updated_data.append(line + "\n")
                found = True

        else:
            updated_data.append(line + "\n")

    if found:
        file = open("inventory.txt", "w")

        for line in updated_data:
            file.write(line)

        file.close()
    else:
        print("Product not found.")
            
def delete_product():
    product_id= input("Enter your product id: ")
    
    try:
        file=open("inventory.txt",'r')
        data=file.readlines()
        file.close()
    except FileNotFoundError:
        print("Inventory file not found")
        
    updated_data=[]
    found=False
    
    for line in data:
        line=line.strip()
        part=line.split(",")
        
        if product_id == part[0]:
            found=True
            
        else:
            updated_data.append(line + "\n")
    
    if found:
        file=open("inventory.txt",'w')
        
        for line in updated_data:
            file.write(line)
        file.close()
        
        print("Product deleted succesfully")
        
    else:
        print("product not found")
            
        
def main():
    while True:
        
        print("\n===== Inventory management System =====")
        print("1.Add prroduct")
        print("2.View prroduct")
        print("3.Search prroduct")
        print("4.update prroduct")
        print("5.Sell prroduct")
        print("6.Delete prroduct")
        
        try:
           choice=int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number")
            continue
            
        if choice==1:
            add_product()
        elif choice==2:
            view_products()
        elif choice==3:
            search_product()
        elif choice==4:
            update_product()
        elif choice==5:
            sell_product()
        elif choice==6:
            delete_product()
        elif choice == 7:
             print("Thank you for using Inventory Management System")
             break
        else:
            print("please enter a valid number between 1 and 6")
            
main()
        
    
            
                
            
        
    
        
    
                
            
        
    
    

    
    

    

    
