import pandas as pd
# Load the dataset
file_path =
"/Users/Desktop/training_dataset_CGPA.csv"
df = pd.read_csv(file_path)
# Function to implement Find-S Algorithm
def find_s(data):
# Extract features and target column
attributes = data.iloc[:, :-1].values # All columns
except last (features)
target = data.iloc[:, -1].values # Last column
(target)
# Initialize the hypothesis with the first positive
example
hypothesis = None
for i, val in enumerate(target):
if val.lower() == "yes": # Consider only positive
MachineLearningLab (BSCL606)
MachineLearningLab (BSCL606)
PageNo. 13
hypothesis = attributes[i].copy()
print(f"Initial Hypothesis (from first positive
example): {hypothesis}\n")
break
if hypothesis is None:
raise ValueError("No positive examples found in
the dataset!")
# Iterate through all examples and update hypothesis
for i, val in enumerate(target):
if val.lower() == "yes": # Consider only positive
examples
for j in range(len(hypothesis)):
if hypothesis[j] != attributes[i][j]:
hypothesis[j] = "?" # Generalize hypothesis
print(f"Hypothesis after example {i+1}:
{hypothesis}\n")
return hypothesis
# Apply Find-S algorithm and display steps
final_hypothesis = find_s(df)
# Print final hypothesis
print("Final Hypothesis:"
, final_hypothesis)