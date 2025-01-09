import pandas as pd
from space import space

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
print(df)
space()

# Select rows where Age > 30
print('\nSelect rows where Age > 30')
result = df[df['Age'] > 30]
print(result)

# Select rows where Age > 30 AND Salary > 60000
print('\nSelect rows where Age > 30 AND Salary > 60000')
result = df[(df['Age'] > 30) & (df['Salary'] > 60000)]
print(result)

# Select rows where Age < 30 OR Salary > 70000
print('\nSelect rows where Age < 30 OR Salary > 70000')
result = df[(df['Age'] < 30) | (df['Salary'] > 70000)]
print(result)

# Select rows where Age > 30 and return only 'Name' and 'Salary' columns
# print('\nSelect rows where Age > 30 and return only Name and Salary columns')
# result = df.loc[df['Age'] > 30, ['Name', 'Salary']]
# # result = df.loc[:, ['Name', 'Salary']]
# print(result)

# Select rows where Name is 'Alice' or 'David'
# --->note: we can just use the | operation
print('\nSelect rows where Name is Alice or David')
result = df[df['Name'].isin(['Alice', 'David'])]
print(result)
