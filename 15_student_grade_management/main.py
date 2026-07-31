from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,student_id,name):
        self.student_id=student_id
        self.name=name
    
    
        
    @abstractmethod
    def display_details(self):
        pass

class Student(Person):
    def __init__(self, student_id, name,marks):
        super().__init__(student_id, name)
        self.__marks=marks
        
    def get_marks(self):
        return self.__marks
    
    def update_marks(self,new_marks):
        self.__marks=new_marks
        
    def display_details(self):
        print("Student details\n")
        
        print(f"Student id: {self.student_id}")
        print(f"Student name: {self.name}")
        print(f"Marks: {self.__marks}")
        print(f"Grade: {self.calculate_grade()}")
        
        
    def calculate_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >=75:
            return "B"
        elif self.__marks >=60:
            return "C"
        elif self.__marks >=40:
            return "D"
        
        else:
            return "Fail"
        
class StudentSystem():
    def __init__(self):
        self.students=[]
        
    def find_student(self,student_id):
        for studen in self.students:
            if studen.student_id == student_id:
                return studen
            
        return None
        
    def add_student(self):
        student_id1=input("Enter your id: ")
        name1=input("Enter your name: ")
        marks1=int(input("Enter your marks: "))
        
        studen1=self.find_student(student_id1)
        if studen1 is not None:
            print("Student already exists")
            return
        student = Student(student_id1, name1, marks1)
        self.students.append(student)
    
        print("Student added successfully.")
        
    def view_students(self):
        if len(self.students)==0:
            print("No student data found.")
            return
        for student in self.students:
            student.display_details()
    
    def search_student(self):
        student_id2=input("Enter your id: ")
        
        studen2=self.find_student(student_id2)
        if studen2 is not None:
            studen2.display_details()
        else:
            print("Student not found")
            
    def update_student_marks(self):
        student_id3=input("Enter your id: ")
        
        
        studenn=self.find_student(student_id3)
        
        if studenn is not None:
            
            new_marks=int(input("enter your marks"))
            studenn.update_marks(new_marks)
            print("Marks updated succesfully")
        else:
            print("Student not found")
        
    def delete_student(self):
        student_id4=input("enter your id: ")
        
        student=self.find_student(student_id4)
        
        if student is not None:
            self.students.remove(student)
            print("Account deleted successfully.")
        else:
            print("No student found")
    
    def find_topper(self):
        if len(self.students) == 0:
            print("No students found.")
            return

        topper = self.students[0]

        for student in self.students:
            if student.get_marks() > topper.get_marks():
                topper = student

        print("\nTopper Details")
        print("-" * 30)
        topper.display_details()
        
    def calculate_average(self):
        if len(self.students)==0:
            print("No student found")
            return
        
        total_marks=0
        
        for student in self.students:
            total_marks+=student.get_marks()
            
        average= total_marks/len(self.students)
        print(f"Average marks: {average}")
    
    def save_student(self):
        file=open("Data.txt",'w')
        
        for student in self.students:
            line = f"{student.student_id},{student.name},{student.get_marks()}\n"
            file.write(line)
            
        file.close()
            
        print("Student data saved successfully")
    
    def load_students(self):
        try:
            with open("Data.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    student = Student(
                        data[0],
                        data[1],
                        int(data[2])
                    )

                    self.students.append(student)

            print("Student data loaded successfully.")

        except FileNotFoundError:
            print("No saved student data found.")

def main():
    system = StudentSystem()

    system.load_students()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Find Topper")
        print("7. Calculate Average")
        print("8. Save Students")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.add_student()

        elif choice == "2":
            system.view_students()

        elif choice == "3":
            system.search_student()

        elif choice == "4":
            system.update_student_marks()

        elif choice == "5":
            system.delete_student()

        elif choice == "6":
            system.find_topper()

        elif choice == "7":
            system.calculate_average()

        elif choice == "8":
            system.save_students()

        elif choice == "9":
            system.save_students()
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid Choice. Please try again.")


main()
            
       
            
            
        
            

            
            
        
        
        
        
        
            
        
        
        
        
        
# add_student()
# view_students()
# search_student()
# update_student_marks()
# delete_student()
# find_topper()
# calculate_average()
# save_students()
# load_students()
        
        