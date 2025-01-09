import pandas as pd
from space import space

# Create a DataFrame with sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 28],
    'Salary': [50000, 60000, 70000, 80000, 55000],
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']
}

df = pd.DataFrame(data)
print(df)
space()

# # 1. Display the first n rows (default n=5)
print(df.head(5))
space()
#
# # 2. Display the last n rows
print(df.tail(5))
space()
#
# # 3. Summary of the DataFrame, including data types
df.info()
space()
#
# # 4. Summary statistics for numerical columns
print(df.describe())
space()
#
# # 5. Return a random sample of n rows
print(df.sample(3))
