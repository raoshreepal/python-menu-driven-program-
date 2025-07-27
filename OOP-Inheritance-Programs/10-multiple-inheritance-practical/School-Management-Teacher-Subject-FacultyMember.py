class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name

class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name

class FacultyMember(Teacher, Subject):
    def __init__(self, teacher_id, name, subject_name):
        Teacher.__init__(self, teacher_id, name)
        Subject.__init__(self, subject_name)

    def profile(self):
        print(f"Faculty: {self.name} (ID: {self.teacher_id}) | Subject: {self.subject_name}")

# Object
f = FacultyMember("T456", "Sneha Kapoor", "Computer Science")
f.profile()
