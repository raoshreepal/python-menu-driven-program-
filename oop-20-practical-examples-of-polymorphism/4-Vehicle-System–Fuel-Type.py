#Definition: Vehicles respond to fuel_type() polymorphically.

class Vehicle:
    def fuel_type(self):
        pass

class Car(Vehicle):
    def fuel_type(self):
        return "Petrol"

class Truck(Vehicle):
    def fuel_type(self):
        return "Diesel"

for v in [Car(), Truck()]:
    print(v.fuel_type())
