import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Vikram'],
    'Age': [22,21,23,20,24],
    'Marks': [85,57,84,84,94],
    'City': ['Bhopal', 'Indore', 'Jbalpur', 'Indore', 'Bhopal']
}
df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.head(3))
print(df.dtypes)
print(df.describe)