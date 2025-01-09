#creating array
import numpy as np

# Create a 1D array from a list
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Create a 2D array from a list of lists
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# Array of zeros
zeros = np.zeros((2, 3))  # 2 rows, 3 columns
print("Array of Zeros:\n", zeros)

# Array of ones
ones = np.ones((3, 2))  # 3 rows, 2 columns
print("Array of Ones:\n", ones)

# Array with a range of numbers
range_array = np.arange(1, 10, 2)  # Start=1, Stop=10, Step=2
print("Range Array:", range_array)

# Array with evenly spaced numbers
linspace_array = np.linspace(0, 1, 5)  # Start=0, Stop=1, 5 points
print("Linspace Array:", linspace_array)


