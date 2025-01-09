import matplotlib.pyplot as plt

# 2. Line Chart
# Advantages:
# - Ideal for visualizing trends over time or sequential data.
# - Easy to compare multiple data series.
# Use Cases:
# - Stock prices over time, sales trends, or temperature variations.

y2 = [15, 25, 20, 35, 40]
plt.plot(x, y, label='Line 1', marker='o')
plt.plot(x, y2, label='Line 2', linestyle='--', color='red')
plt.title('Multiple Lines Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
