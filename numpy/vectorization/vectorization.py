# Numpy Vectorization Summary: Essentials Only

import numpy as np

# 1. What is Vectorization?
# - Vectorization allows operations on entire arrays without explicit loops.
# - Makes code more concise and faster.

# 2. Element-wise Operations
# Perform operations on entire arrays at once
arr = np.array([1, 2, 3, 4, 5])

# Add, subtract, multiply, divide
print(arr + 10)  # Output: [11 12 13 14 15]
print(arr * 2)   # Output: [ 2  4  6  8 10]
print(arr ** 2)  # Output: [ 1  4  9 16 25]

# 3. Vectorized Functions
# Use NumPy's built-in functions for operations
print(np.sqrt(arr))  # Output: [1. 1.414 1.732 2. 2.236]
print(np.exp(arr))   # Output: [  2.718  7.389  20.085  54.598 148.413]

# 4. Operations Between Arrays
# Perform operations on two arrays element-wise
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)  # Output: [5 7 9] (element-wise addition)
print(arr1 * arr2)  # Output: [4 10 18] (element-wise multiplication)

# 5. Conditional Operations
# Apply conditions to entire arrays
print(arr[arr > 3])  # Output: [4 5] (filter elements greater than 3)

# 6. Broadcasting
# Perform operations between arrays of different shapes
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([1, 2, 3])

print(arr3 + arr4)
# Output:
# [[ 2  4  6]
#  [ 5  7  9]]

# Key Points to Remember:
# - Vectorization eliminates the need for loops.
# - Use NumPy's built-in functions for performance.
# - Leverage broadcasting for operations on arrays with different shapes.

# Final Tip: Vectorization is essential for writing fast, concise, and efficient numerical code!
