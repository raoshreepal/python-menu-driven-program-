class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, subjects):
        super().__init__(name)

        self.subjects = subjects  # tuple of subject names

    def display_subjects(self):
        print(f"{self.name}'s Subjects:")
        for sub in self.subjects:
            print("-", sub)

stu = Student("Ankit", ("Math", "Physics", "Computer"))
stu2 = Student("Ankita", ("Math", "Physics", "Computer"))

stu.display_subjects()
stu2.display_subjects()