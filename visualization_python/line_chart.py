# Basic Visualization Using Matplotlib

import matplotlib.pyplot as plt

# 1. Components of a Chart
# A chart typically includes:
# - Title: Describes the chart.
# - Axes: X and Y axes to represent data.
# - Labels: Axis labels and data points.
# - Legend: Explains the data series.
# - Grid: Optional gridlines for better readability.

# Example: Adding components to a line chart
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

plt.plot(x, y, label='Line 1', marker='o')
plt.title('Line Chart Example')  # Title
plt.xlabel('X-axis Label')       # X-axis label
plt.ylabel('Y-axis Label')       # Y-axis label
plt.legend()                     # Legend
plt.grid(True)                   # Gridlines
plt.show()
