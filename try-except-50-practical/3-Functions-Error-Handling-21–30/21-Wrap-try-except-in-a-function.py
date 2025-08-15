def safe_divide(a, b):
    """Divide a by b, handling division by zero error."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

# Example
print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # Error message + None
# Function to check password match with exception handling