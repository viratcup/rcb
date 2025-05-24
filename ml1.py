import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import
fetch_california_housing
# 1. Load the dataset
cal_housing = fetch_california_housing()
df = pd.DataFrame(cal_housing.data,
columns=cal_housing.feature_names)
df['MedHouseVal'] = cal_housing.target # Add
the target to our DataFrame
# Optional: Preview the first few rows
print(df.head())
print("\nSummary statistics:")
print(df.describe())
MachineLearningLab (BSCL606)
PageNo. 02
# 2. Create histograms for each numerical
feature
for col in df.columns:
plt.figure()
plt.hist(df[col]) # no color is specified
plt.title(f"Histogram of {col}")
plt.xlabel(col)
plt.ylabel("Frequency")
plt.show()
# 3. Create box plots for each numerical feature
for col in df.columns:
plt.figure()
plt.boxplot(df[col], vert=True) # no color or
style specified
plt.title(f"Box Plot of {col}")
plt.ylabel(col)
plt.show()