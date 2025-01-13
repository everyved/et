import matplotlib.pyplot as plt

# 3. Scatter Chart
# Used to show the relationship or correlation between two variables.
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]
plt.scatter(x, y, color='red', label='Scatter Points')
#plt.scatter(x, x, color='blue', label='Scatter Points')
plt.title('Scatter Chart Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
