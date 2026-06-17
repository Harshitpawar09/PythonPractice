import matplotlib.pyplot as plt


# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# sales = [45,52,48,61,58,72,69,75,68,82,99,95]
# #Line Chart
# plt.figure(figsize = (12,5))
# plt.plot(months, sales, marker= 'o', color='steelblue', linewidth=2, markersize=8)
# plt.fill_between(months, sales, alpha=0.15, color='steelblue')
# plt.title('monthly sales 2024 (Rs. Thousand)', fontsize=14, fontweight='bold')
# plt.xlabel('Month')
# plt.ylabel('Sales (Rs. K)')
# plt.grid(True, alpha=0.3)
# plt.tight_layout()
# plt.show()


# cities = ['Bhopal', 'Indore', 'Jabalpur', 'Gwalior', 'Ujjain']
# students = [1200,2800,980,850,650]
# colors = ['#2196F3', '#4CAF50','#FF9800', '#9C2780','#F44336']
# plt.figure(figsize=(9,5))
# bars = plt.bar(cities, students, color=colors, edgecolor='white',linewidth=1.5)
# plt.title('students enrolled per city')
# plt.ylabel('Number of students')
# for bar,val in zip(bars,students):
#     plt.text(bar.get_x()+bar.get_width()/2, val+30, str(val), ha='center', fontweight='bold')
# plt.tight_layout()
# plt.show()


import numpy as np
# study_hrs = np.random.uniform(2,10,50)
# marks = study_hrs * 7 + np.random.normal(0,8,50)
# marks = np.clip(marks,30,100)
# plt.figure(figsize=(8,5))
# plt.scatter(study_hrs, marks, c= marks, cmap='RdYlGn', s=100, alpha=0.8)
# plt.colorbar(label='marks')
# plt.title('Study hours vs exam marks')
# plt.xlabel('Study hours/day')
# plt.ylabel('Exam marks')
# plt.show()



import seaborn as sns
import pandas as pd
# np.random.seed(42)
# df = pd.DataFrame({
#     'marks': np.random.randint(40,100,100),
#     'study_hours': np.random.uniform(2,10,100),
#     'city': np.random.choice(['Bhopal', 'Indore', 'Jabalpur'],100),
#     'gender': np.random.choice(['male','Female'],100)})
# plt.figure(figsize=(10,4))
# sns.histplot(df['marks'], bins = 20, kde =True, color='steelblue')
# plt.title('Distribution of student marks')
# plt.show()



# sns.boxplot(data=df, x='city', y='marks', palette='Set2')
# plt.title('Marks distribution by city')
# plt.show()


# plt.figure(figsize=(5,4))
# sns.heatmap(df[['marks', 'study_hours']].corr(),annot=True,cmap='coolwarm', vmin=-1,  vmax=1)
# plt.title('Correlation Matrix')
# plt.show()


# sns.pairplot(df[['marks', 'study_hours']], diag_kind='kde')
# plt.show()


