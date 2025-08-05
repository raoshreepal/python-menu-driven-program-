'''
🔹Scenario: Vehicles are rented for days; discounts apply after 5 days, and we track availability.
🔹Definition: Polymorphism via rental_cost() method; classes add different pricing logic.
'''
class Vehicle:
    def __init__(self, name, available=True):
        self.name = name
        self.available = available

    def rental_cost(self, days):
        raise NotImplementedError("Subclass must implement rental_cost")

class Bike(Vehicle):
    def rental_cost(self, days):
        rate = 100
        discount = 0.1 if days > 5 else 0
        return days * rate * (1 - discount)

class Car(Vehicle):
    def rental_cost(self, days):
        rate = 500
        discount = 0.15 if days > 5 else 0
        return days * rate * (1 - discount)

class SUV(Vehicle):
    def rental_cost(self, days):
        rate = 800
        if days > 7:
            return days * rate - 1000  # Flat discount
        return days * rate

rental_list = {
    "User1": Bike("Bajaj Pulsar", available=True),
    "User2": Car("Hyundai i20", available=True),
    "User3": SUV("XUV700", available=False)
}

days_requested = {
    "User1": 3,
    "User2": 6,
    "User3": 8
}

for user, vehicle in rental_list.items():
    days = days_requested[user]
    print(f"\n{user} requested {vehicle.name} for {days} days.")
    if vehicle.available:
        print(f"Total cost: ₹{vehicle.rental_cost(days)}")
    else:
        print("❌ Vehicle is not available.")
