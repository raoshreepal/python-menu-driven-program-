class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks  # list of subject marks

    def total_marks(self):
        total = 0
        for mark in self.marks:
            total += mark
        return total

class Result(Student):
    def average(self):
        return self.total_marks() / len(self.marks)

s1 = Result("Ravi", 101, [85, 90, 78])
print(f"{s1.name}'s Total: {s1.total_marks()} Average: {s1.average():.2f}")
