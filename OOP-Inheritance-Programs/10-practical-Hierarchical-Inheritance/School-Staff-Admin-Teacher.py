class Staff:
    def __init__(self, name):
        self.name = name

class Admin(Staff):
    def __init__(self, name, dept):
        super().__init__(name)
        self.dept = dept

    def details(self):
        print(f"Admin: {self.name}, Department: {self.dept}")

class Teacher(Staff):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def details(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}")

# Objects
a = Admin("Anil Joshi", "Finance")
t = Teacher("Sunita Sharma", "English")

a.details()
t.details()
