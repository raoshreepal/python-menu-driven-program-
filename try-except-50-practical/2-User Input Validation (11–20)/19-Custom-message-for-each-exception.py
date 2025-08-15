# Give different outputs for ValueError, TypeError, etc.

try:
    a = int(input("Enter an integer: "))
    b = input("Enter a number to divide: ")
    result = a / int(b)
    print("Result:", result)
except ValueError:
    print("Error: Invalid number entered.")
except TypeError:
    print("Error: Type mismatch occurred.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print("Unexpected error:", e)
