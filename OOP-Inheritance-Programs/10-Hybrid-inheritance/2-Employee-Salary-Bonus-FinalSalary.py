class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id

class Salary(Employee):
    def __init__(self, emp_id, basic):
        super().__init__(emp_id)
        self.basic = basic

class Bonus:
    def __init__(self, bonus):
        self.bonus = bonus

class FinalSalary(Salary, Bonus):
    def __init__(self, emp_id, basic, bonus):
        Salary.__init__(self, emp_id, basic)
        Bonus.__init__(self, bonus)

    def total_salary(self):
        print(f"Total Salary for {self.emp_id}: {self.basic + self.bonus}")

f = FinalSalary("E102", 50000, 10000)
f.total_salary()
