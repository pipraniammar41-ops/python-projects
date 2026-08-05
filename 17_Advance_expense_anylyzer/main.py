from expense import expenses

def add_expense():
    category1=input("Enter your category: ")
    Amount1=int(input("Enter your amount: "))
    Description1=input("Enter your describtion: ").title()
    Payment_method1=input("Enter your payment method: ").title()
    
    new_expense={
        "category" : category1,
        "amount" : Amount1,
        "description" : Description1,
        "payment" : Payment_method1
    }
    expenses.append(new_expense)
    
    print("Expense added successfully!")

def View_Expenses():
    if len(expenses)==0:
        print("No expenses found.")
        return
        
    else:
        print("\n========== All Expenses ==========\n")
        
        for expense in expenses:
            print(f"Category    : {expense['category']}")
            print(f"Amount      : ₹{expense['amount']}")
            print(f"Description : {expense['description']}")
            print(f"Payment     : {expense['payment']}")
            print("-" * 35)

def search_Expenses():
    
    if len(expenses)==0:
        print("No category found")
        return
        
    categoryy=input("Enter your category: ")
    
    # for expense in expenses:
    #     if expense["category"] == categoryy:
    #         print(expense)
    
    filtered=filter(lambda expense: expense["category"] == categoryy,expenses)
    found=False
    for expense in filtered:
        found=True
        print(expense)
    
    if not found:
        
        print("Category not found")
        

def Total_expenses():
    if len(expenses)==0:
        print("No expense found")
        return
        
        
    total=0
    for expense in expenses:
        total+=expense["amount"]
        
  
    #advance python
    # total = sum(expense["amount"] for expense in expenses)
    
    print(f"Total expense is {total}")
    
    categoryy=input("Enter your specific category: ")
    
    total=0
    found=False
    for expense in expenses:
        if expense["category"]==categoryy:
            total+=expense["amount"]
            found=True
            
    if found:
        print(f"Total {categoryy} expense = {total}")
    else:
        print("Category not found")
        
        
    # Advanced Python
    # category_total = sum(expense["amount"]for expense in expenses if expense["category"] == categoryy)

    # if category_total > 0:
    #     print(f"Total {categoryy} expense = ₹{category_total}")
    # else:
    #     print("Category not found")
    
def Highest_Expense():
    if len(expenses)==0:
        print("No expense found")
        return
        
    highest=expenses[0]
    
    for expense in expenses:
        if expense["amount"]>highest["amount"]:
            highest=expense
            
    # highest1=max(expenses,key=lambda expense: expense["amount"])
            

    print(f"Category : {highest['category']}")
    print(f"Amount : {highest['amount']}")
    print(f"Description : {highest['description']}")
    print(f"Payment : {highest['payment']}")

def Lowest_expense():
    if len(expenses)==0:
        print("No expense found")
        return
    
    # lowest=expenses[0]
    # for expense in expenses:
    #     if expense["amount"] < lowest["amount"]:
    #         lowest=expense
    
    #Advance python
    lowest=min(expenses,key=lambda expense:expense["amount"])
    
    #this is common in both
    print(f"Category : {lowest['category']}")
    print(f"Amount : {lowest['amount']}")
    print(f"Description : {lowest['description']}")
    print(f"Payment : {lowest['payment']}")
    

def Sort_expenses():
    if len(expenses) == 0:
        print("No expense found")
        return

    print("\n1. Low to High")
    print("2. High to Low")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sorted_expenses = sorted(expenses,key=lambda expense: expense["amount"])

    elif choice == 2:
        sorted_expenses = sorted(expenses,key=lambda expense: expense["amount"],reverse=True)

    else:
        print("Invalid Choice")
        return

    print("\n====== Sorted Expenses ======\n")

    for expense in sorted_expenses:
        print(f"Category    : {expense['category']}")
        print(f"Amount      : ₹{expense['amount']}")
        print(f"Description : {expense['description']}")
        print(f"Payment     : {expense['payment']}")
        print("-" * 35)
    
def Delete_expense():
    if len(expenses) == 0:
        print("No expense found")
        return

    print("\n========== All Expenses ==========\n")

    # Display all expenses with serial numbers
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['category']} - ₹{expense['amount']}")

    deletee = int(input("\nEnter expense number to delete: "))

    # Validate input
    if deletee < 1 or deletee > len(expenses):
        print("Invalid expense number")
        return

    # Delete the selected expense
    deleted_expense = expenses.pop(deletee - 1)

    print("\nExpense Deleted Successfully!")
    print(f"Deleted: {deleted_expense['category']} - ₹{deleted_expense['amount']}")

def update_expense():
    if len(expenses) == 0:
        print("No expense found")
        return

    print("\n========== All Expenses ==========\n")

    # Display all expenses with serial numbers
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['category']} - ₹{expense['amount']}")
        
        
        
    update=int(input("Enter your number: "))
    
    if update < 1 or update > len(expenses):
        print("Invalid expense number")
        return
    
    expense= expenses[update -1]
    
    print("\nWhat do you want to update?")
    print("1.Category")
    print("2.Amount")
    print("3.Description")
    print("4.Payment")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        expense["category"] = input("Enter new category: ")

    elif choice == 2:
        expense["amount"] = int(input("Enter new amount: "))

    elif choice == 3:
        expense["description"] = input("Enter new description: ")

    elif choice == 4:
        expense["payment"] = input("Enter new payment method: ")

    else:
        print("Invalid Choice")
        return
    
    print("\nExpense updated succesfully")
    
def save_file():

    file = open("Data.txt", "w")

    for expense in expenses:

        file.write(
            f"{expense['category']},{expense['amount']},{expense['description']},{expense['payment']}\n"
        )

    file.close()

    print("Expenses saved successfully.")
    
def load_file():

    try:
        file = open("Data.txt", "r")

        expenses.clear()

        for line in file:

            line = line.strip()

            category, amount, description, payment = line.split(",")

            expense = {
                "category": category,
                "amount": int(amount),
                "description": description,
                "payment": payment
            }

            expenses.append(expense)

        file.close()

        print("Expenses loaded successfully.")

    except FileNotFoundError:
        print("No saved file found.")
    
def main():

    load_file()

    while True:

        print("\n===== Expense Analyzer =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Total Expense")
        print("5. Highest Expense")
        print("6. Lowest Expense")
        print("7. Sort Expenses")
        print("8. Delete Expense")
        print("9. Update Expense")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_expense()

        elif choice == 2:
            View_Expenses()

        elif choice == 3:
            search_Expenses()

        elif choice == 4:
            Total_expenses()


        elif choice == 5:
            Highest_Expense()

        elif choice == 6:
            Lowest_expense()

        elif choice == 7:
            Sort_expenses()

        elif choice == 8:
            Delete_expense()

        elif choice == 9:
            update_expense()

        elif choice == 10:
            save_file()
            print("Thank you for using Expense Analyzer.")
            break

        else:
            print("Invalid Choice")
main()
        


    
    
    
     
        
    
    
        
        
        
    
        

        
            