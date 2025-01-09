import pandas as pd
from space import space

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
space()
print(df)
space()

# Add a new column with a scalar value
# df['Salary'] = 50000  # Assign the same salary to all rows
df['Salary'] = [50000,34,56]  # Assign different salaries to everyone using a list
# df['Salary'] = [5000,34,56]  # update the column
print(df)
space()

# Add a column with a list
df['Department'] = ['HR', 'IT', 'Finance']
print(df)

