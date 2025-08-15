def might_fail(n):
    """Raise error if input is negative."""
    if n < 0:
        raise ValueError("Negative value not allowed")
    return n * 10

def caller():
    """Call might_fail and let exceptions bubble up."""
    return might_fail(-1)

# When calling caller(), the ValueError will propagate up unless caught.
# Uncomment to test:
# print(caller())  # Raises ValueError
