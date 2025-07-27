class Person:
    def __init__(self, name):
        self.name = name

class Staff(Person):
    def __init__(self, name, staff_id):
        super().__init__(name)
        self.staff_id = staff_id

class TeachingStaff(Staff):
    def __init__(self, name, staff_id, subject):
        super().__init__(name, staff_id)
        self.subject = subject

    def record(self):
        print(f"{self.name} | ID: {self.staff_id} | Subject: {self.subject}")

# Object
t = TeachingStaff("Dr. Arora", "STF113", "Mathematics")
t.record()
