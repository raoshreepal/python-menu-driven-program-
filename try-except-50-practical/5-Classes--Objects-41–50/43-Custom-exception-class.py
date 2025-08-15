class MyError(Exception):  # mestipon: Custom exception definition
    pass

def check_value(x):
    if x == 0:
        raise MyError("Zero is not allowed.")  # mestipon: Raise custom error

check_value(5)
# check_value(0)  # Uncomment to test error
# Output: MyError: Zero is not allowed.
# The code defines a custom exception class `MyError` that inherits from the built-in `Exception` class.
# The function `check_value` raises this custom exception if the input value is zero.
# This demonstrates how to create and raise a custom exception in Python.