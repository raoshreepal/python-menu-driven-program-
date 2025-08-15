# Program using nested try-except blocks for complex operations

try:
    a = int(input("Enter a number: "))
    try:
        result = 100 / a
        print("Result:", result)
    except ZeroDivisionError:
        print("Inner error: Cannot divide by zero.")
except ValueError:
    print("Outer error: Invalid input, not an integer.")
