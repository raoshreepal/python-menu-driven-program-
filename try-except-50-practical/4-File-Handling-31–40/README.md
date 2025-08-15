

# 📁 Python File Handling – Programs 31 to 40

Welcome to the **File Handling Masterclass** in Python. These examples demonstrate how to **safely read, write, create, check, and manage files** using robust error handling—ideal for both beginners and working developers building real-world apps.

---

## 🔢 Program Descriptions

### 📄 31. Open File Safely

```python
with open("nonexistent_file.txt", "r")
```

✅ **Handles:** `FileNotFoundError`
💡 **Use Case:** Prevent crashes when reading missing files (e.g., logs, configs, user data).

---

### 📖 32. Read From File with Error Check

```python
with open("data.txt", "r")
```

✅ **Handles:** `IOError`
💡 **Use Case:** Protect your app from issues like corrupted files or hardware I/O failures.

---

### ✍️ 33. Write to File & Catch Permission Error

```python
with open("/restricted_file.txt", "w")
```

✅ **Handles:** `PermissionError`
💡 **Use Case:** Writing to system-level files or protected directories in Linux/Windows.

---

### 🔒 34. Handle File Not Closed Properly

```python
try:
    file = open(...)
finally:
    file.close()
```

✅ **Handles:** Any error + ensures closure
💡 **Use Case:** Legacy systems or non-context-managed environments where `with` isn't used.

---

### 🧠 35. Use `with open()` in Try-Except

```python
with open("info.txt", "r")
```

✅ **Handles:** File + I/O errors safely inside a context manager
💡 **Use Case:** Standard best practice in modern Python for safe file operations.

---

### 🔢 36. Read & Parse Integer from File

```python
number = int(file.read())
```

✅ **Handles:** `FileNotFoundError`, `ValueError`
💡 **Use Case:** Reading numeric settings, config files, input data (e.g., age, count).

---

### 📍 37. Check if File Exists Before Open

```python
if os.path.exists(...)
```

✅ **Alternative to:** `try/except FileNotFoundError`
💡 **Use Case:** UI or CLI programs that check before accessing user files.

---

### ✨ 38. Create File if Not Found

```python
except FileNotFoundError:
    open(file_name, "w")
```

✅ **Handles:** File creation if missing
💡 **Use Case:** Bootstrapping apps that auto-generate default configs, logs, etc.

---

### 🧩 39. Handle Large File Reading

```python
chunk = file.read(1024)
```

✅ **Handles:** `MemoryError`, `FileNotFoundError`
💡 **Use Case:** Reading logs, media, or datasets without crashing due to memory overload.

---

### 📝 40. Log File Errors to a Separate Log File

```python
with open("file_error_log.txt", "a")
```

✅ **Handles:** Any exception + logs it
💡 **Use Case:** Production-grade applications where silent fails are not acceptable.

---

## 🌍 Real-World Applications

| Feature             | Example Use Case                    |
| ------------------- | ----------------------------------- |
| `FileNotFoundError` | Missing config/log files            |
| `PermissionError`   | Writing to restricted directories   |
| `ValueError`        | Parsing corrupted input files       |
| `os.path.exists()`  | Pre-check before file operation     |
| Chunked Reading     | Handling large log files / datasets |
| Error Logging       | Generating crash logs for debugging |

---

## 💡 Best Practices Learned

* ✅ Always validate file presence
* 🔁 Use `with open()` for auto-closing
* 🚫 Never assume permissions
* 📋 Log exceptions for auditing
* 💪 Be memory-efficient for large files

