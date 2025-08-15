my_list = [10, 20, 30]

try:
    # Trying to access an invalid index
    print(my_list[5])
except IndexError as e:
    print("Caught an IndexError!")
    print("Error message:", e)
