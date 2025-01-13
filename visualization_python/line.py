import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 12, 15, 18, 20]
y2 = [8, 9, 14, 16, 19]

# plt.plot(x, y1, label='Line 1', linestyle='-', color='blue')
# plt.plot(x, y2, label='Line 2', linestyle='--', color='green')

plt.plot(x, y1,color='blue')
plt.plot(x, y2,color='green')

plt.title('Line Chart: Multiple Lines')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
