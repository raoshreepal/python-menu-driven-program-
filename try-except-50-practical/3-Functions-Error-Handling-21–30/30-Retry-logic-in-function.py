import time

def unreliable_operation():
    """Simulate an operation that fails randomly."""
    import random
    if random.random() < 0.7:
        raise RuntimeError("Temporary failure")
    return "Success!"

def retry_operation(max_retries=3):
    """Retry an operation up to max_retries times."""
    for attempt in range(1, max_retries + 1):
        try:
            result = unreliable_operation()
            print(f"Attempt {attempt}: Success")
            return result
        except RuntimeError as e:
            print(f"Attempt {attempt} failed: {e}")
            time.sleep(1)
    print("All attempts failed.")
    return None

# Example usage
retry_operation()
