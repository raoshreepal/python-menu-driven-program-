def parse_int_safe(s):
    """Parse string to int safely, return None if invalid."""
    try:
        return int(s)
    except ValueError:
        print(f"ValueError: '{s}' is not a valid integer.")
        return None

# Example
print(parse_int_safe("42"))    # 42
print(parse_int_safe("xyz"))   # Prints error, returns None
