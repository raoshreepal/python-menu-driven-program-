class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks  # List of marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calculate_average():.2f}")

# Usage
student1 = Student("Alice", 101, [85, 90, 78])
student2 = Student("Bob", 102, [75, 88, 92])

student1.display()
student2.display()
