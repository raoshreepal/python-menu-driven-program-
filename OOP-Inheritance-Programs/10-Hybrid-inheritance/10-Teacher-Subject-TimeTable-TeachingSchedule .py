class Teacher:
    def __init__(self, teacher_name):
        self.teacher_name = teacher_name

class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name

class TimeTable:
    def __init__(self, time_slot):
        self.time_slot = time_slot

class TeachingSchedule(Teacher, Subject, TimeTable):
    def __init__(self, teacher_name, subject_name, time_slot):
        Teacher.__init__(self, teacher_name)
        Subject.__init__(self, subject_name)
        TimeTable.__init__(self, time_slot)

    def details(self):
        print(f"{self.teacher_name} teaches {self.subject_name} at {self.time_slot}")

t = TeachingSchedule("Mrs. Kapoor", "Mathematics", "10:00 AM - 11:00 AM")
t.details()
