# Program to use else block when no exception occurs

try:
    a = 20
    b = 4
    result = a / b
except ZeroDivisionError:
    print("Error: Division by zero.")
else:
    # This block runs only if no exception is raised
    print("Success! The result is:", result)
