import pandas as pd
from space import space
data = {
    'Category': ['A', 'A', 'B', 'B', 'C'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X'],
    'Values': [10, 20, 30, 40, 50]
}
df=pd.DataFrame(data)
print(df)
a=df.groupby('Category').agg(['sum'])
space()
print(a)
b=a.reset_index()
space()
print(b)

df['Group_mean']=df.groupby('Category')['Values'].transform('mean')
space()
print(df)
