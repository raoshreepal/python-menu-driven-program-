import numpy as np

n = int(input("Enter array length: "))
arr = np.array([int(input(f"Value {i+1}: ")) for i in range(n)])

x = int(input("Enter value to search: "))
idxs = np.where(arr == x)[0]
if idxs.size > 0:
    print(f"Value {x} found at positions:", idxs)
else:
    print(f"{x} not found in array.")

cond = int(input("Enter threshold to test any greater than: "))
print("Any greater than", cond, "?:", np.any(arr > cond))
