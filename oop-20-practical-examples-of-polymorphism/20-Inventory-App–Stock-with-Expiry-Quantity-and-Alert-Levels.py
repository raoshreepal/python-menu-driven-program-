
'''
🔹Scenario: System checks stock status for perishable and non-perishable items using quantity and expiry date logic.
🔹Definition: check_stock() method is polymorphic depending on product type and logic.
'''

from datetime import datetime, timedelta

class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def check_stock(self):
        raise NotImplementedError("Subclasses must implement this method")

class Perishable(Item):
    def __init__(self, name, quantity, expiry_date):
        super().__init__(name, quantity)
        self.expiry_date = expiry_date

    def check_stock(self):
        days_left = (self.expiry_date - datetime.today()).days
        if days_left < 0:
            return f"{self.name}: ❌ Expired!"
        elif self.quantity < 10:
            return f"{self.name}: ⚠️ Low stock, {days_left} days left"
        else:
            return f"{self.name}: ✅ Fresh, {days_left} days remaining"

class NonPerishable(Item):
    def __init__(self, name, quantity, reorder_level):
        super().__init__(name, quantity)
        self.reorder_level = reorder_level

    def check_stock(self):
        if self.quantity <= self.reorder_level:
            return f"{self.name}: ⚠️ Below reorder level ({self.quantity} items)"
        return f"{self.name}: ✅ Sufficient stock ({self.quantity} items)"

# Inventory setup
inventory = [
    Perishable("Milk", 8, datetime.today() + timedelta(days=2)),
    Perishable("Yogurt", 15, datetime.today() - timedelta(days=1)),
    NonPerishable("Sugar", 50, reorder_level=20),
    NonPerishable("Salt", 10, reorder_level=15)
]

for item in inventory:
    print(item.check_stock())
