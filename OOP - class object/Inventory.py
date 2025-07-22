class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def display(self):
        print(f"Product: {self.name}")
        print(f"Price: ₹{self.price}, Quantity: {self.quantity}")
        print(f"Total Stock Value: ₹{self.total_value()}")

# Usage
product1 = Product("Laptop", 50000, 10)
product2 = Product("Mouse", 500, 100)

product1.display()
product2.display()
