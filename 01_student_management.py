#STUDENT MANAGEMENT PROJECT
student = {}

while True:

    print("\n===== Student Result Management =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Find Topper")
    print("4. Average Marks")
    print("5. Count Passed Students")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Student Name: ")
        marks = int(input("Enter Marks: "))

        student[name] = marks
        print(student)

        print("✅ Student Added Successfully!")

    elif choice == 2:

        if len(student) == 0:
            print("No students found.")

        else:
            print("\n===== Students =====")

            for name, marks in student.items():
                print(name, ":", marks)

    elif choice == 3:

        if len(student) == 0:
            print("No students found.")

        else:
            highest_marks = None
            topper = ""

            for name, marks in student.items():
                if highest_marks is None or marks > highest_marks:
                    highest_marks = marks
                    topper = name

            print("\n===== Topper =====")
            print("Name :", topper)
            print("Marks:", highest_marks)
        

    elif choice == 4:
        
         if len(student) == 0:
             print("No students found.")
         else:
             total = 0

             for marks in student.values():
                 total += marks

             print("Average Marks:", total / len(student))
        
        
        
    elif choice == 5:
        
        if len(student) == 0:
            print("No students found.")
        else:
            count = 0

            for marks in student.values():
                 if marks >= 40:
                     count += 1
            print("\n===== Passed Students =====")
            print("Total Passed Students:", count)

    elif choice == 6:
        print("Thank you for using Student Management System.")
        break
    else:
        print("❌ Invalid Choice")


                     







    

