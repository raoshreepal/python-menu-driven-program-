class Item:
    def get_total(self, qty, price):
        pass

class Food(Item):
    def get_total(self, qty, price):
        return qty * price

class Luxury(Item):
    def get_total(self, qty, price):
        return qty * price * 1.18

items = [Food(), Luxury()]
names = ["Bread", "Perfume"]
quantities = [2, 1]
prices = [50, 500]

for name, obj, q, p in zip(names, items, quantities, prices):
    print(f"{name} Total: ₹{obj.get_total(q, p)}")
