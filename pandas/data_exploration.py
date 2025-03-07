import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)
print(df)
df.head()   # First 5 rows
df.tail()   # Last 5 rows
df.info()   # Data type and non-null values
df.describe()  # Summary statistics
df.shape  # Number of rows and columns
df.columns  # Column names
