#Library management system

def add_book():
    name=input("Enter Borrower's name: ")
    book=input("Enter  book name: ")
    
    with open("library.txt",'a') as file:
        file.write(f"{name},{book}\n")
    print("Book added succesfully")
        
def view_books():
    try:
        file=open("library.txt",'r')
        data=file.readlines()
    except FileNotFoundError:
        print("Please enter a valid file name")
        return
    
    for line in data:
        line=line.strip()
        part=line.split(",")
        print(f"Borrower: {part[0]} | Book: {part[1]}")
    file.close()
    
def search_book():
    search_name=input("Enter your name: ")
    try:
        file=open("library.txt",'r')
        data=file.readlines()
        
    except FileNotFoundError:
        print("Please enter a valid file name")
    
    found=False
    for line in data:
        line=line.strip()
        part=line.split(",")
        
        if search_name == part[0]:
            print(f"Borrower: {part[0]} | Book: {part[1]}")
            found=True
            break
    if not found:
        print("Borrower not found")
    file.close()       
        
def update_book():
    search_name = input("Enter Borrower's Name: ")
    new_book = input("Enter New Book Name: ")

    try:
        file = open("library.txt", "r")
        data = file.readlines()
        file.close()
    except FileNotFoundError:
        print("Library file not found.")
        return

    updated_data = []
    found = False

    for line in data:
        line = line.strip()
        part = line.split(",")

        if search_name == part[0]:
            updated_data.append(f"{part[0]},{new_book}\n")
            found = True
        else:
            updated_data.append(line + "\n")

    if found:
        file = open("library.txt", "w")

        for line in updated_data:
            file.write(line)

        file.close()
        print("Book updated successfully.")

    else:
        print("Borrower not found.")
    
    
def delete_book():
    delete_name=input("enter your name to delete: ")
    
    try:
        file=open("library.txt",'r')
        data=file.readlines()
    except FileNotFoundError:
        print("File name not found..")
        
    updated_data = []
    found=False
    
    for line in data:
        line=line.strip()
        part=line.split(",")
        
        if delete_name == part[0]:
            found=True
        else:
            updated_data.append(line + "\n")
            
    if found:
        
        file=open("library.txt",'w')
        for line in updated_data:
            file.write(line)
        file.close()
        print("Borrower name deleted successfully")
    
    else:
        print("Borrower not found")
    file.close()
def main():
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            add_book()

        elif choice == 2:
            view_books()

        elif choice == 3:
            search_book()

        elif choice == 4:
            update_book()

        elif choice == 5:
            delete_book()

        elif choice == 6:
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Please enter a number between 1 and 6.")

main()

        
        
        
        
            
    
    
    
        
        
    


    




    


    
