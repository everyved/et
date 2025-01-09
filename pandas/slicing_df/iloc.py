# Pandas iloc Summary: Essentials Only
#df.iloc[row_index, column_index]

import pandas as pd
from space import space

# Create a DataFrame for demonstration
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
space()

# 1. Selecting Rows by Index
# Select a single row by index (returns a Series)
print(df.iloc[0])  # Output: First row (Alice's details)
space()

# # Select multiple rows by index
print(df.iloc[0:2])  # Output: Rows 0 and 1 (Alice and Bob's details)
space()
# print(df.iloc[:])  # Output: everything
#
# # 2. Selecting Columns by Index
# # Select a specific column (using row index with column index)
print(df.iloc[:, 1])  # Output: All rows for the 'Age' column
space()
# print(df.iloc[:, :2])  # Output: All rows for the columns 0 to 1(age)
#
# # Select multiple columns
print(df.iloc[:,:2])  # Output: All rows for 'Name' and 'Age' columns
space()
#
# # 3. Selecting Specific Rows and Columns
# # Use row and column indices to get a specific value
print(df.iloc[1, 2])  # Output: 'Los Angeles'
#
# # Select a subset of rows and columns
print(df.iloc[0:2, 1:3])  # Output: Rows 0-1 for columns 'Age' and 'City'
space()
#
# # 4. Negative Indexing
# # Select the last row
print(df.iloc[-1])  # Output: Last row (Charlie's details)
space()
#
# # Select the last column
print(df.iloc[:, -1])  # Output: All rows for the 'City' column
#
# # Key Points to Remember:
# # - Use iloc[row_index, column_index] to select data by numerical indices.
# # - Row index goes first, column index second.
# # - Use slicing for ranges (e.g., 0:2) or single indices.
# # - Negative indices can be used to select rows/columns from the end.
#
# # Final Tip: Master the basics to handle rows and columns efficiently!
