import matplotlib.pyplot as plt

# 6. Box Plot
# Used to visualize the distribution, median, and outliers of a dataset.
data = [7, 8, 9, 10, 10, 11, 13, 13, 14, 15, 16, 16, 17, 18, 19]
# plt.boxplot(data, vert=True, patch_artist=True, notch=True, boxprops=dict(facecolor='lightblue'))
plt.boxplot(data)
plt.title('Box Plot Example')
plt.xlabel('Dataset')
plt.ylabel('Values')
plt.grid(True)
plt.show()
