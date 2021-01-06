# Dependencies
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
import pandas as pd

crime_data = pd.read_csv("../Resources/crime_data.csv")

year = crime_data.iloc[:, 0]

violent_crime_rate = crime_data.iloc[:, 3]
(vc_slope, vc_int, _, _, _) = linregress(year, violent_crime_rate)
vc_fit = vc_slope * year + vc_int

murder_rate = crime_data.iloc[:, 5]
(m_slope, m_int, _, _, _) = linregress(year, murder_rate)
m_fit = m_slope * year + m_int

aggravated_assault_rate = crime_data.iloc[:, 9]
(aa_slope, aa_int, _, _, _) = linregress(year, aggravated_assault_rate)
aa_fit = aa_slope * year + aa_int

# Plot violent crime rate
plt.scatter(year, violent_crime_rate, marker="o", color="b")
plt.plot(year, vc_fit, color="b", linestyle='dashed', linewidth=1)
plt.ylabel("Violent Crime Rate")
plt.xlim(min(year), max(year))
plt.title("Violent Crime Rate Over Time")
plt.show()

# Plot murder rate
plt.scatter(year, murder_rate, marker="o", color="r")
plt.plot(year, m_fit, color="r", linestyle='dashed', linewidth=1)
plt.ylabel("Murder Rate")
plt.xlim(min(year), max(year))
plt.title("Murder Rate Over Time")
plt.show()

# Plot aggravated assault rate
plt.scatter(year, aggravated_assault_rate, marker="o", color="g")
plt.plot(year, aa_fit, color="g", linestyle='dashed', linewidth=1)
plt.ylabel("Aggravated Assault Rate")
plt.xlim(min(year), max(year))
plt.title("Aggravated Assault Rate Over Time")
plt.show()

year = 2019
print("The violent crime rate in 2019 will be " + str(vc_slope * year + vc_int) + ".")
print("The murder rate in 2019 will be " + str(m_slope * year + m_int) + ".")
print("The aggravated assault rate in 2019 will be " + str(aa_slope * year + aa_int) + ".")
