#Student record system

def add_student():

    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))

    file = open("students.txt", "a")
    file.write(f"{name},{marks}\n")
    file.close()

    print("✅ Student Added Successfully")

def view_students():
    d=open("students.txt")
    f=d.read()
    print(f)
    d.close()
    print("Your file has been viewed succesfully")

def search_student():
    search_name = input("Enter student name to search: ")

    file = open("students.txt", "r")

    found = False

    for line in file:
        line = line.strip()  #Removes the hidden \n
        parts = line.split(",") #Split Name and marks in list

        if search_name == parts[0]:
            print(f"Student: {parts[0]}")
            print(f"Marks: {parts[1]}")

            found = True
            break

    file.close()

    if found == False:
        print("❌ Student not found.")


def update_marks():
    update = input("Enter student name to update marks: ")
    new_marks = input("Enter new marks: ")

    file = open("students.txt", "r")


    students = []
    found = False

    for line in file:
        line = line.strip()
        parts = line.split(",")

        if update == parts[0]:
            students.append(f"{parts[0]},{new_marks}\n")
            found = True

        else:
            students.append(line + "\n")

    file.close()

    file = open("students.txt", "w")
    file.writelines(students)
    file.close()

    if found:
        print("✅ Marks Updated Successfully")
    else:
        print("❌ Student Not Found")
    
def delete_student():
    del_student=input("Whats the name of student you want to delete: ")
    file=open("students.txt", 'r')
    students=[]
    found=False
    
    for line in file:
        line = line.strip()
        parts=line.split(",")
        
        if del_student == parts[0]:
            found=True
        else:
            students.append(line + "\n")
            
    file.close()
    file=open("students.txt",'w')
    file.writelines(students)
    file.close()
    
    if found:
        print("student deleted succesfully")
    else:
        print("Student not found")


def menu():
    while True:
        print("1. Add student")
        print("2. View student")
        print("3. Search student")
        print("4. Update marks")
        print("5. Delete student")
        print("6. Exit")
        
        try:
            choice=int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        
        
        if choice==1:
            add_student()
        elif choice==2:
            view_students()
        elif choice==3:
            search_student()
        elif choice==4:
            update_marks()
        elif choice==5:
            delete_student()
        elif choice==6:
            print("Thank you for using our system.")
            break
            
        else:
            print("Please enter a valid number between 1 and 6.")
            
menu()




     













    
 
    


        
            
    
    
