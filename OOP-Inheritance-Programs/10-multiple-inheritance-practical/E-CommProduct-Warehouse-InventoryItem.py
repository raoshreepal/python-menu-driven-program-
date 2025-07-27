class Product:
    def __init__(self, name, sku):
        self.name = name
        self.sku = sku

class Warehouse:
    def __init__(self, location, stock):
        self.location = location
        self.stock = stock

class InventoryItem(Product, Warehouse):
    def __init__(self, name, sku, location, stock):
        Product.__init__(self, name, sku)
        Warehouse.__init__(self, location, stock)

    def details(self):
        print(f"{self.name} ({self.sku}) in {self.location}: {self.stock} units")

# Object
item = InventoryItem("Wireless Mouse", "WM1234", "Delhi", 200)
item.details()
