class BankAccount:

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        
        if amount > 0:
            
            
            self.balance += amount
            print("Amount deposited successfully.")
            return True

        print("Invalid deposit amount.")
        return False

    def withdraw(self, amount):
        
        if amount <= 0:
            
            print("Invalid withdrawal amount.")
            return False

        if amount > self.balance:
            
            print("Insufficient balance.")
            return False

        self.balance -= amount
        print("Amount withdrawed successfully.")
        return True

    def show_detail(self):
        print("\n===== Account Details =====")
        print(f"Account Number : {self.account_number}")
        print(f"Holder Name    : {self.holder_name}")
        print(f"Balance        : ₹{self.balance}")
        
def create_account():
    Account_number = int(input("Enter your account number: "))
    Holder_name = input("Enter your name: ")
    Initial_Balance = int(input("Enter your balance: "))

    
    file = open("Total.txt", "r")
    data = file.readlines()

    for line in data:
        part = line.strip().split(",")

        if Account_number == int(part[0]):
            print("Account already exists. Please use another account number.")
            file.close()
            return

    file.close()

    
    account = BankAccount(Account_number, Holder_name, Initial_Balance)

    
    file = open("Total.txt", "a")
    file.write(f"{account.account_number},{account.holder_name},{account.balance}\n")
    file.close()

    print("Account created successfully.")
        
def deposit_money():
    Account_number = int(input("Enter account number: "))
    Deposit_amount = int(input("Enter amount to deposit: "))

    file = open("Total.txt", "r")
    data = file.readlines()

    updated_data = []
    found = False

    for line in data:

        line = line.strip()
        part = line.split(",")

        if Account_number == int(part[0]):

            account = BankAccount(
                int(part[0]),
                part[1],
                int(part[2])
            )

            account.deposit(Deposit_amount)

            updated_data.append(
                f"{account.account_number},{account.holder_name},{account.balance}\n"
            )

            found = True

        else:
            updated_data.append(line + "\n")

    file.close()

    if found:

        file = open("Total.txt", "w")

        for line in updated_data:
            file.write(line)

        file.close()

        # print("Amount deposited successfully.")

    else:
        print("Account not found.")
    
def withdraw_money():
    Account_number=int(input("Enter your account number: "))
    widhraw_amount= int(input("Enter your amount to widhraw: "))
    
    file=open("Total.txt",'r')
    data=file.readlines()
    file.close()
    
    updated_data=[]
    found=False
    
    for line in data:
        line=line.strip()
        part=line.split(",")
        
        if Account_number == int(part[0]):
            found=True
            Acc=BankAccount(
                int(part[0]),
                part[1],
                int(part[2]),
            )
            
            success = Acc.withdraw(widhraw_amount)
            
            if success:
                updated_data.append(f"{Acc.account_number},{Acc.holder_name},{Acc.balance}\n")
                found=True
            else:
                updated_data.append(line + "\n")
                
        
        else:
            updated_data.append(line + "\n")
    file.close()
    
    if found:
        file=open("Total.txt",'w')
        
        for line in updated_data:
            file.write(line)
            
        file.close()
        # print("Amount Withdrawed succesfully")
        
    else:
        print("Account not found")
        
def search_account():
    account_number=int(input("Enter your account number: "))
    
    file=open("Total.txt",'r')
    data=file.readlines()
    file.close()
    
    
    for line in data:
        line=line.strip()
        part=line.split(",")
        
        if account_number == int(part[0]):
            account=BankAccount(
                int(part[0]),
                part[1],
                int(part[2]),
            )
            
            account.show_detail()
            return
        
    print("Account not found")
            
def view_accounts():
    file=open("Total.txt",'r')
    data=file.readlines()
    file.close()
    
    if not data:
        print("No accounts found")
        return
        
    
    for line in data:
        line=line.strip()
        part=line.split(",")
        
        account=BankAccount(
            int(part[0]),
            part[1],
            int(part[2]),
        )
        
        account.show_detail()
        
def delete_account():
    account_number=int(input("Enter your account number: "))
    
    file=open("Total.txt",'r')
    data=file.readlines()
    file.close()
    
    updated_data=[]
    found=False
    
    for line in data:
        line=line.strip()
        part=line.split(",")
        
        if account_number == int(part[0]):
            found=True
        else:
            updated_data.append(line + "\n")
            
    if found:
        file = open("Total.txt", "w")

        for line in updated_data:
            file.write(line)
        file.close()
        print("Account deleted successfully.")
    else:
        print("Account not found")
        
            
def main():
    while True:
        print("==== Bank Management System ====")
        
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Search Account")
        print("5. View All Account")
        print("6. Delete Account")
        print("7. Exit")
        
        try:
            choice=int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number")
            continue
            
        
        if choice==1:
            create_account()
        elif choice==2:
            deposit_money()
        elif choice==3:
            withdraw_money()
        elif choice==4:
            search_account()
        elif choice==5:
            view_accounts()
        elif choice==6:
            delete_account()
        elif choice==7:
            print("Thank you for using our system")
            break
        else:
            print("please enter a valid number between 1 and 7.")
            
main()
            
            
            
        
        
        
    
        
         
        
        
                
                
            
            
    
        
        
        
    
            
    
    
    

    

    

    
    

    

    

        
        