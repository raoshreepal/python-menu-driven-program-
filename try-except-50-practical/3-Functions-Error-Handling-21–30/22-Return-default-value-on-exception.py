def safe_divide_with_default(a, b):
    """Return division result or -1 if an error occurs."""
    try:
        return a / b
    except Exception:
        return -1

# Example
print(safe_divide_with_default(10, 2))  # 5.0
print(safe_divide_with_default(10, 0))  # -1
