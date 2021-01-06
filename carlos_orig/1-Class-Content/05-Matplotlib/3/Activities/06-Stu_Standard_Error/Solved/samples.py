# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import sem

# Read data
housing_data = pd.read_csv("../Resources/housing_data.csv")
housing_data = housing_data.sample(frac=1).reset_index(drop=True)

# Create a bunch of samples, each with div items
div = 20
lim = len(housing_data) // div
samples = [housing_data.iloc[(i * div):(i * div + div), 13]
           for i in range(0, lim)]

# Calculate means
means = [np.mean(s) for s in samples]

# Calculate standard error on means
sem = [sem(s) for s in samples]

# Plot sample means with error bars
plt.errorbar(np.arange(0, len(means)), means, yerr=sem, fmt="o", color="b", alpha=0.5)

plt.xlim(-0.5, len(means))

plt.xlabel("Sample Number")
plt.ylabel("Mean of Median House Prices")

plt.show()
