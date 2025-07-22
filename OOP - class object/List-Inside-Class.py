class StudentManager:
    def __init__(self):
        self.students = []  # List to hold multiple student records

    def add_student(self, name, roll, marks):
        student = {
            "name": name,
            "roll": roll,
            "marks": marks
        }
        self.students.append(student)

    def display_all(self):
        print("\n--- All Students ---")
        for student in self.students:
            print(f"Name: {student['name']}, Roll No: {student['roll']}, Marks: {student['marks']}")

# Usage
manager = StudentManager()
n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))
    manager.add_student(name, roll, marks)

manager.display_all()
