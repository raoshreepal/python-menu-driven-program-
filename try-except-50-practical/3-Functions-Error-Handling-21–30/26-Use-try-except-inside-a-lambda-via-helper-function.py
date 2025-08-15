def safe_int_conversion(s):
    """Convert string to int safely."""
    try:
        return int(s)
    except ValueError:
        return None

# Use lambda to wrap helper function
safe_convert = lambda s: safe_int_conversion(s)

# Examples
print(safe_convert("123"))  # 123
print(safe_convert("abc"))  # None
