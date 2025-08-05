class Staff:
    def perform_duty(self):
        pass

class Doctor(Staff):
    def perform_duty(self):
        return "Treating patients"

class Nurse(Staff):
    def perform_duty(self):
        return "Assisting doctor"

staffs = [Doctor(), Nurse()]
for s in staffs:
    print(s.perform_duty())
