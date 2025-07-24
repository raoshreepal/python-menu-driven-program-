class Inventory:
    def __init__(self, items):
        self.items = items  # dict of item:quantity

    def total_items(self):
        count = 0
        for key in self.items:
            count += self.items[key]
        return count

class Store(Inventory):
    def show(self):
        for k, v in self.items.items():
            print(f"{k} - {v}")
        print("Total Items:", self.total_items())

store = Store({"Apples": 20, "Bananas": 30, "Mangoes": 10})
store.show()
