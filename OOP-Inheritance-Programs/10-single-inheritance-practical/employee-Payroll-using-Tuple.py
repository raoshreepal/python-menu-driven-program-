class Employee:
    def __init__(self, name, emp_id, salary_components):
        self.name = name
        self.emp_id = emp_id
        self.salary_components = salary_components  # tuple (basic, hra, bonus)

    def gross_salary(self):
        total = 0
        for s in self.salary_components:
            total += s
        return total

class PaySlip(Employee):
    def display(self):
        print(f"Name: {self.name}, Gross Salary: {self.gross_salary()}")

emp = PaySlip("Amit", 202, (30000, 12000, 5000))
emp.display()
