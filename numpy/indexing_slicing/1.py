# Numpy Indexing and Slicing Summary: Essentials Only

import numpy as np

# 1. Indexing 1D Arrays
arr = np.array([10, 20, 30, 40, 50])
print(arr)

# Access a single element by index
print(arr[0])  # Output: 10 (first element)
print(arr[-1])  # Output: 50 (last element)

# 2. Slicing 1D Arrays
# Slicing syntax: arr[start:stop:step]
print(arr[1:4])  # Output: [20 30 40] (from index 1 to 3)
print(arr[:3])  # Output: [10 20 30] (from start to index 2)
print(arr[::2])  # Output: [10 30 50] (every second element)

# 3. Indexing 2D Arrays
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)

# Access a single element by row and column indices
print(arr_2d[1, 2])  # Output: 6 (element at row 1, column 2)

# Access an entire row
print(arr_2d[0])  # Output: [1 2 3] (first row)

# Access an entire column
print(arr_2d[:, 1])  # Output: [2 5 8] (second column)

# 4. Slicing 2D Arrays
# Slice rows and columns
print(arr_2d[0:2, 1:3])  # Output: [[2 3] [5 6]] (rows 0-1, columns 1-2)

# Key Points to Remember:
# - Use `arr[index]` for 1D arrays.
# - Use `arr[start:stop:step]` for slicing.
# - For 2D arrays, use `arr[row_index, col_index]` for single elements.
# - Slice rows and columns with `arr[start_row:stop_row, start_col:stop_col]`.

# Final Tip: Master indexing and slicing to efficiently manipulate NumPy arrays!
