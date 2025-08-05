#✅ 8-Shopping-Cart–Dynamic-Discounts-with-Dictionary
class Product:
    def get_discount(self):
        pass

class Electronics(Product): 
    def get_discount(self):
        return 10

class Grocery(Product):
    def get_discount(self):
        return 2

cart = {
    "Laptop": Electronics(),
    "Rice": Grocery(),
}

for item, obj in cart.items():
    print(f"{item} has {obj.get_discount()}% discount")
#Output:
#Laptop has 10% discount
#Rice has 2% discount