class Employee:
    def __init__(self, name, age):
        try:
            if not isinstance(age, int):
                raise TypeError("Age must be an integer.")
            self.name = name
            self.age = age
        except TypeError as e:
            print("Constructor error:", e)  # mestipon: Error handling during object creation

# e = Employee("Alice", "twenty")  # Uncomment to test
e = Employee("Bob", 30)
