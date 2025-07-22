class Hospital:
    def __init__(self):
        self.patients = []  # List of patient records

    def add_patient(self, name, age, disease):
        patient = {
            "name": name,
            "age": age,
            "disease": disease
        }
        self.patients.append(patient)

    def display_patients(self):
        print("\n--- Patient Records ---")
        for p in self.patients:
            print(f"Name: {p['name']}, Age: {p['age']}, Disease: {p['disease']}")

# Usage
hospital = Hospital()
n = int(input("Enter number of patients to add: "))

for _ in range(n):
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    disease = input("Enter disease: ")
    hospital.add_patient(name, age, disease)

hospital.display_patients()
