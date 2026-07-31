class Patient:
    def __init__(self,patient_id,name,age,gender,disease,doctor,appointment_date):
        self.patient_id=patient_id
        self.name=name
        self.age=age
        self.gender=gender
        self.disease=disease
        self.doctor=doctor
        self.appointment_date=appointment_date
        
    def show_details(self):
        print("----- Patient Details -----\n\n")
        print(f"Patient id: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Disease: {self.disease}")
        print(f"Doctor: {self.doctor}")
        print(f"Appointment: {self.appointment_date}\n")
        print("------------")
        
class Hospital:

    def __init__(self):
        self.patients = []

    def add_patient(self, patient_id, name, age, gender, disease, doctor, appointment_date):
        
        patient=Patient(
            patient_id,
            name,
            age,
            gender,
            disease,
            doctor,
            appointment_date
        )
        
        self.patients.append(patient)
        
        print("patient added succesfully")
    

    def view_patients(self):
        
        if len(self.patients) == 0:
            
            print("No patients found.")
            return

        print("\n----- Patient List -----\n")

        for patient in self.patients:
            patient.show_details()


    def search_patient(self):
        if len(self.patients) == 0:
            print("No patient found")
            return
        
        search_id = input("Enter Patient ID to search: ")
        
        found = False
        
        for patient1 in self.patients:
            
            if patient1.patient_id == search_id:
                patient1.show_details()
                found=True
                break
        if found == False:
        # if not found:
            print("Patient not found")
        
    def update_patient(self):
        if len(self.patients) == 0:
            print("No patient found")
            return
        
        search_id = input("Enter patient id to search: ")
        
        found=False
        
        for patient2 in self.patients:
            
            if patient2.patient_id == search_id:
                
                patient2.name = input("Enter new name: ")
                patient2.age = input("Enter new age: ")
                patient2.gender = input("Enter new gender: ")
                patient2.disease = input("Enter new Diesease: ")
                patient2.doctor = input("Enter new doctor: ")
                patient2.appointment_date = input("Enter new date: ")
                
                print("Patient updated succesfully")
                
                found=True
                break
        
        if not found:
            print("Patient not found")
        
            
    def delete_patient(self):
        if len(self.patients) == 0:
            print("No patient found")
            return
        
        search_id=input("Enter your patient id for delete: ")
        
        found=False
        
        for patient3 in self.patients:
            if patient3.patient_id==search_id:
                self.patients.remove(patient3)
                print("Deleted succesfully")
                found=True
                break
        
        if not found:
            print("No patient found")
            
       
    def save_to_file(self):
        file=open("Data.txt",'w')
        
        for patient4 in self.patients:
            
            file.write(
                f"{patient4.patient_id},"
                f"{patient4.name},"
                f"{patient4.age},"
                f"{patient4.gender},"
                f"{patient4.disease},"
                f"{patient4.doctor},"
                f"{patient4.appointment_date}\n"
            )
            
        file.close()
        print("Date saved succesfully")
            
    def load_from_file(self):
        file=open("Data.txt","r")
        
        for line in file:
            line=line.strip()
            parts=line.split(",")
            
            patient = Patient(
                parts[0],
                parts[1],
                int(parts[2]),
                parts[3],
                parts[4],
                parts[5],
                parts[6]
            )
            
            self.patients.append(patient)
        file.close()
    
def main():

    hospital = Hospital()

    try:
        hospital.load_from_file()
    except FileNotFoundError:
        print("No previous data found. Starting with an empty hospital.")

    while True:

        print("\n===== Hospital Management System =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Save Data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = int(input("Enter Patient Age: "))
            gender = input("Enter Gender: ")
            disease = input("Enter Disease: ")
            doctor = input("Enter Doctor Name: ")
            appointment_date = input("Enter Appointment Date: ")

            hospital.add_patient(
                patient_id,
                name,
                age,
                gender,
                disease,
                doctor,
                appointment_date
            )

        elif choice == "2":
            hospital.view_patients()

        elif choice == "3":
            hospital.search_patient()

        elif choice == "4":
            hospital.update_patient()

        elif choice == "5":
            hospital.delete_patient()

        elif choice == "6":
            hospital.save_to_file()

        elif choice == "7":
            hospital.save_to_file()
            print("Data saved successfully.")
            print("Thank you for using Hospital Management System.")
            break

        else:
            print("Invalid choice. Please try again.")
                


main()

        

        

        

        