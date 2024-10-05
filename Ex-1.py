class Vehicle:
    def _init_(self):
        fuel_left=0
        mileage=0
        self.fuel_left=fuel_left
        self.mileage=mileage
        
    def identify_distance_that_can_be_travelled(self):
        if(self.fuel_left>5):
            without_reservefuel=self.fuel_left-5
            remaining_distance=without_reservefuel*self.mileage
            return remaining_distance
        elif(self.fuel_left<=5):
            return 0
        
    def identify_distance_travelled(self,initial_fuel):
        if(initial_fuel>self.fuel_left):
            distance_traveled=(initial_fuel-self.fuel_left)*self.mileage
            return distance_traveled


Car=Vehicle()
Car.fuel_left=10
Car.mileage=20
reamining_fuel=Car.identify_distance_that_can_be_travelled()
distance_travel=Car.identify_distance_travelled(25)
print("The Reamining Distance:",reamining_fuel)
print("The Distance Traveled:",distance_travel)