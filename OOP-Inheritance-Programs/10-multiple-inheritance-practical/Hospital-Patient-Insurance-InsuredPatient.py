class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Insurance:
    def __init__(self, policy_number, provider):
        self.policy_number = policy_number
        self.provider = provider

class InsuredPatient(Patient, Insurance):
    def __init__(self, name, age, policy_number, provider):
        Patient.__init__(self, name, age)
        Insurance.__init__(self, policy_number, provider)

    def info(self):
        print(f"{self.name}, Age {self.age}, Insured with {self.provider} (Policy: {self.policy_number})")

# Object
p = InsuredPatient("Ramesh Sinha", 45, "POL12345", "HDFC Ergo")
p.info()
