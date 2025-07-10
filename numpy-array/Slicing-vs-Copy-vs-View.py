import numpy as np

# Fixed array
arr = np.array([10, 20, 30, 40, 50, 60])
print("Original:", arr)

# User chooses slicing range
start = int(input("Enter slice start index: "))
end = int(input("Enter slice end index (exclusive): "))

# User chooses type
choice = input("Type 'view' or 'copy': ").strip().lower()
if choice == 'view':
    sub = arr[start:end]
    print("You chose view.")
elif choice == 'copy':
    sub = arr[start:end].copy()
    print("You chose copy.")
else:
    print("Invalid choice, defaulting to view.")
    sub = arr[start:end]

print("Sub-array before change:", sub)
# Modify original
mod_idx = int(input("Enter index in original to modify: "))
new_val = int(input("Enter new value: "))
if 0 <= mod_idx < arr.size:
    arr[mod_idx] = new_val
    print("Original after change:", arr)
    print("Sub-array now:", sub)
else:
    print("Index out of range.")
