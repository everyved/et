import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [3, 1, 4],
    'B': [2, 5, 1],
    'C': [9, 6, 8]
})

print(df)

# Sort the rows by column 'A'
sorted_df = df.sort_values(by='A')
print('\n-----------------\n')
print(sorted_df)

# Sort by multiple columns, sort priority A>B
# sorted_df_multi = df.sort_values(by=['A', 'B'], ascending=[True, False])
sorted_df_multi = df.sort_values(by=['A', 'B'])
print('\n-----------------\n')
print(sorted_df_multi)

