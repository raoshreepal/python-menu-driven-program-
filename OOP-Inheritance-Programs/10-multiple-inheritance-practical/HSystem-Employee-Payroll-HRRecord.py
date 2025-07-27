class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

class Payroll:
    def __init__(self, salary, bank):
        self.salary = salary
        self.bank = bank

class HRRecord(Employee, Payroll):
    def __init__(self, emp_id, name, salary, bank):
        Employee.__init__(self, emp_id, name)
        Payroll.__init__(self, salary, bank)

    def summary(self):
        print(f"{self.name} (ID: {self.emp_id}) gets ₹{self.salary}/month via {self.bank}")

# Object
hr = HRRecord("EMP1001", "Vikram Sharma", 50000, "ICICI Bank")
hr.summary()
