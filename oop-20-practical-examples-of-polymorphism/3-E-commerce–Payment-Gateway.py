#Definition: Different payment methods use the same interface.
class Payment:
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paying ₹{amount} via Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paying ₹{amount} via UPI")

for method in [CreditCard(), UPI()]:
    method.pay(500)


