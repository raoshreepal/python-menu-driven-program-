class Person:
    def __init__(self, name):
        self.name = name

class AccountHolder(Person):
    def __init__(self, name, account_number):
        super().__init__(name)
        self.account_number = account_number

class LoanCustomer(AccountHolder):
    def __init__(self, name, account_number, loan_amount):
        super().__init__(name, account_number)
        self.loan_amount = loan_amount

    def info(self):
        print(f"{self.name} | A/C: {self.account_number} | Loan: ₹{self.loan_amount}")

# Object
c = LoanCustomer("Amit Patel", "SB112233", 500000)
c.info()
