import pandas as pd

# Creating a Series
s = pd.Series([1, 2, 3, 4, 5])
print(s)

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)
print(df)
