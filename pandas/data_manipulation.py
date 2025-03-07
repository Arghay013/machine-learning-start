import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)
# Add new column
df['Salary'] = [50000, 60000, 70000]

# Update values
df.loc[df['Name'] == 'Alice', 'Age'] = 26

# Apply functions
df['Age'] = df['Age'].apply(lambda x: x + 1)
