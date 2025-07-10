import numpy as np

# -----------------------------------------
# Step 1: User-defined Input for Array
# -----------------------------------------
n = int(input("Enter total number of elements (must equal rows * columns): "))

# Input the elements
elements = []
print(f"Enter {n} integer elements:")
for i in range(n):
    val = int(input(f"Element {i+1}: "))
    elements.append(val)

# -----------------------------------------
# Step 2: Reshape Array to 2D
# -----------------------------------------
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

if r * c != n:
    print("❌ Error: Rows * Columns must equal the number of elements.")
    exit()

# Reshape array
arr = np.array(elements).reshape((r, c))
print("\n✅ Reshaped 2D Array:")
print(arr)

# -----------------------------------------
# Step 3: Sort the Array
# -----------------------------------------
axis = int(input("\nEnter axis to sort (0 = column-wise, 1 = row-wise): "))

# Sort using np.sort
sorted_arr = np.sort(arr, axis=axis)
print("\n✅ Sorted Array:")
print(sorted_arr)

# -----------------------------------------
# Step 4: Search for a Value
# -----------------------------------------
x = int(input("\nEnter value to search in the array: "))

# Find locations using np.where
loc = np.where(sorted_arr == x)

# Display results
if loc[0].size > 0:
    positions = list(zip(loc[0], loc[1]))
    print(f"\n✅ Value {x} found at positions (row, column): {positions}")
else:
    print(f"\n❌ Value {x} not found in the array.")
