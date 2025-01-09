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

# Drop the 'Salary' column
# axis=1: Specifies that you're dropping columns (use axis=0 to drop rows).
df_without_salary = df.drop('Salary', axis=1)
print(df)
space()

# Drop 'Age' and 'Salary' columns
df_without_age_salary = df.drop(['Age', 'Salary'], axis=1)
print(df_without_age_salary)
