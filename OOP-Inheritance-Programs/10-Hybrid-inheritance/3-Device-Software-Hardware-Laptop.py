class Device:
    def __init__(self, brand):
        self.brand = brand

class Software(Device):
    def __init__(self, brand, os):
        super().__init__(brand)
        self.os = os

class Hardware:
    def __init__(self, ram):
        self.ram = ram

class Laptop(Software, Hardware):
    def __init__(self, brand, os, ram):
        Software.__init__(self, brand, os)
        Hardware.__init__(self, ram)

    def details(self):
        print(f"Laptop: {self.brand}, OS: {self.os}, RAM: {self.ram}GB")

l = Laptop("Dell", "Windows 11", 16)
l.details()
