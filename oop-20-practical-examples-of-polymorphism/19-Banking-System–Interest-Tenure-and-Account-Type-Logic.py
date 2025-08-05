'''

🔹Scenario: Different accounts calculate interest based on amount, duration, and customer type (regular/senior citizen).
🔹Definition: Same method calculate_interest() behaves differently depending on account type.
'''
class Account:
    def __init__(self, name, principal, years, is_senior=False):
        self.name = name
        self.principal = principal
        self.years = years
        self.is_senior = is_senior

    def calculate_interest(self):
        raise NotImplementedError("Subclasses must implement this method")

class SavingAccount(Account):
    def calculate_interest(self):
        rate = 0.04
        if self.is_senior:
            rate += 0.005  # 0.5% extra for senior
        return self.principal * rate * self.years

class FixedDeposit(Account):
    def calculate_interest(self):
        if self.years >= 5:
            rate = 0.075 if not self.is_senior else 0.08
        else:
            rate = 0.065 if not self.is_senior else 0.07
        return self.principal * rate * self.years

# List of account objects
accounts = [
    SavingAccount("Amit", 10000, 2, is_senior=False),
    FixedDeposit("Priya", 50000, 6, is_senior=True),
    SavingAccount("Rajesh", 15000, 1, is_senior=True),
    FixedDeposit("Sneha", 30000, 3, is_senior=False)
]

for acc in accounts:
    interest = acc.calculate_interest()
    print(f"{acc.name} earns ₹{interest:.2f} interest from {acc.__class__.__name__}")
