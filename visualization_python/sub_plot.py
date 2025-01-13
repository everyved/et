# 5. Subplots
# Used to display multiple charts in a single figure.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
plt.plot(x, y1, label='Quadratic', color='purple')
plt.title('Quadratic')
plt.grid(True)

plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
plt.plot(x, y2, label='Linear', color='orange')
plt.title('Linear')
plt.grid(True)

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
