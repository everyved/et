import pandas as pd
from space import space

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'C'],
    'Values': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
print(df )

# Group by 'Category' and calculate the sum
grouped_sum = df.groupby('Category').mean()
grouped_sum2 = df.groupby('Category').sum()
group_sum3=df.groupby('Category').agg(['mean','sum','count','median'])

space()
print(grouped_sum)
space()
print(grouped_sum2)
space()
print(group_sum3)
