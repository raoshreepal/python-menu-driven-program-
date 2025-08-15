class Product:
    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")  # mestipon: Raising error for invalid input
        self.price = price

p = Product()
p.set_price(100)
# p.set_price(-10)  # Uncomment to test error
# Output: ValueError: Price cannot be negative.
# The code defines a class `Product` with a method `set_price` that raises a `ValueError` if the price is negative.
