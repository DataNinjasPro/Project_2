# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scipy.stats import sem, ttest_ind

general_heights = pd.read_csv("../Resources/general_heights.csv")

wba_data = pd.read_csv("../Resources/wba_data.csv")
wba_heights = wba_data.iloc[:, -1]

(t_stat, p) = ttest_ind(general_heights, wba_heights, equal_var=False)

# Report
print("The mean height of WBA players is " + str(wba_heights.mean()))
print("The mean height of women sampled is " + str(general_heights.mean()))

if p < 0.05:
    print("The difference in sample means is significant.")
else:
    print("The difference in sample means is not significant.")

# Plot sample means with error bars
tick_labels = ["General Public", "WBA Players"]

means = [np.mean(general_heights), np.mean(wba_heights)]
x_axis = np.arange(0, len(means), 1)

sem = [sem(general_heights), sem(wba_heights)]

# Plot
plt.errorbar(x_axis, means, yerr=sem, fmt="o")
plt.title("Mean Height of Women in General Population and WBA Players")

plt.xlim(-0.5, 1.5)
plt.ylim(64, 73)

plt.xticks(x_axis, tick_labels)

plt.ylabel("Height (Inches)")

plt.show()
