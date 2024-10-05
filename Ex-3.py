class Vehicle:
    def __init__(self):
        vehicle_type=None
        vehicle_id=None
        vehicle_cost=None
        premium_amount=None
        self.__vehicle_type=vehicle_type
        self.__vehicle_id=vehicle_id
        self.__premium_amount=premium_amount
        self.__vehicle_cost=vehicle_cost
    
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
    
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
    
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type
    
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    
    def get_premium_amount(self):
        return self.__premium_amount
    
    def calculate_premium(self):
        if(self.__vehicle_type=="Two Wheeler"):
            self.__premium_amount=((self.__vehicle_cost/100)*2)
            
        elif(self.__vehicle_type=="Four Wheeler"):
            self.__premium_amount=(self.__vehicle_cost/100)*6
        
        print(self.get_premium_amount())

    def display_vehicle_details(self):
        print(f"vehicle_cost-{self.__vehicle_cost} vehicle_type-{self.__vehicle_type}")

theVehicle=Vehicle()
theVehicle.set_vehicle_type("Two Wheeler")
theVehicle.set_vehicle_cost(105000)
theVehicle.calculate_premium()
theVehicle.display_vehicle_details()





    
    
