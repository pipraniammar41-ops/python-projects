class Student:
    
    def __init__(self,student_id,name,age,course,marks,grade):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.course=course
        self.marks=marks
        self.grade=grade
    
    def show_details(self):
        print("\n----- Student Details -----\n")
        
        print(f"Student id: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"course: {self.course}")
        print(f"marks: {self.marks}")
        print(f"grade: {self.grade}")
        
        print("--------------------------")

class StudentSystem:
    
    def __init__(self):
        self.students = []
    
    def add_student(self,student_id,name,age,course,marks,grade):
        stud=Student(
            student_id,
            name,
            age,
            course,
            marks,
            grade
        )
        
        self.students.append(stud)
        
        print("student added successfully")
        
    def view_student(self):
        if len(self.students) == 0:
            print("No student found")
            return
        print("\nStudent list\n")
        
        for stuud in self.students:
            stuud.show_details()
            
    def search_student(self):
        if len(self.students) == 0:
            print("No student found")
            return
    
        search_name=input("Enter your student id: ")
        
        found=False
        
        for studen in self.students:
            if studen.student_id == search_name:
                studen.show_details()
                found=True
                break
        if not found:
            print("No student found")
        
    def update_student(self):
        if len(self.students)==0:
            print("No student found")
            return
        
        search_idd=input("Enter student id: ")
        
        found=False
        
        for student in self.students:
            
            if student.student_id == search_idd:
                student.name=input("Enter new name: ")
                student.age=input("Enter new age: ")
                student.course=input("Enter new course: ")
                student.marks=input("Enter new marks: ")
                student.grade=input("Enter new grade: ")
                
                print("Student updated successfully")
                
                found=True
                break
        if not found:
            print("No student found")
            
    def delete_student(self):
        if len(self.students)== 0:
            print("student not found")
            return
            
        search_id=input("enter your student id: ")
        
        found=False
        
        for studentt in self.students:
            
            if studentt.student_id==search_id:
                self.students.remove(studentt)
                print("Deleted successfully")
                found=True
                break
            
        if not found:
            print("No student found")
            
    def save_to_file(self):
        file=open("Data.txt",'w')
        
        for student in self.students:
            file.write(
                f"{student.student_id},"
                f"{student.name},"
                f"{student.age},"
                f"{student.course},"
                f"{student.marks},"
                f"{student.grade}\n"
            )
        file.close()
        print("Data saved suseccfully")
        
    def load_from_file(self):
        file=open("Data.txt",'r')
        
        for line in file:
            line=line.strip()
            parts=line.split(",")
            
            studd=Student(
                
                parts[0],
                parts[1],
                int(parts[2]),
                parts[3],
                parts[4],
                parts[5],
                parts[6]
            )
            
            self.students.append(studd)
        file.close()
    
def main():
    
    system=StudentSystem()
    
    try:
        system.load_from_file()
    except:
        print("No previous data found.start with empty students.")
        
    while True:
        
        print("\n Student result management\n")
        print("1. Add student")
        print("2. View student")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Save Data")
        print("7. Exit")
        
        choice=input("Enter your choice: ")
        
        if choice=="1":
            
            studen_id=input("Enter your student id: ")
            name=input("Enter your name: ")
            age=input("Enter your age: ")
            course=input("Enter your course: ")
            marks=input("Enter your marks: ")
            grade=input("Enter yout grade")
            
            system.add_student(
                studen_id,
                name,
                age,
                course,
                marks,
                grade
            )
        elif choice=="2":
            system.view_student()
        elif choice=="3":
            system.search_student()
        elif choice=="4":
            system.update_student()
        elif choice=="5":
            system.delete_student()
        elif choice=="6":
            system.save_to_file()
            print("Data saved succesfully")
            print("Thank your for using our system")
            break
        else:
            print("Invalid choice...")
main()
        
            
            
            
            
        