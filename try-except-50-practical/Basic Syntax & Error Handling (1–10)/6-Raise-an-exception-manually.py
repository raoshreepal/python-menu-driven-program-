# Program to raise a custom exception manually

age = -5

if age < 0:
    raise ValueError("Custom error: Age cannot be negative.")
else:
    print("Age is valid.")
# This code checks if the age is negative and raises a ValueError with a custom message.
# It demonstrates how to manually raise an exception when a specific condition is met.
# If the age is valid (non-negative), it prints that the age is valid.
# This is useful for enforcing constraints in your code and providing clear error messages.