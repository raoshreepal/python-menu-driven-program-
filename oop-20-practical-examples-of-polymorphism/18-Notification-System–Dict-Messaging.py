class Email:
    def send(self, msg):
        return f"Email: {msg}"

class SMS:
    def send(self, msg):
        return f"SMS: {msg}"

notifiers = {
    "customer1": Email(),
    "customer2": SMS()
}

for user, channel in notifiers.items():
    print(channel.send("Your order is shipped"))
