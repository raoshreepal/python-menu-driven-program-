import numpy as np

def practical_2d():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    data = list(map(int, input(f"Enter {rows * cols} integers: ").split()))
    arr = np.array(data).reshape(rows, cols)

    print("🔹Original Array:\n", arr)
    print("Shape:", arr.shape)

    print("🔹Sliced [first 2 rows]:\n", arr[:2])
    print("🔹Element at (1,1):", arr[1, 1])
    
    arr_copy = arr.copy()
    arr_view = arr.view()
    arr_copy[0, 0] = 999
    arr_view[1, 1] = 888

    print("🔹Copy (independent):\n", arr_copy)
    print("🔹View (linked):\n", arr_view)

    print("🔹Iterating:")
    for row in arr:
        print(row)

    print("🔹Sorted each row:\n", np.sort(arr))

    filtered = arr[arr > 50]
    print("🔹Filtered > 50:\n", filtered)

practical_2d()
