import numpy as np

n = int(input("Enter number of elements: "))
arr = np.array([int(input(f"Element {i+1}: ")) for i in range(n)])
threshold = int(input("Enter threshold to filter > : "))

mask = arr > threshold
print("Mask:",mask)
filtered = arr[mask]

print("Original:", arr)
print(f"Filtered (> {threshold}):", filtered)
