#Notes manager
#File and exception handling
from datetime import datetime

def add_note():
    note=input("Enter your note: ")
    current_time = datetime.now()
    formatted_time = current_time.strftime("%d-%m-%Y %I:%M %p")
    a=open("note.txt",'a')
    # a.write(note + "\n")
    a.write(f"[{formatted_time}] {note}\n")
    a.close()
    print("✅ Note Added Successfully")
    
def view_notes():
    a = open("note.txt", "r")
    content=a.read()
    print(content)
    a.close()
    print("Your note has been viewed")
    
def clear_notes():
    a=open("note.txt","w")
    a.close()
    print("All notes cleared")
    
def menu():

    while True:

        print("===== NOTES MANAGER =====")

        print("1. Add Note")
        print("2. View Notes")
        print("3. Clear Notes")
        print("4. Exit")
       
        try:   
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number. ")
            continue

        if choice==1:
            add_note()
        elif choice==2:
            view_notes()
        elif choice==3:
            clear_notes()
        elif choice==4:
            print("Thank you for using our Notes manager.")
            break
        else:
            print("Invalid choice.Please choose between 1 and 4.")
        
menu()
            
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     Notes Manager

# 1. Add Note
# 2. View Notes
# 3. Clear Notes
# 4. Exit