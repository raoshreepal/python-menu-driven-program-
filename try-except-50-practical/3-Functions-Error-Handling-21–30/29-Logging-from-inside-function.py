import logging

logging.basicConfig(level=logging.ERROR)

def divide_with_logging(a, b):
    """Divide and log errors if any occur."""
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error(f"Division error: {e}")
        return None

# Example
print(divide_with_logging(10, 0))  # None and logs error
