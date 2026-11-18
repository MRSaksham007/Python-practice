'''
import matplotlib.pyplot as plt
subjects=['Math', 'Science', 'English', 'History', 'Art']
marks=[85, 90, 78, 92, 88]
plt.bar(subjects, marks, color='gray', edgecolor='black')
plt.title('Student Marks in Different Subjects')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.show()
'''
'''
import numpy as np 
import matplotlib.pyplot as plt
subjects = ['Math', 'Science', 'English', 'History', 'Art']
section_a = [85, 90, 78, 92, 88]
section_b = [80, 85, 75, 88, 82]
x = np.arange(len(subjects))
w=0.35
plt.bar(x - w/2, section_a, w, label='Section A', color='blue', edgecolor='black', hatch='//')
plt.bar(x + w/2, section_b, w, label='Section B', color='orange', edgecolor='black')
plt.xticks(x, subjects)
plt.ylabel('Marks')
plt.title('Student Marks in Different Subjects')
plt.legend()
plt.show()
'''
'''
import matplotlib.pyplot as plt
marks=[35,42,48,50,52,55,56,58,60,62
       ,65,68,70,72,75,78,80,82,85,88]
plt.hist(marks, bins=[30, 40, 50, 60, 70, 80, 90, 100], color='lightblue', edgecolor='black')
plt.title('Distribution of Student Marks')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
scores = np.array([50, 55, 60, 65, 70, 75, 80, 85])
plt.scatter(hours, scores, color='green', edgecolor='black',s=60)
plt.plot(hours, m * hours + c, 'k--', linestyle='Trend Line')
plt.title('Hours Studied and Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')
plt.legend()
plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt
labels = ['Rent', 'Food', 'Travel', 'Other']
share = [40, 30, 20, 10]
plt.pie(share, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Monthly Expenses')
plt.axis('equal')
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np
class_a=[45, 50, 55, 58, 60, 62, 65, 70, 72, 98]
class_b=[40, 48, 52, 60, 63, 68, 74, 80, 85, 90]
plt.boxplot([class_a, class_b], medianprops=dict(color='red'))
plt.xticks([1, 2], ['Class A', 'Class B'])
plt.title('Box Plot of Student Marks')
plt.ylabel('Marks')
plt.show()
'''
'''
import matplotlib.pyplot as plt
years = [2015, 2016, 2017, 2018, 2019, 2020]
subscr = [20, 35, 50, 80, 95, 110]
plt.fill_between(years, subscr, color='lightgreen', alpha=0.5)
plt.title('Subscription Growth')
plt.xlabel('Years')
plt.ylabel('Subscriptions')
plt.xticks(years)
plt.show()
'''
'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Year': [2015, 2016, 2017, 2018, 2019, 2020],
    'Sales': [120, 150, 180, 200, 220, 250],
    'Profit': [30, 40, 50, 60, 70, 80]
})
df.plot(x='Year', y=['Sales', 'Profit'], kind='line', style=['k=0','k--s'])
plt.title('Sales and Profit')
plt.ylabel('Amount (lakh rs)')
plt.grid(True)
plt.show()
'''
'''
ax=df.plot(x='Year', y=['Sales', 'Profit'], kind='bar', color=['gray', 'white'], edgecolor='black')
ax.set_title('Sales and Profit')
ax.set_ylabel('Amount (lakh rs)')
'''