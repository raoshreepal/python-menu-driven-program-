# Raise a custom exception if age is negative or zero

try:
    age = int(input("Enter your age: "))
    if age <= 0:
        raise ValueError("Age must be greater than 0.")
    print("Your age is:", age)
except ValueError as e:
    print("Error:", e)
