class ScienceStudent:
    def get_grade(self):
        return "A in Physics"

class CommerceStudent:
    def get_grade(self):
        return "A in Accounts"

students = [ScienceStudent(), CommerceStudent()]
for s in students:
    print(s.get_grade())
