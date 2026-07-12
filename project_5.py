#Contact Book

contacts={}

while True:
    print("1. Add new contacts")
    print("2. Search contacts")
    print("3. Update contacts")
    print("4. Delete contacts")
    print("5. Display all contacts")
    print("6. Exit the program")

    choose=int(input("Enter your choice: "))
    
    if choose==1:
        name=input("Enter your name: ")
        number=input("Enter your mobile number: ")
    
        if len(number) < 10:
            print("❌ Mobile number must be at least 10 digits")
        
        else:
            contacts[name]=number
            print("✅ Contact Added Successfully")

            
    elif choose==2:
            
        search_name=input("Enter your name to search: ")
        
        if search_name in contacts:
            print(contacts[search_name])
        
        else:
            print("Contact not found")
            
    
    elif choose==3:
        update_number= input("Enter the name of contact to update:")
        
        if update_number in contacts:
            enter_number=input("Enter new number: ")
            contacts[update_number]=enter_number
            print("✅ Contact Updated Successfully")
        
        else:
            print("❌ Contact Not Found")
            
    elif choose==4:
        delete_name= input("Tell name of contact whihc you want to delete: ")
        
        if delete_name in contacts:
            del contacts[delete_name]
            print("Contact deleted successfully")
            
        else:
            print("No contact found")
            
    elif choose==5:
        
        if len(contacts) == 0:
            print("No contact found")
            
        else:
            for name,number in contacts.items():
                print(name, ":", number)   
                
                
    elif choose==6:
        
        print("Thank you for using our system")
        break   
    