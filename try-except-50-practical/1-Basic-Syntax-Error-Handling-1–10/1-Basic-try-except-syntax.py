# Program to divide two numbers and catch ZeroDivisionError

try:
    a = 10
    b = 0
    result = a / b  # This will raise ZeroDivisionError
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
