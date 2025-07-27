class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

    def details(self):
        print(f"Student: {self.name}, Roll: {self.roll}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def details(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}")

# Objects
s = Student("Pooja", 102)
t = Teacher("Dr. Ramesh", "Physics")

s.details()
t.details()
