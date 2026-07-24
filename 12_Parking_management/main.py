# Start Program
#       │
#       ▼
# Create Parking Lot
#       │
#       ▼
# Menu
#       │
#       ├──────── Park Vehicle
#       │
#       ├──────── Exit Vehicle
#       │
#       ├──────── Show Available Slots
#       │
#       ├──────── Show Parked Vehicles
#       │
#       └──────── Exit

class ParkingLot:

    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.available_slots = total_slots
        self.parked_vehicles = {}
        
    def park_vehicle(self,vehicle_obj):
        if self.available_slots == 0:
            print("No slots available")
            return
        
        if vehicle_obj.vehicle_number in self.parked_vehicles:
            print("Vehicle is already parked.")
            return
         
        self.parked_vehicles[vehicle_obj.vehicle_number] = vehicle_obj
        self.available_slots-=1
        
        print("Vehicle parked successfully.")

class Vehicle:
    
    def __init__(self,vehicle_number,owner_name,vehicle_type):
        self.vehicle_number=vehicle_number
        self.owner_name=owner_name
        self.vehicle_type=vehicle_type
        
    def remove_vehicle(self, vehicle_number):

        if vehicle_number not in self.parked_vehicles:
            print("No vehicle found.")
            return

        del self.parked_vehicles[vehicle_number]
        self.available_slots += 1

        print("Vehicle removed successfully.")
        
    def show_parked_data(self):
        print(f"Vehicle number: {self.vehicle_number}")
        print(f"Owner: {self.owner_name}")
        print(f"Type: {self.vehicle_type}")
            
            
    

       


            
        
            
        
            
        
        
        
         
        
    