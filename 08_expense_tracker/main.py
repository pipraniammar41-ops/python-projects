#Expense Tracker

def add_expense():
    name=input("Tell your expense name: ")
    amount=int(input("How much amount you spent: "))
    try:
       with open("Expense.txt","a") as file:
           file.write(f"{name},{amount}\n")
           print("Expense added succesfully")
    except Exception as err:
        print(f"This is an error {err}")
        
def view_expense():
    
    try:
        file = open("Expense.txt", "r")
        data = file.readlines()
    except FileNotFoundError:
        
        print(f"No expense file found.please enter a valid name")
        
    
    for line in data:
        line = line.strip()
        part=line.split(",")
        print(f"{part[0]} - ₹{part[1]}")
    file.close()
           
    
def total_expense():
    
    try:
        file=open("Expense.txt",'r')
        data = file.readlines()
        
    except FileNotFoundError:
        print(f"No expense file found.please enter a valid name")
        
    total=0
        
    for line in data:
        line=line.strip()
        part=line.split(",")
        total += int(part[1])
    print(f"Total Expense: ₹{total}")
        
    file.close()
    
def main():
    while True:
        print("1. Add expenses")
        print("2. View expenses")
        print("3. Total expenses")
        print("4. Exit")
        
        try:
            choice=int(input("Enter your number: "))
        except ValueError:
            print("Please enter a valid number ")
            continue
        
        if choice==1:
            add_expense()
        elif choice==2:
            view_expense()
        elif choice==3:
            total_expense()
        elif choice==4:
            print("Thank you for using our system")
            break
        else:
            print("Please enter a valid number between 1 and 4")
main()
    
        
    
    
    
    
