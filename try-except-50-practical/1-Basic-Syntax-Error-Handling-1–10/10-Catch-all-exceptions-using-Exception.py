# Program to catch any kind of exception using a generic handler

try:
    a = int("abc")  # This will raise ValueError
except Exception as e:
    print("An error occurred:", e)
