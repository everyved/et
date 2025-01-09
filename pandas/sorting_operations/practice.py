import pandas as pd
from space import space
a={
    'a':[1,35,2,13,4],
    'c':[1,35,2,13,4],
    'b':[1,35,2,13,4]
}

df=pd.DataFrame(a)
print(df)
space()

df=df.sort_index(axis=1)
print(df)

df=df.sort_values(by='a')
space()
print(df)
