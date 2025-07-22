class BankAccount:
    def __init__(self, name, acc_no, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display(self):
        print(f"Account Holder: {self.name}, Account No: {self.acc_no}")
        print(f"Current Balance: ₹{self.balance}")

# Usage
acc1 = BankAccount("Anjali", 1001, 5000)
acc1.deposit(2000)
acc1.withdraw(1000)
acc1.display()
