# Program to catch TypeError when adding incompatible types

try:
    result = 10 + "5"  # Invalid operation: int + str
except TypeError:
    print("Error: Cannot add integer and string.")