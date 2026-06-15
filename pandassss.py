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

#select column
print("df['Name']: \n", df['Name'])
print(df[['Name', 'Marks']])

#Filter Row
print(df[df['Marks'] >= 85])
print(df[df['City'] == 'Bhopal'])
print(df[(df['Marks'] >=80) & (df['City'] == 'Indore' )])
def get_grade(x):
    if x >= 90:
        return 'A'
    elif x >= 75:
        return 'B'
    else:
        return 'C'
df['Grade'] = df['Marks'].apply(get_grade)
print(df['Grade'])
print(df)