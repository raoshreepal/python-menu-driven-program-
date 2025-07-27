class Location:
    def __init__(self, city):
        self.city = city

class Warehouse(Location):
    def __init__(self, city, capacity):
        super().__init__(city)
        self.capacity = capacity

class DeliveryCenter(Warehouse):
    def __init__(self, city, capacity, delivery_area):
        super().__init__(city, capacity)
        self.delivery_area = delivery_area

    def status(self):
        print(f"Center in {self.city} | Capacity: {self.capacity} | Area: {self.delivery_area}")

# Object
d = DeliveryCenter("Bangalore", 10000, "South Zone")
d.status()
