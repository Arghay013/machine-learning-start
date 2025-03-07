import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)



# Selecting columns
print(df['Name'])  

# Selecting multiple columns
print(df[['Name', 'Age']])

# Filtering rows
print(df[df['Age'] > 30])

# Using loc and iloc
print(df.loc[0])  # Select row by index
print(df.iloc[1, 1])  # Select specific value
