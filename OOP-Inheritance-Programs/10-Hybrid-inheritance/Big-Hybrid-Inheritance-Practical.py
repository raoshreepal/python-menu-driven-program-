'''

Person
 ├── Patient
 │    └── MedicalHistory
 ├── Doctor
 │    └── Appointment
 └── Bill
         \
       MedicalReport (inherits from MedicalHistory, Appointment, Bill)



'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id

class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

class MedicalHistory(Patient):
    def __init__(self, name, age, patient_id, disease):
        super().__init__(name, age, patient_id)
        self.disease = disease

class Appointment(Doctor):
    def __init__(self, name, age, specialization, appointment_date):
        super().__init__(name, age, specialization)
        self.appointment_date = appointment_date

class Bill:
    def __init__(self, amount):
        self.amount = amount

class MedicalReport(MedicalHistory, Appointment, Bill):
    def __init__(self, name, age, patient_id, disease, specialization, appointment_date, amount):
        MedicalHistory.__init__(self, name, age, patient_id, disease)
        Appointment.__init__(self, name, age, specialization, appointment_date)
        Bill.__init__(self, amount)

    def show_report(self):
        print(f"Patient: {self.name} ({self.age} yrs), ID: {self.patient_id}")
        print(f"Disease: {self.disease}")
        print(f"Doctor: {self.specialization}, Appointment: {self.appointment_date}")
        print(f"Total Bill: ₹{self.amount}")

report = MedicalReport(
    name="Rahul",
    age=32,
    patient_id="P101",
    disease="Typhoid",
    specialization="General Medicine",
    appointment_date="2025-07-29",
    amount=2500
)

report.show_report()
