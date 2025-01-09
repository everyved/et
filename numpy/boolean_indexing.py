# Numpy Boolean Indexing Summary

import numpy as np

# Create a NumPy array for demonstration
arr = np.array([10, 20, 30, 40, 50])

# 1. Boolean Indexing Basics
# Create a boolean condition
condition = arr > 30  # Check where elements are greater than 30
print(condition)  # Output: [False False False  True  True]

# Use the condition to filter elements
filtered = arr[condition]
print(filtered)  # Output: [40 50]

# 2. Combining Conditions
# Use logical operators (&, |) to combine conditions
combined_condition = (arr > 20) & (arr < 50)  # Between 20 and 50
print(arr[combined_condition])  # Output: [30 40]

# 3. Modifying Elements with Boolean Indexing
# Set all elements greater than 30 to 100
arr[arr > 30] = 100
print(arr)  # Output: [ 10  20  30 100 100]

# 4. Boolean Indexing in 2D Arrays
# Create a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Filter elements greater than 5
print(arr_2d[arr_2d > 5])  # Output: [6 7 8 9]

# Key Points to Remember:
# - Boolean indexing is used to filter or modify elements in arrays.
# - Use conditions to create a boolean mask.
# - Combine multiple conditions using logical operators (&, |).
# - Works with both 1D and 2D arrays for flexible filtering.
