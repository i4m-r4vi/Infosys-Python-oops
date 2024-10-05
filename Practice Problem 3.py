class Tollbooth:
    def __init__(self):
        self.__no_of_vehicle=0
        self.__total_amount=0

    def get_no_of_vehicle(self):
        return self.__no_of_vehicle
    def get_total_amount(self):
        return self.__total_amount

    def count_vehicle(self):
        self.__no_of_vehicle+=1

    def calculate_amount(self,vehicle_type):
        if vehicle_type.lower()== "car":
            self.__total_amount+=70
        elif vehicle_type.lower()=="bus":
            self.__total_amount+=100
        elif vehicle_type.lower()=="truck":
            self.__total_amount+=150
        else:
            self.__total_amount+=70


    def collect_toll(self,owner_type,vehicle_type):
        self.count_vehicle()
        if str(owner_type).lower() =="non-vip":
            self.calculate_amount(vehicle_type)


c=Tollbooth()
c.collect_toll('non-vip','car')

