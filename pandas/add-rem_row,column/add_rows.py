import pandas as pd
from space import space

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30],
    'Salary': [50000, 60000]
}
df = pd.DataFrame(data)
print(df)
space()

# Add a new row
df.loc[len(df)] = ['Charlie', 35, 70000]
# df.loc[1] = ['Chhharlie', 35, 70000] #update a row
print(df)
space()

# New rows as a DataFrame
new_rows = pd.DataFrame({
    'Name': ['David', 'Eva'],
    'Age': [40, 28],
    'Salary': [80000, 55000]
})

# Concatenate the DataFrames
df2 = pd.concat([df, new_rows])
print(df2)
space()

# Add a row from a lis
