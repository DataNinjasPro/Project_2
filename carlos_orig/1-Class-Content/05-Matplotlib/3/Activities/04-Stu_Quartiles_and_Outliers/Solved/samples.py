# Dependencies
import matplotlib.pyplot as plt
import numpy as np

arr = [8, 8, 12, 24, 54, 54, 75, 78, 98, 102, 132]
x_axis = np.arange(0, len(arr), 1)

# Calculate the indices for the lower and upper quartiles
lower_quartile_index = 2
upper_quartile_index = 8

# Retrieve the lower and upper quartiles
lower_quartile = arr[lower_quartile_index]
upper_quartile = arr[upper_quartile_index]

# Calculate the interquartile range
iqr = upper_quartile - lower_quartile

# Create axes for the included and excluded data
included = arr[2:9]
included_axis = np.arange(2, 9, 1)

excluded_low = arr[0:2]
low_axis = np.arange(0, 2, 1)

excluded_high = arr[9:11]
high_axis = np.arange(9, 11, 1)

# Create a plot displaying included and excluded data
plt.plot(included_axis, included, marker='o', color='b')
plt.scatter(low_axis, excluded_low, marker='o', color='r')
plt.scatter(high_axis, excluded_high, marker='o', color='r')

plt.title("Interquartile Range Example")

plt.show()

# Report descriptions of the data
print("The lowr quartile of the data is " + str(lower_quartile))
print("The upper quartile of the data is " + str(upper_quartile))
print("The interquartile range of the data is " + str(iqr))
