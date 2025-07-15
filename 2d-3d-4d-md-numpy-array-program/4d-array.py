import numpy as np

def practical_4d_array_operations():
    print("📦 4D ARRAY CREATION AND OPERATIONS")

    # Step 1: Get array dimensions from user
    dim1 = int(input("Enter size for Dimension 1 (e.g., number of datasets): "))
    dim2 = int(input("Enter size for Dimension 2 (e.g., number of blocks per dataset): "))
    dim3 = int(input("Enter size for Dimension 3 (e.g., number of rows per block): "))
    dim4 = int(input("Enter size for Dimension 4 (e.g., number of columns per row): "))

    total_elements = dim1 * dim2 * dim3 * dim4

    print(f"\nPlease enter {total_elements} integers to fill a {dim1}x{dim2}x{dim3}x{dim4} array.")
    user_data = list(map(int, input("Enter the numbers separated by space:\n").split()))

    if len(user_data) != total_elements:
        print(f"❌ Error: Expected {total_elements} values, but got {len(user_data)}.")
        return

    # Step 2: Create the 4D NumPy array
    array_4d = np.array(user_data).reshape(dim1, dim2, dim3, dim4)
    
    print("\n✅ 4D Array Created Successfully!")
    print("Shape of array:", array_4d.shape)

    # Step 3: Basic Indexing and Slicing
    print("\n🔹Slicing [first dataset, first block]:\n", array_4d[0, 0])

    # Step 4: Iterating over the first dimension (datasets)
    print("\n🔹Iterating over each dataset:")
    for i, dataset in enumerate(array_4d):
        print(f"\nDataset {i+1}:\n", dataset)

    # Step 5: Flatten the array
    flat_array = array_4d.flatten()
    print("\n🔹Flattened 1D View of All Elements:\n", flat_array)

    # Step 6: Filtering values > 100
    filtered = array_4d[array_4d > 100]
    print("\n🔹Filtered Values (greater than 100):\n", filtered if filtered.size else "No values > 100")

    # Step 7: Show reshaped view (optional reshape to 2D for display)
    print("\n🔹Reshaped to 2D (rows of fixed 10 elements):")
    reshaped = flat_array.reshape(-1, 10) if flat_array.size % 10 == 0 else flat_array.reshape(-1, 5)
    print(reshaped)

# Run the function
practical_4d_array_operations()
