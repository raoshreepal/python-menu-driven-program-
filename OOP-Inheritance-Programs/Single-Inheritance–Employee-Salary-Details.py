class Employee:
    def __init__(self, name, basic):
        self.name = name
        self.basic = basic

class Salary(Employee):
    def calculate_salary(self):
        hra = 0.2 * self.basic
        da = 0.1 * self.basic
        return self.basic + hra + da

emp = Salary("Ravi", 30000)
print(f"{emp.name}'s Salary: ₹{emp.calculate_salary()}")
