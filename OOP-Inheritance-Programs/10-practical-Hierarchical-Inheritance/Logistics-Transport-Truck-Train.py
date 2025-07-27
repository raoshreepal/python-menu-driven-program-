class Transport:
    def __init__(self, number):
        self.number = number

class Truck(Transport):
    def __init__(self, number, load):
        super().__init__(number)
        self.load = load

    def status(self):
        print(f"Truck {self.number} carrying {self.load} tons")

class Train(Transport):
    def __init__(self, number, coaches):
        super().__init__(number)
        self.coaches = coaches

    def status(self):
        print(f"Train {self.number} with {self.coaches} coaches")

# Objects
t1 = Truck("MH12TR3456", 15)
t2 = Train("12345", 20)

t1.status()
t2.status()
