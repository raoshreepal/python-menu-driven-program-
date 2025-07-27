class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def __init__(self, name, specialization):
        super().__init__(name)
        self.specialization = specialization

class Surgeon(Doctor):
    def __init__(self, name, specialization, surgeries_done):
        super().__init__(name, specialization)
        self.surgeries_done = surgeries_done

    def profile(self):
        print(f"Dr. {self.name} | {self.specialization} | Surgeries: {self.surgeries_done}")

# Object
s = Surgeon("Ravi Krishnan", "Orthopedic", 450)
s.profile()
