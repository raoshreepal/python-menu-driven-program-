class Product:
    def __init__(self, name):
        self.name = name

class Item(Product):
    def __init__(self, name, price):
        super().__init__(name)
        self.price = price

class BilledItem(Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price)
        self.quantity = quantity

    def bill(self):
        total = self.price * self.quantity
        print(f"{self.name} x {self.quantity} = ₹{total}")

# Object
item = BilledItem("Shampoo", 120, 3)
item.bill()
