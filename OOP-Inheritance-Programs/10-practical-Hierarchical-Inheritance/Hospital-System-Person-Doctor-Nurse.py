class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def __init__(self, name, dept):
        super().__init__(name)
        self.dept = dept

    def info(self):
        print(f"Dr. {self.name}, Department: {self.dept}")

class Nurse(Person):
    def __init__(self, name, shift):
        super().__init__(name)
        self.shift = shift

    def info(self):
        print(f"Nurse {self.name}, Shift: {self.shift}")

# Objects
d = Doctor("Neha Sharma", "Cardiology")
n = Nurse("Kiran", "Night")

d.info()
n.info()
