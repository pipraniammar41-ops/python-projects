#Inventory management

inventory={}

while True:
    print("1. Add product")
    print("2. Display products")
    print("3. find most expensive prodcut")
    print("4. Total Inventory value")

    choice=int(input("Enter your choice: "))
    if choice == 1:
        name= input("Enter your prodcut name: ")
        price= int(input("Enter your price: "))
    
        inventory[name]=price
    
    if choice == 2:
        if len(inventory)== 0:
            print("NO INVENTORY FOUND")
        
        else:
            print("==products==")
            for name,price in inventory.items():
                print(name, ":", price)
        
    if choice == 3:
        if len(inventory)==0:
            print("No ibventory found")
        
            
        else:
            largest_price=None
            expensive_product=""
             
            for name,price in inventory.items():
                if largest_price is None or price > largest_price:
                    largest_price=price
                    expensive_product=name
                    
            print("\n===== Most Expensive Product =====")
            print("Product:", expensive_product)
            print("Price:", largest_price)
      
            
    if choice == 4:
        if len(inventory)==0:
            print("Nop inventory found")
            
        else:
            sum=0
            for price in inventory.values():
                sum+=price
            print(f"The total amount of inventory is: {sum}")
            
    if choice==5:
        print("Thanl you for using our shopping system")
        break
            
            
            
            
            
                
                
        
        
        
        
       
            
    