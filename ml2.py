im# Step 1: Load the California Housing Dataset
cal_housing= fetch_california_housing()
df =
pd.DataFrame(cal_housing.data,columns=cal_housin
g.feature_names)
df['medHouseVal']=cal_housing.target
# Step 2: Compute the correlation matrix
corr_matrix = df.corr()
# Step 3: Visualize the correlation matrix using a
heatmap
print("correlation matrix:")
print(corr_matrix)
plt.figure(figsize=(8,6))
plt.imshow(corr_matrix, cmap='coolwarm'
,
interpolation='nearest'
, aspect='auto')
plt.colorbar(label='correlation coefficient')
MachineLearningLab (BSCL606)
PageNo. 07
# Corrected line: use corr_matrix.columns to get the
column names and their count
plt.xticks(range(len(corr_matrix.columns)),corr_matr
ix.columns)
plt.title("correlation matrix Heatmap")
plt.tight_layout()
plt.show()