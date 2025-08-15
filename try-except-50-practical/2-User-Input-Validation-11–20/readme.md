
# 🎯 User Input Validation in Python (Programs 11–20)

Mastering user input validation is key to writing **reliable, user-friendly, and secure** Python applications. This section demonstrates how to validate different types of input, handle common errors, and make your CLI programs bulletproof!

---

## 🔢 Program Descriptions

### 11. 🧮 Input Validation for Integers

```python
int(input("Enter an integer: "))
```

✅ **Handles:** `ValueError`
💡 **Use Case:** Prevents app crashes when users enter non-integer values.

---

### 12. 🔁 Repeated Input Until Valid

```python
while True: try: ...
```

✅ **Handles:** Repeated retries until input is valid
💡 **Use Case:** Input forms, quiz apps, games requiring numeric input.

---

### 13. ⏳ Limit Input Attempts

```python
while attempts < max_attempts:
```

✅ **Handles:** Retry logic with a limit
💡 **Use Case:** Login systems, ATM PIN inputs, quizzes with timeouts.

---

### 14. 🔐 Password Match Validation

```python
if password1 != password2:
    raise ValueError
```

✅ **Handles:** Password mismatch
💡 **Use Case:** Signup pages, user account creation, password reset forms.

---

### 15. 🔢 Convert String to Float Safely

```python
float(input("Enter a float: "))
```

✅ **Handles:** `ValueError`
💡 **Use Case:** Accepting decimal input in billing, pricing, measurements.

---

### 16. 🎂 Check Age (Must Be > 0)

```python
if age <= 0:
    raise ValueError
```

✅ **Handles:** Negative or zero values
💡 **Use Case:** Age validation in sign-up forms, medical or legal apps.

---

### 17. 📅 Validate Date Format

```python
datetime.strptime(date_str, "%Y-%m-%d")
```

✅ **Handles:** Wrong format (e.g., 15/08/2025)
💡 **Use Case:** Event scheduling, calendars, reminders.

---

### 18. 🪵 Log Exceptions to a File

```python
with open("error_log.txt", "a")
```

✅ **Handles:** All runtime exceptions
💡 **Use Case:** Debugging and error tracking in deployed applications.

---

### 19. 🎯 Custom Message per Exception

```python
except ValueError, TypeError, ZeroDivisionError
```

✅ **Handles:** Multiple errors, each with a unique message
💡 **Use Case:** Teaching, user-friendly CLI tools, interpreters.

---

### 20. ⌨️ Handle Keyboard Interrupt Gracefully

```python
except KeyboardInterrupt:
```

✅ **Handles:** Ctrl+C interruption
💡 **Use Case:** CLI apps, servers, loops that run until user exits.

---

## 🧠 What You Learn from These Programs

* ✔️ Defensive programming techniques
* 🛑 Error handling best practices
* 🧼 User input sanitization
* 🔄 Retry patterns & graceful failures
* 📋 Logging and debugging

---

## 🌍 Real-World Application Areas

| Area                     | How It Helps                          |
| ------------------------ | ------------------------------------- |
| Web forms (Flask/Django) | Prevent invalid submissions           |
| CLI tools                | Create robust command-line interfaces |
| APIs                     | Handle bad input in endpoints         |
| Finance apps             | Validate float and integer inputs     |
| Healthcare/Legal         | Strict age/date validations           |
| DevOps scripts           | Gracefully handle user interrupts     |

