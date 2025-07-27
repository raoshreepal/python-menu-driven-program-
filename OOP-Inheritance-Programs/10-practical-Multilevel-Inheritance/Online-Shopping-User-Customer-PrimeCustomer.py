class User:
    def __init__(self, username):
        self.username = username

class Customer(User):
    def __init__(self, username, address):
        super().__init__(username)
        self.address = address

class PrimeCustomer(Customer):
    def __init__(self, username, address, prime_validity):
        super().__init__(username, address)
        self.prime_validity = prime_validity

    def details(self):
        print(f"{self.username} | Address: {self.address} | Prime Till: {self.prime_validity}")

# Object
p = PrimeCustomer("rohitx", "Pune", "Dec 2025")
p.details()
