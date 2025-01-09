# Pandas loc Summary: Essentials Only
#loc[row_label, column_label]

import pandas as pd
from space import space

# Create a DataFrame for demonstration
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data, index=['a', 'b', 'c'])
space()
print(df)
space()

# 1. Selecting Rows by Label
# Select a single row by label (returns a Series)
print(df.loc['a'])  # Output: Row with label 'a' (Alice's details)
space()
#
# # Select multiple rows by labels
print(df.loc[['a', 'b'],['Age','City']])  # Output: Rows 'a' and 'b' (Alice and Bob's details)
space()
#
# # 2. Selecting Columns by Label
# # Select a specific column using column label
print(df.loc[:, 'Age'])  # Output: All rows for the 'Age' column
space()
#
# # Select multiple columns by labels
print(df.loc[:, ['Name', 'City']])  # Output: All rows for 'Name' and 'City' columns
space()
#
# # 3. Selecting Specific Rows and Columns
# # Use row and column labels to get a specific value
print(df.loc['b', 'City'])  # Output: 'Los Angeles'
space()
#
# # Select a subset of rows and columns
print(df.loc['a':'b', 'Name':'City'])  # Output: Rows 'a' to 'b' for columns 'Name' to 'City'
space()

# # 4. Conditional Selection
# # Select rows based on a condition
print(df.loc[df['Age'] > 25])  # Output: Rows where 'Age' is greater than 25
#
# # Key Points to Remember:
# # - Use loc[row_label, column_label] to select data by labels.
# # - Row labels go first, column labels second.
# # - Supports slicing with labels and conditions for filtering.
#
# # Final Tip: Master loc for label-based indexing and filtering efficiently!
