import pandas as pd
from space import space

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}

df=pd.DataFrame(data)
print(df )
# space()
#
# df=df[df['Age']>25]
# print(df)
# space()
# df=df[(df['Age']>25) & (df['Salary']>60000)]
# print(df )

df=df[(df['Name']=='David')|(df['Name']=='Bob')]
space()
print(df)
