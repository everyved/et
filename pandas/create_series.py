import pandas as pd

# Create a Series from a list
data = [10, 20, 30, 40]
series = pd.Series(data)  # default index
series2 = pd.Series(data, index=['a', 'b', 'c', 'd'])  # Optional custom index
print(series)
print(series2)
