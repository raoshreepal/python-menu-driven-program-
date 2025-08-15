# Program to catch KeyError when accessing a missing dictionary key

person = {'name': 'Alice', 'age': 30}

try:
    print(person['email'])  # 'email' key doesn't exist
except KeyError:
    print("Error: Key not found in dictionary.")
