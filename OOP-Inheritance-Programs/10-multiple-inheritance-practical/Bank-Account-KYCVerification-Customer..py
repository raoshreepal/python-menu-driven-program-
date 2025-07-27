class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class KYCVerification:
    def __init__(self, aadhar, pan):
        self.aadhar = aadhar
        self.pan = pan

class Customer(Account, KYCVerification):
    def __init__(self, account_number, balance, aadhar, pan, name):
        Account.__init__(self, account_number, balance)
        KYCVerification.__init__(self, aadhar, pan)
        self.name = name

    def show_details(self):
        print(f"{self.name}: ₹{self.balance} | Aadhar: {self.aadhar}, PAN: {self.pan}")

# Object
cust = Customer("SB123456", 15000, "1234-5678-9101", "ABCDE1234F", "Rahul Mehta")
cust.show_details()
