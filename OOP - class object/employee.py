class Employee:
    def __init__(self, name, id, base_salary, bonus):
        self.name = name
        self.id = id
        self.base_salary = base_salary
        self.bonus = bonus

    def total_salary(self):
        return self.base_salary + self.bonus

    def display(self):
        print(f"Employee: {self.name}, ID: {self.id}")
        print(f"Total Salary: ₹{self.total_salary()}")

# Usage
emp1 = Employee("Ravi", 201, 30000, 5000)
emp2 = Employee("Meena", 202, 28000, 4000)

emp1.display()
emp2.display()
