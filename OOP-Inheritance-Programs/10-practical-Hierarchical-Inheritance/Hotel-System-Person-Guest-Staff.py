class Person:
    def __init__(self, name):
        self.name = name

class Guest(Person):
    def __init__(self, name, room_no):
        super().__init__(name)
        self.room_no = room_no

    def info(self):
        print(f"Guest: {self.name}, Room: {self.room_no}")

class Staff(Person):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

    def info(self):
        print(f"Staff: {self.name}, Role: {self.role}")

# Objects
g = Guest("Ajay", 402)
s = Staff("Ravi", "Receptionist")

g.info()
s.info()
