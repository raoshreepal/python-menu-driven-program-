class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Course:
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

class Enrollment(User, Course):
    def __init__(self, username, email, course_name, duration):
        User.__init__(self, username, email)
        Course.__init__(self, course_name, duration)

    def details(self):
        print(f"{self.username} ({self.email}) enrolled in {self.course_name} [{self.duration}]")

# Object
e = Enrollment("rahul_k", "rahul@gmail.com", "Data Science Bootcamp", "12 weeks")
e.details()
