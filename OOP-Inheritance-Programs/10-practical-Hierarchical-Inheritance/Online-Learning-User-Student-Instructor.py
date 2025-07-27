class User:
    def __init__(self, name):
        self.name = name

class Student(User):
    def __init__(self, name, enrolled_course):
        super().__init__(name)
        self.enrolled_course = enrolled_course

    def show(self):
        print(f"Student: {self.name}, Course: {self.enrolled_course}")

class Instructor(User):
    def __init__(self, name, expertise):
        super().__init__(name)
        self.expertise = expertise

    def show(self):
        print(f"Instructor: {self.name}, Expertise: {self.expertise}")

# Objects
s = Student("Kunal", "Python Bootcamp")
i = Instructor("Ritika", "Machine Learning")

s.show()
i.show()
