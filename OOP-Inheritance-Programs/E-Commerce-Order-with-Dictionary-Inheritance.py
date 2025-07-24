class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

class Order(Product):
    def __init__(self, pid, name, price, qty):
        super().__init__(pid, name, price)
        self.qty = qty

    def total_price(self):
        return self.qty * self.price

    def summary(self):
        print(f"{self.name} x{self.qty} = ₹{self.total_price()}")

o = Order(101, "Shoes", 2000, 2)
o.summary()
*
**
***
****
*****