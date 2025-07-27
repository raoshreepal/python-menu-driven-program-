'''
Bank System: Customer + Loan + Account = LoanAccount
'''
class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

class Loan(Customer):
    def __init__(self, name, customer_id, loan_amount):
        super().__init__(name, customer_id)
        self.loan_amount = loan_amount

class Account:
    def __init__(self, account_type):
        self.account_type = account_type

class LoanAccount(Loan, Account):
    def __init__(self, name, customer_id, loan_amount, account_type):
        Loan.__init__(self, name, customer_id, loan_amount)
        Account.__init__(self, account_type)

    def show_details(self):
        print(f"{self.name} (ID: {self.customer_id}) has a {self.account_type} loan of ₹{self.loan_amount}")

obj = LoanAccount("Kavita", "C234", 150000, "Home")
obj.show_details()
