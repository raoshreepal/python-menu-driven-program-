class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

class GraduateStudent(Student):
    def __init__(self, name, roll, degree):
        super().__init__(name, roll)
        self.degree = degree

    def details(self):
        print(f"{self.name} | Roll: {self.roll} | Degree: {self.degree}")

# Object
s = GraduateStudent("Kavya Singh", "BSC2025", "B.Sc. Computer Science")
s.details()
