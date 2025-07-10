import numpy as np

# Input
n = int(input("Enter number of elements: "))
arr = np.array([int(input(f"Element {i+1}: ")) for i in range(n)])

# Indexing
idx = int(input(f"Enter index to access (0 to {n-1}): "))
if 0 <= idx < n:
    print("Element at index", idx, "is", arr[idx])
else:
    print("Index out of range.")
