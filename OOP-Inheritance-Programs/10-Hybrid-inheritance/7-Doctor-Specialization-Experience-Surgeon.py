'''
7. Doctor + Specialization + Experience = Surgeon
'''

class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def __init__(self, name, reg_no):
        super().__init__(name)
        self.reg_no = reg_no

class Specialization:
    def __init__(self, field):
        self.field = field

class Experience:
    def __init__(self, years):
        self.years = years

class Surgeon(Doctor, Specialization, Experience):
    def __init__(self, name, reg_no, field, years):
        Doctor.__init__(self, name, reg_no)
        Specialization.__init__(self, field)
        Experience.__init__(self, years)

    def info(self):
        print(f"{self.name} ({self.reg_no}) - {self.field} Surgeon with {self.years} years experience.")

s = Surgeon("Dr. Ajay", "D567", "Cardiac", 10)
s.info()
