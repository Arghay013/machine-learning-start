
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)

# Check for missing values
print(df.isnull().sum())

# Fill missing values
df.fillna(0, inplace=True)

# Drop missing values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)
