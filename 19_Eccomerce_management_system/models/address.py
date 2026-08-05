class Address:
    def __init__(self,address_id,full_name,phone,house,area,city,state,pincode,country):
        self.address_id=address_id
        self.full_name=full_name
        self.phone=phone
        self.house=house
        self.area=area
        self.city=city
        self.state=state
        self.pincode=pincode
        self.country=country
    
    def display(self):
        
        print("\n========== ADDRESS ==========\n")

        print(f"Name      : {self.full_name}")
        print(f"Phone     : {self.phone}")
        print(f"House No. : {self.house}")
        print(f"Area      : {self.area}")
        print(f"City      : {self.city}")
        print(f"State     : {self.state}")
        print(f"Pincode   : {self.pincode}")
        print(f"Country   : {self.country}")

        print("\n=============================")
        
        
    def update(self,full_name,phone,house,area,city,state,pincode,country):
        
        self.full_name = full_name
        self.phone = phone
        self.house = house
        self.area = area
        self.city = city
        self.state = state
        self.pincode = pincode
        self.country = country
        
        print("Address updated successfully.")
 
        
    def validate(self):
        if len(str(self.pincode)) != 6:
            print("Invalid Pincode")
            return False
        
        if len(str(self.phone)) != 10:
            print("Invalid Phone Number")
            return False
        
        return True
    
    
        



    
        
        