class NewCustomer:
    def notify(self):
        return "Send welcome email"

class LoyalCustomer:
    def notify(self):
        return "Send loyalty coupon"

clients = [NewCustomer(), LoyalCustomer(), NewCustomer()]
for client in clients:
    print(client.notify())
