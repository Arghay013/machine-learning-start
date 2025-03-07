import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)
# Group by column
grouped = df.groupby('Age').mean()

# Aggregation functions
df.groupby('Age').agg({'Salary': 'sum'})
