class Vehicle:
    def __init__(self, brand, model, dimensions):
        self.brand = brand
        self.model = model
        self.dimensions = dimensions  # (length, width)

    def area(self):
        return self.dimensions[0] * self.dimensions[1]

class Car(Vehicle):
    def display(self):
        print(f"{self.brand} {self.model} Area: {self.area()} sq.ft.")

v = Car("Toyota", "Innova", (15, 6))
v.display()
 