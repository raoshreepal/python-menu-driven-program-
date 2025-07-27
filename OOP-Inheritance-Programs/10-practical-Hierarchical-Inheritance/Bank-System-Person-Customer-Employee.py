class Person:
    def __init__(self, name):
        self.name = name

class Customer(Person):
    def __init__(self, name, account_number):
        super().__init__(name)
        self.account_number = account_number

    def show(self):
        print(f"Customer: {self.name}, Account: {self.account_number}")

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def show(self):
        print(f"Employee: {self.name}, ID: {self.emp_id}")

# Objects
cust = Customer("Ravi Kumar", "SB778899")
emp = Employee("Megha Rani", "EMP102")

cust.show()
emp.show()
