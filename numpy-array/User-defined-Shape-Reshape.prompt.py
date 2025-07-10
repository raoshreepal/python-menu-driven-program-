import numpy as np

r = int(input("Enter rows: "))
c = int(input("Enter columns: "))
total = r * c

elements = []
print(f"Enter {total} elements:")
for i in range(total):
    elements.append(int(input(f"Element {i+1}: ")))

arr = np.array(elements)
print(arr.size)
if arr.size == total:
    arr = arr.reshape((r, c))
    print("Reshaped array:")
    print(arr)
else:
    print("Element count mismatch.")
print("Shape is:", arr.shape)
