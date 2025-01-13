# 4. Pie Chart
# Used to show proportions of a whole.
import matplotlib.pyplot as plt

labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [30, 20, 25, 25]
colors = ['gold', 'lightblue', 'lightgreen', 'pink']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart Example')
plt.show()
