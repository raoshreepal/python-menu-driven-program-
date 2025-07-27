class Person:
    def __init__(self, name):
        self.name = name

class Department(Person):
    def __init__(self, name, dept):
        super().__init__(name)
        self.dept = dept

class Course:
    def __init__(self, course_name):
        self.course_name = course_name

class Trainer(Department, Course):
    def __init__(self, name, dept, course_name):
        Department.__init__(self, name, dept)
        Course.__init__(self, course_name)

    def show(self):
        print(f"Trainer: {self.name}, Dept: {self.dept}, Course: {self.course_name}")

t = Trainer("Kiran", "IT", "Python")
t.show()
