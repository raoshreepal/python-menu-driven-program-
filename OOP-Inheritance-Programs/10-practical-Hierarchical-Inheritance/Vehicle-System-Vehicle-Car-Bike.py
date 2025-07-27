class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def info(self):
        print(f"Car: {self.brand} {self.model}")

class Bike(Vehicle):
    def __init__(self, brand, cc):
        super().__init__(brand)
        self.cc = cc

    def info(self):
        print(f"Bike: {self.brand} {self.cc}cc")

# Objects
c = Car("Hyundai", "i20")
b = Bike("Yamaha", 150)

c.info()
b.info()
