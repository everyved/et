import pandas as pd
from space import space

# Sample DataFrame
df = pd.DataFrame({
    'a': [3, 1, 4],
    'c': [2, 5, 1],
    'b': [9, 6, 8]
},index=['z', 'y', 'x'])

print(df)
space()

sorted_columns = df.sort_index(axis=1)
print(sorted_columns)

# Sort rows by index
sorted_rows = df.sort_index(axis=0)
space()
print(sorted_rows)
