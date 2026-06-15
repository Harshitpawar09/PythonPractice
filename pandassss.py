import pandas as pd
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Vikram'],
    'Age': [22,21,23,20,24],
    'Marks': [85,57,84,84,94],
    'City': ['Bhopal', 'Indore', 'Jbalpur', 'Indore', 'Bhopal']
}
df = pd.DataFrame(data)
print(df)
# print(df.shape)
# print(df.head(3))
# print(df.dtypes)
# print(df.describe)

# #select column
# print("df['Name']: \n", df['Name'])
# print(df[['Name', 'Marks']])

# #Filter Row
# print(df[df['Marks'] >= 85])
# print(df[df['City'] == 'Bhopal'])
# print(df[(df['Marks'] >=80) & (df['City'] == 'Indore' )])
# def get_grade(x):
#     if x >= 90:
#         return 'A'
#     elif x >= 75:
#         return 'B'
#     else:
#         return 'C'
# df['Grade'] = df['Marks'].apply(get_grade)
# print(df['Grade'])
# print(df)





#Group By
city_avg  = df.groupby ('City')['Marks'].mean()
print(city_avg)

# print(df.groupby('City')['Marks'].mean())
#df.groupby('City')['Marks'].mean()

# Read real CSV file
df2 = pd.read_csv('students.csv') 
print(df2)
#Cleaning
df2['Name'] = df2['Name'].str.strip()
df2['Marks'] = df2['Marks'].str.replace('#', '')
df2['City'] = df2['City'].str.strip()


df2.to_csv('clean_output.csv', index=False)