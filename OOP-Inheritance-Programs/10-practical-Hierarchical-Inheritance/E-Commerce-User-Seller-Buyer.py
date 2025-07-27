class User:
    def __init__(self, username):
        self.username = username

class Seller(User):
    def __init__(self, username, shop_name):
        super().__init__(username)
        self.shop_name = shop_name

    def show(self):
        print(f"Seller: {self.username}, Shop: {self.shop_name}")

class Buyer(User):
    def __init__(self, username, location):
        super().__init__(username)
        self.location = location

    def show(self):
        print(f"Buyer: {self.username}, Location: {self.location}")

# Objects
s = Seller("seller_rahul", "Rahul Electronics")
b = Buyer("buyer_sneha", "Mumbai")

s.show()
b.show()
