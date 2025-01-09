import pandas as pd
from space import space
a={
 'Category': ['A', 'A', 'B', 'B', 'C'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X'],
    'Values': [10, 20, 30, 40, 50]
}
df=pd.DataFrame(a)
space()
print(df)

#grouping by Category and Subcategory
b=df.groupby(['Category','Subcategory']).agg(['mean','sum'])
space()
print(b)

# resetting index
c=b.reset_index()
space()
print(c)
