def validate_positive_number(num):
    """Raise ValueError if number is not positive."""
    if num <= 0:
        raise ValueError("Number must be positive!")
    return num

# Example usage (uncomment to test)
# print(validate_positive_number(5))  # 5
# print(validate_positive_number(-3)) # Raises ValueError
