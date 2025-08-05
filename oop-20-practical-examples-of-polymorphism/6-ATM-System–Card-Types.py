class ATMCard:
    def withdraw_limit(self):
        pass

class DebitCard(ATMCard):
    def withdraw_limit(self):
        return 25000

class CreditCard(ATMCard):
    def withdraw_limit(self):
        return 50000

for card in [DebitCard(), CreditCard()]:
    print(f"Limit: ₹{card.withdraw_limit()}")
