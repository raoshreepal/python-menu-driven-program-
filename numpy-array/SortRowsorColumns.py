import numpy as np

r, c = map(int, input("Rows columns: ").split())
arr = np.array([int(input()) for _ in range(r*c)]).reshape((r, c))

axis = int(input("Sort along axis (0 for columns, 1 for rows): "))
sorted_arr = np.sort(arr, axis=axis)

print("Original array:\n", arr)
print("Sorted array:\n", sorted_arr)
