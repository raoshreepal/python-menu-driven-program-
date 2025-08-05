class Intern:
    def apply_leave(self):
        return "2 days approved"

class Manager:
    def apply_leave(self):
        return "10 days approved"

employees = {
    "Ravi": Intern(),
    "Neha": Manager()
}

for name, obj in employees.items():
    print(f"{name}: {obj.apply_leave()}")
