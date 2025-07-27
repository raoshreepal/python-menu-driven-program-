class Owner:
    def __init__(self, name, license_no):
        self.name = name
        self.license_no = license_no

class VehicleDetails:
    def __init__(self, vehicle_number, model):
        self.vehicle_number = vehicle_number
        self.model = model

class RegisteredVehicle(Owner, VehicleDetails):
    def __init__(self, name, license_no, vehicle_number, model):
        Owner.__init__(self, name, license_no)
        VehicleDetails.__init__(self, vehicle_number, model)

    def display(self):
        print(f"{self.name} owns {self.model} ({self.vehicle_number}) - License: {self.license_no}")

# Object
v = RegisteredVehicle("Arjun Kumar", "DL-091234", "MH12AB1234", "Honda City")
v.display()
