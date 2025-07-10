'''import numpy as np

r = int(input("Enter rows for 2D array: "))
c = int(input("Enter columns: "))
print(f"Enter {r*c} elements for the array:")
elements = [int(input(f"Element {i+1}: ")) for i in range(r*c)]
arr = np.array(elements).reshape((r, c))

total = 0
print("Iterating through array:")
for i, row in enumerate(arr):
    for j, val in enumerate(row):
        print(f"arr[{i},{j}] = {val}")
        total += val

print("Sum of all elements:", total)
'''

import numpy as np

# ---------------------------------------------
# Step 1: Input for First Array
# ---------------------------------------------
print("📌 First Array Input")
r1, c1 = map(int, input("Enter number of rows and columns (e.g., 2 3): ").split())

print(f"Enter {r1 * c1} elements for the first array:")
elements1 = [int(input(f"Element {i+1}: ")) for i in range(r1 * c1)]

# Reshape into 2D
a1 = np.array(elements1).reshape((r1, c1))

print("\n✅ First Array:")
print(a1)

# ---------------------------------------------
# Step 2: Input for Second Array
# ---------------------------------------------
print("\n📌 Second Array Input (same shape required)")
r2, c2 = map(int, input("Enter number of rows and columns (e.g., 2 3): ").split())

if r1 != r2 and c1 != c2:
    print("⚠️ Warning: Arrays must have compatible shapes to join.")

print(f"Enter {r2 * c2} elements for the second array:")
elements2 = [int(input(f"Element {i+1}: ")) for i in range(r2 * c2)]

# Reshape into 2D
a2 = np.array(elements2).reshape((r2, c2))

print("\n✅ Second Array:")
print(a2)

# ---------------------------------------------
# Step 3: Choose Join Axis (0 = vertical, 1 = horizontal)
# ---------------------------------------------
axis = int(input("\n🔄 Enter axis to join (0 = vertical / row-wise, 1 = horizontal / column-wise): "))

# ---------------------------------------------
# Step 4: Perform Joining
# ---------------------------------------------
if axis == 0:
    result = np.vstack((a1, a2))
    print("\n✅ Joined Array (Vertical Stack):")
elif axis == 1:
    result = np.hstack((a1, a2))
    print("\n✅ Joined Array (Horizontal Stack):")
else:
    print("❌ Invalid axis. Use 0 or 1.")
    exit()

# ---------------------------------------------
# Step 5: Display Result
# ---------------------------------------------
print(result)
