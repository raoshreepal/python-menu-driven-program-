import numpy as np

n = int(input("Enter size of 1D array: "))
arr = np.array([int(input(f"Element {i+1}: ")) for i in range(n)])
k = int(input("Enter number of splits: "))

parts = np.array_split(arr, k)
for i, part in enumerate(parts):#return row and index both 
    print(f"Part {i+1}:", part)
'''for i in range(len(parts)):
    print(i, parts[i])
'''