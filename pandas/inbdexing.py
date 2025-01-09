import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])

# Select a single row by label
print(df.loc['A'])


# Select rows 'A' to 'C' and the 'Name' and 'Salary' columns
print('\nSelect rows A to C and the Name and Salary columns')
print(df.loc['A':'C', ['Name', 'Salary']])
