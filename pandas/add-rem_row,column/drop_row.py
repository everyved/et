import pandas as pd
from space import space

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)
print(df)
space()

# Drop the row with index 1 (Bob)
df_without_row = df.drop(1, axis=0)
print(df_without_row)
space()

# Drop rows with index 0 and 2 (Alice and Charlie)
# df_without_rows = df.drop([0, 2], axis=0)
df_without_rows = df.drop([0, 2], axis=0)
print(df_without_rows)
space()

# Drop rows where Age > 30
df_condition = df[df['Age'] <= 30]
print(df_condition)

