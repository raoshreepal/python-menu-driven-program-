class StudentInfo:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

class Marks:
    def __init__(self, subject_marks):
        self.subject_marks = subject_marks

class ReportCard(StudentInfo, Marks):
    def __init__(self, name, roll, subject_marks):
        StudentInfo.__init__(self, name, roll)
        Marks.__init__(self, subject_marks)

    def display(self):
        total = sum(self.subject_marks.values())
        print(f"{self.name} (Roll: {self.roll}) Total Marks: {total}")

# Object
marks = {'Math': 85, 'Science': 90, 'English': 88}
student = ReportCard("Anjali Verma", 102, marks)
student.display()
