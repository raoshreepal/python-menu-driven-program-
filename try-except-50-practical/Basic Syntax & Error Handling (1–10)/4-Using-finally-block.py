# Program to show that finally block runs regardless of exceptions

try:
    a = 15
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
finally:
    print("Done")
# This block will always execute
# regardless of whether an exception occurred or not.
# It is often used for cleanup actions, like closing files or releasing resources.
# In this case, it simply prints "Done" after the try-except block.
# The finally block is useful for ensuring that certain code runs no matter what happens in the try-except.
