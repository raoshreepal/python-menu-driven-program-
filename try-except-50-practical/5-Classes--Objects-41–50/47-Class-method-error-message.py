class Account:
    def withdraw(self, balance, amount):
        if amount > balance:
            # mestipon: Return error message instead of raising
            return "Insufficient funds."
        return balance - amount

acc = Account()
print(acc.withdraw(100, 150))  # mestipon: Displays message instead of crashing
