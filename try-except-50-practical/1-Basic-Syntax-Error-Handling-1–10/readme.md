
# 🛠️ Python Basics – Syntax & Error Handling (Programs 1–10)

Get hands-on experience with Python’s **core error handling features**. This set covers everything from catching specific exceptions to using `finally` blocks and raising your own errors, perfect for beginners and intermediate devs alike.

---

## 📚 Program Summaries

### 1️⃣ Basic Try-Except: Division

*Catch division by zero to avoid crashes.*

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
```

---

### 2️⃣ Catch Multiple Exceptions

*Handle both invalid input and zero division.*

```python
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
```

---

### 3️⃣ Using Else Block

*Run code only when no exceptions occur.*

```python
try:
    result = 20 / 4
except ZeroDivisionError:
    print("Error: Division by zero.")
else:
    print("Success! Result is:", result)
```

---

### 4️⃣ Finally Block

*Execute cleanup regardless of exceptions.*

```python
try:
    result = 15 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
finally:
    print("Done")
```

---

### 5️⃣ Nested Try-Except Blocks

*Manage multiple error sources cleanly.*

```python
try:
    a = int(input("Enter a number: "))
    try:
        result = 100 / a
        print("Result:", result)
    except ZeroDivisionError:
        print("Inner error: Cannot divide by zero.")
except ValueError:
    print("Outer error: Invalid input, not an integer.")
```

---

### 6️⃣ Raise Custom Exception

*Manually enforce constraints.*

```python
age = -5
if age < 0:
    raise ValueError("Custom error: Age cannot be negative.")
else:
    print("Age is valid.")
```

---

### 7️⃣ Handle IndexError

*Catch invalid list index access.*

```python
my_list = [10, 20, 30]
try:
    print(my_list[5])
except IndexError as e:
    print("Caught an IndexError!")
    print("Error message:", e)
```

---

### 8️⃣ Handle KeyError

*Safely access dictionary keys.*

```python
person = {'name': 'Alice', 'age': 30}
try:
    print(person['email'])
except KeyError:
    print("Error: Key not found in dictionary.")
```

---

### 9️⃣ Handle TypeError

*Catch invalid type operations.*

```python
try:
    result = 10 + "5"
except TypeError:
    print("Error: Cannot add integer and string.")
```

---

### 🔟 Catch All Exceptions

*Generic error handler for unexpected errors.*

```python
try:
    a = int("abc")
except Exception as e:
    print("An error occurred:", e)
```

---

## 🎯 Key Takeaways

| Concept                     | Real-World Use Case                           |
| --------------------------- | --------------------------------------------- |
| Specific exception handling | Prevent crashes and give clear error messages |
| Using `else` block          | Separate success logic cleanly                |
| `finally` block             | Ensure cleanup tasks always run               |
| Nested exceptions           | Handle layered operations and failures        |
| Raising exceptions          | Enforce custom business rules                 |
| Handling common errors      | Prevent app from breaking on bad input        |

---

## 🚀 Where This Is Used in Real Projects

* **Web Apps:** Validating user inputs in forms
* **Data Processing:** Handling bad data in ETL pipelines
* **CLI Tools:** Robust command line programs with user prompts
* **Financial Software:** Prevent divide by zero in calculations
* **APIs:** Graceful error responses to invalid client requests
* **Games & Simulations:** Handling unexpected inputs or states

