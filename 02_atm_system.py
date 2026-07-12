#ATM system

balance = 10000

while True:
    print("ATM Menu")
    print("1. Check balance")
    print("2. Deposite")
    print("3. widhraw")
    print("4. exit")
    
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Your current balance is ₹", balance)
    
    elif choice==2:
        amount=int(input("Enter amount to deposite: "))
        balance+= amount
        print(amount, "Deposited succesfully")
        print(f"Your total balance is {balance}" )
    
    elif choice==3:
        amount_1=int(input("Enter amount to withdraw: "))
        if amount_1 <= balance:
            balance-=amount_1
            print(amount_1, "Withdrawed succesfully")
            print(f"your total balance is {balance}")
        else:
            print("Insufficeint Blance")
    else:
        print("Thank you")
        
        
        
            
        
        
