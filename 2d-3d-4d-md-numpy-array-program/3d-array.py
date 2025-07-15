import numpy as np
def practical_3d():
    depth = int(input("Enter depth: "))
    rows = int(input("Enter rows: "))
    cols = int(input("Enter columns: "))
    total = depth * rows * cols
    data = list(map(int, input(f"Enter {total} integers: ").split()))
    arr = np.array(data).reshape(depth, rows, cols)

    print("🔹Original 3D Array:\n", arr)
    print("Shape:", arr.shape)

    part1, part2 = np.array_split(arr, 2)
    print("🔹Split Part 1:\n", part1)
    print("🔹Split Part 2:\n", part2)

    joined = np.concatenate((part1, part2), axis=0)
    print("🔹Rejoined Array:\n", joined)

    val = int(input("Enter value to search: "))
    loc = np.where(arr == val)
    print("🔹Value found at indices:", list(zip(*loc)))

practical_3d()
