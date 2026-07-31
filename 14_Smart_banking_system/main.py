from abc import ABC,abstractmethod

class BankAccount(ABC):
    def __init__(self,account_number,holder_name,balance):
        self.account_number=account_number
        self.holder_name=holder_name
        self.__balance=balance
        
    def get_balance(self):
        return self.__balance
    
    def update_balance(self,new_balance):
        self.__balance=new_balance
    

    def deposit(self,amount):
        if amount <=0:
            print("Enter a valid amount")
            return
        self.__balance+=amount
        print(f"{amount} deposited successfully.")
        
        
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def display_details(self):
        pass
        

class SavingAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance):
        super().__init__(account_number, holder_name, balance)
        
    def withdraw(self, amount):
        if amount <=0:
            print("Please enter a valid amount")
            return False
        balance=self.get_balance()
        
        if amount > self.get_balance():
            print("Insufficent balance")
            return False
        
        elif self.get_balance() - amount < 1000:
            print("Minimum maintain balance of 1000 required.")
            return
            
        balance = self.get_balance()
        new_balance = balance - amount
        self.update_balance(new_balance)
        print(f"{amount} withdrawn successfully")
        return
    
    def display_details(self):
        print("Account Details\n")
        
        print(f"Account number: {self.account_number}")
        print(f"Holder name: {self.holder_name}")
        print(f"Balance: {self.get_balance()}\n")
        
class CurrentAccount(BankAccount):
    
    def withdraw(self, amount):
        if amount  <=0:
            print("Please enter a valid amount")
            return False
        
        balance=self.get_balance()
    
    
            
        if amount > self.get_balance():
            print("Insufficeient balance")
            return
        
        balance= self.get_balance()
        new_balance= balance - amount
        self.update_balance(new_balance)
        print(f"{amount} withdrawn successfully")
        return True
    
    def display_details(self):
        print("========== Current Account ==========\n")
        
        print(f"Account number: {self.account_number}")
        print(f"Holder name: {self.holder_name}")
        print(f"Balance: {self.get_balance()}\n")

class BankSystem:
    def __init__(self):
        self.accounts=[]
        
    def create_account(self):
        account_type = input("Enter account type (Savings/Current): ")
        account_number=input("Enter account number:  ")
        holder_name=input("Enter holder name: ")
        initial_balance=float(input("Enter your initial balance"))
        
        for account in self.accounts:
            if account.account_number == account_number:
                print("Account number already exist")
                return
            
        if account_type.lower() == "savings":
            account = SavingAccount(account_number,holder_name,initial_balance)
             
        elif account_type.lower() == "current":
            account = CurrentAccount(account_number, holder_name, initial_balance)

        else:
            print("Invalid account type.")
            return
        
        self.accounts.append(account)
        print("Account created Successfully")
        
    def find_account(self, account_number):

        for account in self.accounts:

            if account.account_number == account_number:
                return account

        return None
    
    def deposit(self):
        account_number= input("Enter account number: ")
        
        amount = float(input("Enter amount: "))
        
        account = self.find_account(account_number)
            
        if account is not None:
            account.deposit(amount)
        else:
            print("Account not found")
    
    def withdraw(self):
        account_number=input("Enter account number: ")
        
        amount = float(input("Enter amount: "))
        
        account=self.find_account(account_number)
    
        if account is not None:
            account.withdraw(amount)
        else: print("Account not found ")
        
    def view_account(self):
        account_number1=input("Enter account number: ")
        
        account=self.find_account(account_number1)
        
        if account is not None:
            account.display_details()
        else:
            print("No account found")
    
    def view_all_accounts(self):
        if len(self.accounts) == 0:
            print("No account found")
            return
        
        for acc in self.accounts:
            acc.display_details()
            
    def transfer(self):
        sender_account = input("Enter sender account number: ")
        receiver_account = input("Enter receiver account number: ")
        amount = float(input("Enter amount to transfer: "))
        
        sender = self.find_account(sender_account)
        receiver = self.find_account(receiver_account)
        
        if sender is None:
            print("No account found")
            return
        
        if receiver is None:
            print("Receiver account not found.")
            return
        
        if sender == receiver:
            
            print("Cannot transfer to the same account.")
            return
        if amount <=0:
            print("Please enter a valid amount.")
            return
        success=sender.withdraw(amount)
        
        if success:
            receiver.deposit(amount)
            print("Transfer completed successfully.")
            
    def delete_account(self):

        account_number = input("Enter account number: ")

        account = self.find_account(account_number)
 
        if account is None:
            print("Account not found.")
            return

        self.accounts.remove(account)
        print("Account deleted successfully.")
        
    def save_accounts(self):

        file = open("accounts.txt", "w")

        for acc in self.accounts:

            if isinstance(acc, SavingAccount):
                account_type = "Savings"
            else:
                account_type = "Current"

            file.write(
                f"{account_type},"
                f"{acc.account_number},"
                f"{acc.holder_name},"
                f"{acc.get_balance()}\n"
            )

        file.close()

        print("Accounts saved successfully.")
    
    def load_accounts(self):

        file = open("accounts.txt", "r")

        for line in file:

            line = line.strip()
            data = line.split(",")

            account_type = data[0]
            account_number = data[1]
            holder_name = data[2]
            balance = float(data[3])

            if account_type == "Savings":
                account = SavingAccount(
                    account_number,
                    holder_name,
                    balance
                )

            else:
                account = CurrentAccount(
                    account_number,
                    holder_name,
                    balance
                )

            self.accounts.append(account)

        file.close()

        print("Accounts loaded successfully.")
        
def main():
    bank=BankSystem()
    
    try:
        bank.load_accounts()
    except:
        print("No data found")
        
    while True:
        print("========== SMART BANKING SYSTEM ==========\n")
        
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Account")
        print("6. View All Accounts")
        print("7. Delete Account")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice=="1":
            bank.create_account()
        elif choice=="2":
            bank.deposit()
        elif choice=="3":
            bank.withdraw()
        elif choice=="4":
            bank.transfer()
        elif choice=="5":
            bank.view_account()
        elif choice=="6":
            bank.view_all_accounts()
        elif choice=="7":
            bank.delete_account()
        elif choice=="8":
            bank.save_accounts()
            print("Accounts saved successfully.")
            print("Thank you for using our system")
            break
        else:
            print("Invalid choice")
            
main()
        
            
            
        
            
            
        
            
    
                
                
        