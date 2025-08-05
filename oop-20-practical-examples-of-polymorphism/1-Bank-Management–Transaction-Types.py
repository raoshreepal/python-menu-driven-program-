'''
Definition: Same method process() behaves differently for Deposit and Withdrawal.
'''
class Transaction:
    def process(self):
        pass

class Deposit(Transaction):
    def process(self):
        print("Depositing amount...")

class Withdrawal(Transaction):
    def process(self):
        print("Withdrawing amount...")

def execute_transaction(transaction: Transaction):
    transaction.process()

execute_transaction(Deposit())
execute_transaction(Withdrawal())
