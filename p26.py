import matplotlib.pyplot as plt
'''
x=[1, 2, 3, 4, 5]
y=[2, 3, 5, 7, 11]
plt.plot(x, y)
plt.show()
'''
'''
days=[1, 2, 3, 4, 5]
temperature=[22, 24, 19, 23, 25]
plt.plot(days, temperature)
plt.show()
'''
'''
fig, ax = plt.subplots()
months=['jan', 'feb', 'mar', 'apr', 'may', 'jun']
sales=[100, 150, 200, 250, 300, 350]
ax.plot(months, sales)
ax.set_title('Monthly Sales')
ax.set_xlabel('Months')
ax.set_ylabel('Sales (units)')
plt.show()
'''
days=[1, 2, 3, 4, 5.6,7]
week_a=[10,12,11,13,15,17,16]
week_b=[8,9,10,11,12,13,14]
fig, ax = plt.subplots()
ax.plot(days, week_a, label='Week A')
ax.plot(days, week_b, label='Week B')
ax.set_title('Daily Output: Two Weeks')
ax.set_xlabel('Days')
ax.set_ylabel('Output')
ax.legend()
ax.grid(True,alpha=1)
plt.show()