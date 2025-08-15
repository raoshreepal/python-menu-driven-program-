
# 📝 User Input Validation in Python (Programs 11–20)

Welcome to the **User Input Validation** collection! This set of programs focuses on **handling user inputs safely and robustly** using Python’s exception handling. From simple validation to retry logic, and logging to retrying operations — this is essential for building resilient applications.

---

## 🔥 What You’ll Learn Here

* Wrapping risky operations in functions
* Returning safe defaults on errors
* Raising and propagating exceptions
* Using `try-finally` for resource cleanup
* Nested exceptions in multi-step processing
* Safe type conversion with lambdas
* Logging errors from functions
* Implementing retry logic for unreliable operations

---

## 📋 Program List (11–20)

### 21. Safe Division with Try-Except

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
```

**Use:** Protects your division from crashing your program if `b` is zero.

---

### 22. Return Default Value on Exception

```python
def safe_divide_with_default(a, b):
    try:
        return a / b
    except Exception:
        return -1
```

**Use:** Return a fallback value (`-1`) for any error during division.

---

### 23. Raise Exception for Invalid Input

```python
def validate_positive_number(num):
    if num <= 0:
        raise ValueError("Number must be positive!")
    return num
```

**Use:** Enforce business rules by manually raising exceptions.

---

### 24. Use Try-Finally for Resource Cleanup

```python
def process_resource():
    resource = None
    try:
        resource = open("test.txt", "w")
        resource.write("Hello, World!")
    finally:
        if resource:
            resource.close()
            print("Resource closed")
```

**Use:** Ensure files or resources close properly no matter what.

---

### 25. Nested Exception Handling Across Functions

```python
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found!")
        return None

def process_file(filename):
    content = read_file(filename)
    if content:
        try:
            number = int(content)
            return number * 2
        except ValueError:
            print("File content is not a valid number!")
            return None
    return None
```

**Use:** Combine multiple steps with independent error handling.

---

### 26. Use Lambda with Exception Handling Helper

```python
def safe_int_conversion(s):
    try:
        return int(s)
    except ValueError:
        return None

safe_convert = lambda s: safe_int_conversion(s)
```

**Use:** Use lambdas and helper functions to simplify validation.

---

### 27. Print Error Inside Function and Return None

```python
def parse_int_safe(s):
    try:
        return int(s)
    except ValueError:
        print(f"ValueError: '{s}' is not a valid integer.")
        return None
```

**Use:** Notify users when inputs are invalid but keep running.

---

### 28. Exception Propagation

```python
def might_fail(n):
    if n < 0:
        raise ValueError("Negative value not allowed")
    return n * 10

def caller():
    return might_fail(-1)
```

**Use:** Let exceptions bubble up for higher-level handling.

---

### 29. Logging Exceptions in Functions

```python
import logging
logging.basicConfig(level=logging.ERROR)

def divide_with_logging(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logging.error(f"Division error: {e}")
        return None
```

**Use:** Log errors instead of just printing, for production readiness.

---

### 30. Retry Logic for Unreliable Operations

```python
import time
import random

def unreliable_operation():
    if random.random() < 0.7:
        raise RuntimeError("Temporary failure")
    return "Success!"

def retry_operation(max_retries=3):
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
```

**Use:** Automatically retry operations that might fail temporarily, like network calls.

---

## 🌟 Why These Matter in Real Projects

* **User Input Validation:** Ensures apps don’t crash on unexpected or malicious inputs.
* **Resource Handling:** Prevents resource leaks in file/database/network operations.
* **Logging:** Tracks failures silently in the background for debugging later.
* **Retry Logic:** Improves resilience in flaky network or hardware interactions.
* **Exception Propagation:** Enables clean error handling across multiple layers in big projects.

---

## 🚀 Next Steps

* Combine these techniques to build fault-tolerant, user-friendly applications.
* Practice by adding these patterns to your own projects — from web apps to data pipelines.
* Experiment with custom exceptions and more sophisticated retry/backoff strategies.

