

# 🐍 Python Exception Handling & Input Validation — Programs 1 to 50

Welcome to the ultimate guide and code collection for mastering **Python Exception Handling, Input Validation, and File Handling**! These 50 carefully crafted programs demonstrate essential Python concepts from beginner to intermediate level, preparing you for real-world software robustness.

---

## 📚 Contents Overview

| Program Range | Topic                             | Key Concepts Covered                                                                                                                           |
| ------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 – 10        | Basic Syntax & Error Handling     | try-except, else, finally, nested try, raising exceptions, catching common errors (IndexError, KeyError, TypeError)                            |
| 11 – 20       | User Input Validation             | Input validation loops, retries, raising custom exceptions, logging errors, handling keyboard interrupt                                        |
| 21 – 30       | Advanced Exception Handling       | Functions with exceptions, resource cleanup, exception propagation, logging, retry logic                                                       |
| 31 – 40       | File Handling                     | Safe file open/read/write, handling FileNotFoundError, IOError, PermissionError, parsing file content, large file reading, logging file errors |
| 41 – 50       | (Pending your input / Extendable) | Further real-world examples like network errors, API calls, database access error handling, or custom exception classes                        |

---

## Detailed Program Guide

---

### 1–10: Basic Syntax & Error Handling

Learn to use the core `try-except` structure, catch specific errors like `ZeroDivisionError`, `IndexError`, `KeyError`, `TypeError`, and how to use `else` and `finally` blocks effectively.

* **Example:** Handling division by zero
* **Example:** Nested try-except blocks
* **Example:** Raising exceptions manually with `raise`

---

### 11–20: User Input Validation

Make your programs foolproof against invalid user inputs by applying exception handling and validation loops. This set includes retry mechanisms, limited attempts, password confirmation, and graceful exit on keyboard interrupts.

* **Example:** Retry input until valid integer is entered
* **Example:** Raise exception if passwords don't match
* **Example:** Log errors to file on exception
* **Example:** Retry logic with random failure simulation

---

### 21–30: Advanced Exception Handling & Functions

Focus on modularizing exception handling into reusable functions, managing resources with `try-finally`, handling nested exceptions across function calls, and logging errors with Python's `logging` module.

* **Example:** Safe division function with error handling
* **Example:** Reading and processing files with nested exceptions
* **Example:** Retry operations with exponential backoff

---

### 31–40: File Handling with Error Management

Master file I/O operations and safely handle common file-related errors like missing files, permission issues, improper closures, invalid content formats, and handling large files efficiently.

* **Example:** Open file safely and catch `FileNotFoundError`
* **Example:** Use `with open()` and context managers for safe file handling
* **Example:** Read large files in chunks to avoid memory errors
* **Example:** Log file errors in a separate error log file

---

### 41–50: Real-world Use Cases & Further Extensions

Expand your skills with real-world projects handling network failures, API requests, database errors, and defining custom exceptions tailored for your application.

---

## Why This Matters in Real-Time Projects

* **Robust User Interfaces:** Prevent crashes by validating all user inputs.
* **Reliable Data Processing:** Ensure file and resource handling is fail-safe.
* **Maintainability:** Use logging to track and debug errors without user impact.
* **Scalability:** Retry mechanisms help services handle temporary failures gracefully.
* **Professional Code:** Proper exception design and handling makes your code production-ready.

---

## How to Use This Repository

1. **Explore the programs folder** by category (e.g., 1–10, 11–20, etc.)
2. **Run each program individually** to see how exceptions are caught and handled.
3. **Modify inputs and introduce errors** to experiment with different exception flows.
4. **Use functions and modules** from the programs to add robust error handling in your projects.
5. **Refer to real-world usage tips** in each program's comments for practical insights.

---

## Example Snippet: Safe Division Function (Program 11)

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

print(safe_divide(10, 2))  # Outputs: 5.0
print(safe_divide(10, 0))  # Outputs error message + None
```

---

## What’s Next?

* Add your own projects applying these exception handling principles
* Extend with multithreading and async exception handling
* Learn to create custom exception classes for clearer error semantics
* Combine with logging, monitoring, and debugging tools in bigger projects

---
