class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

    def profile(self):
        print(f"{self.name} | ID: {self.emp_id} | Manages: {self.team_size} people")

# Object
m = Manager("Seema Rao", "EMP987", 12)
m.profile()
