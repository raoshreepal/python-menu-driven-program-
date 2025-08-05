#Definition: Different roles (Student, Teacher) implement get_details() differently.

class User:
    def get_details(self):
        pass

class Student(User):
    def get_details(self):
        return "Student details"

class Teacher(User):
    def get_details(self):
        return "Teacher details"

users = [Student(), Teacher()]
for user in users:
    print(user.get_details())

#Output:
#Student details
#Teacher details