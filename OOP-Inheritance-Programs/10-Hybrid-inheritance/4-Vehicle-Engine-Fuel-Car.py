class Vehicle:
    def __init__(self, model):
        self.model = model

class Engine(Vehicle):
    def __init__(self, model, power):
        super().__init__(model)
        self.power = power

class Fuel:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

class Car(Engine, Fuel):
    def __init__(self, model, power, fuel_type):
        Engine.__init__(self, model, power)
        Fuel.__init__(self, fuel_type)

    def show_info(self):
        print(f"Car: {self.model}, Power: {self.power}hp, Fuel: {self.fuel_type}")

c = Car("Creta", 120, "Petrol")
c.show_info()
