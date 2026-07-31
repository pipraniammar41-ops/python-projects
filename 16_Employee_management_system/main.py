from abc import ABC,abstractmethod

class Head(ABC):
    def __init__(self,employee_id,employee_name,employee_role,salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.employee_role=employee_role
        self.__salary=salary
        
    def get_salary(self):
        return self.__salary
    
    def update_salary(self,new_salary):
        self.__salary=new_salary
        
    @abstractmethod
    def display_details(self):
        pass

class Employee(Head):
    def __init__(self, employee_id, employee_name, employee_role, salary):
        super().__init__(employee_id, employee_name, employee_role, salary)
        
    
    
        
    def display_details(self):
        print("Employee details\n")
        
        print(f"Employee id: {self.employee_id}")
        print(f"Employee name: {self.employee_name} ")
        print(f"Employee role: {self.employee_role}")
        print(f"Employee salary: {self.get_salary()}")
        
class EmployeeSystem():
    def __init__(self):
        self.employees= []
        
    def find_employee(self,employee_id1):
        
        for employ in self.employees:
            if employ.employee_id==employee_id1:
                return employ
            
        return None
    
    def add_employee(self):
        employ_id=input("Enter your id: ")
        
        employee1=self.find_employee(employ_id)
        
        if employee1 is not None:
            print("Employee id already exist.")
            return
        
        employe_name=input("Enter your name: ")
        employe_role=input("Enter your role")
        employe_salary=float(input("Enter your salary: "))
        
        employee1=Employee(
            employ_id,
            employe_name,
            employe_role,
            employe_salary
        )
        
        self.employees.append(employee1)
        
    def view_employee(self):
        if len(self.employees)==0:
            print("No employee found")
            return
        
        for employ in self.employees:
            employ.display_details()
            
        print("Employees viewed succesfully.")
        return
        
    def search_employee(self):
        employee_id = input("Enter Employee ID: ")

        employee = self.find_employee(employee_id)

        if employee is None:
            print("Employee not found.")
            return

        employee.display_details()
        
    def update_salary(self):
        employ_id=input("enter your id: ")
        
        employ=self.find_employee(employ_id)
        
        if employ is None:
            print("Employee id not found")
            return
        
        new_salary=float(input("enter your new salary."))
        employ.update_salary(new_salary)
        print("Salary updated successfully")
        
    def delete_employee(self):
        employee_id=input("Enter your id: ")
        
        employ=self.find_employee(employee_id)
        
        if employ is None:
            print("Employee not found")
            return
            
        self.employees.remove(employ)
        print("Employee removed successfully")
        
    
    def highest_paid_employee(self):
        if len(self.employees) == 0:
            print("No employees found.")
            return

        highest = self.employees[0]

        for employee in self.employees:

            if employee.get_salary() > highest.get_salary():
                highest = employee

        print("\nHighest Paid Employee")
        highest.display_details()
    
    def average_salary(self):
        if len(self.employees) == 0:
            print("No employees found.")
            return
        total_salary=0
        
        for employee in self.employees:
            total_salary+=employee.get_salary()
            
        average=total_salary/len(self.employees)
        print(f"Average salary: {average}")
    
    def save_employees(self):
        
        file=open("Data.txt",'w')
        
        for employe in self.employees:
            data=(
                f"{employe.employee_id},"
                f"{employe.employee_name},"
                f"{employe.employee_role},"
                f"{employe.get_salary()}\n"
            )
            file.write(data)
        
        file.close()
        print("Employees saved successfully.")
        
    def load_employess(self):
        with open("Data.txt","r") as file:
            for line in file:
                line=line.strip().split(",")
                
                employ=Employee(
                    line[0],
                    line[1],
                    line[2],
                    float(line[3])
                    
                    
                )
                
                self.employees.append(employ)
        print("Employees loaded successfully.")
        
def main():
    employee_system = EmployeeSystem()

    employee_system.load_employess()

    while True:

        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Salary")
        print("5. Delete Employee")
        print("6. Highest Paid Employee")
        print("7. Average Salary")
        print("8. Save Employees")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee_system.add_employee()

        elif choice == "2":
            employee_system.view_employee()

        elif choice == "3":
            employee_system.search_employee()

        elif choice == "4":
            employee_system.update_salary()

        elif choice == "5":
            employee_system.delete_employee()

        elif choice == "6":
            employee_system.highest_paid_employee()

        elif choice == "7":
            employee_system.average_salary()

        elif choice == "8":
            employee_system.save_employees()

        elif choice == "9":
            employee_system.save_employees()
            print("Thank you for using Employee Management System.")
            break

        else:
            print("Invalid Choice. Please try again.")


main()
            
                
            
        
        
            
        
        
             
        
        
        
        
                
        
        
            







# EmployeeSystem

# __init__()

# find_employee()

# add_employee()

# view_employees()

# search_employee()

# update_salary()

# delete_employee()

# highest_paid_employee()

# average_salary()

# save_employees()

# load_employees()