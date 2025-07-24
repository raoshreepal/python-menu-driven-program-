class Account:
    def __init__(self, acc_no, holder, transactions):
        self.acc_no = acc_no
        self.holder = holder
        self.transactions = transactions

    def balance(self):
        bal = 0
        for t in self.transactions:
            bal += t
        return bal

class SavingsAccount(Account):
    def display(self):
        print(f"{self.holder} ({self.acc_no}) Balance: ₹{self.balance()}")

a = SavingsAccount("SB1001", "Nina", [1000, -500, 2000])
a.display()
