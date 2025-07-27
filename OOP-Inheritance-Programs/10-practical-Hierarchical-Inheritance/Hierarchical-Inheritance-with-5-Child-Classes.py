'''

User Roles in an IT Company (Hierarchical Inheritance)
Parent Class: Person
Child Classes:

Developer

Tester

Designer

Manager

HR

Each role shares basic identity (from Person) but has its own responsibility.


'''



class Person:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_basic_info(self):
        print(f"Name: {self.name} | ID: {self.emp_id}")


class Developer(Person):
    def __init__(self, name, emp_id, language):
        super().__init__(name, emp_id)
        self.language = language

    def work(self):
        self.show_basic_info()
        print(f"Role: Developer | Code in: {self.language}")


class Tester(Person):
    def __init__(self, name, emp_id, tool):
        super().__init__(name, emp_id)
        self.tool = tool

    def work(self):
        self.show_basic_info()
        print(f"Role: Tester | Testing Tool: {self.tool}")


class Designer(Person):
    def __init__(self, name, emp_id, software):
        super().__init__(name, emp_id)
        self.software = software

    def work(self):
        self.show_basic_info()
        print(f"Role: Designer | Tools: {self.software}")


class Manager(Person):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

    def work(self):
        self.show_basic_info()
        print(f"Role: Manager | Team Size: {self.team_size}")


class HR(Person):
    def __init__(self, name, emp_id, region):
        super().__init__(name, emp_id)
        self.region = region

    def work(self):
        self.show_basic_info()
        print(f"Role: HR | Region: {self.region}")


# === Create Objects for each role ===
print("\n--- Developer ---")
dev = Developer("Aman", "DEV101", "Python")
dev.work()

print("\n--- Tester ---")
tester = Tester("Priya", "QA202", "Selenium")
tester.work()

print("\n--- Designer ---")
designer = Designer("Rohit", "DS303", "Figma")
designer.work()

print("\n--- Manager ---")
manager = Manager("Sonia", "MG404", 10)
manager.work()

print("\n--- HR ---")
hr = HR("Kiran", "HR505", "North Zone")
hr.work()
