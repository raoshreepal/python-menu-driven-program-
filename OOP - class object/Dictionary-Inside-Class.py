class EmployeeRecords:
    def __init__(self):
        self.employees = {}  # Dictionary with emp_id as key

    def add_employee(self, emp_id, name, salary):
        self.employees[emp_id] = {
            "name": name,
            "salary": salary
        }

    def display_all(self):
        print("\n--- All Employees ---")
        for emp_id, info in self.employees.items():
            print(f"ID: {emp_id}, Name: {info['name']}, Salary: ₹{info['salary']}")

# Usage
records = EmployeeRecords()
n = int(input("Enter number of employees: "))

for _ in range(n):
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    records.add_employee(emp_id, name, salary)

records.display_all()
