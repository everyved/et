import pandas as pd
from space import space

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)
print(df)
space()

# Attributes
print("Index:", df.index)         # Index: RangeIndex(start=0, stop=3, step=1)
space()

print("Columns:", df.columns)     # Columns: Index(['Name', 'Age', 'Salary'], dtype='object')
space()
 
print("Shape:", df.shape)         # Shape: (3, 3)
space()

print("Data Types:\n", df.dtypes) # Data Types of columns
space()

print("Values:\n", df.values)     # Underlying data as NumPy array
space()

print("Size:", df.size)           # Total elements: 9
space()

print("Transpose:\n", df.T)       # Transposed DataFrame
