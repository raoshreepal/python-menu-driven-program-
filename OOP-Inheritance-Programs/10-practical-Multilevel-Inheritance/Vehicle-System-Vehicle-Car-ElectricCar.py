class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_range):
        super().__init__(brand, model)
        self.battery_range = battery_range

    def specs(self):
        print(f"{self.brand} {self.model} | Range: {self.battery_range} km")

# Object
e_car = ElectricCar("Tesla", "Model 3", 500)
e_car.specs()
