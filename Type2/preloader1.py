import cudf
import pandas as pd
from joblib import Parallel, delayed

# Read the CSV files using cudf
df_candidates = cudf.read_csv("Type2/candidates.csv")
df_inputs = cudf.read_csv("Type2/Inputs.csv")

# Extract relevant columns into cuDF Series for faster access
uid_inputs = df_inputs.iloc[:, 0]
data_inputs = df_inputs.iloc[:, 1:]

# Initialize an empty list to store results
results = []

# Define a function to process each pair of inputs
def process_pair(i, j):
    uid_new = uid_inputs[i] + " " + uid_inputs[i+j]
    # Check if uid_new is present in df_candidates
    label = 1 if uid_new in df_candidates.values else 0
    return [uid_new, *data_inputs.iloc[i], *data_inputs.iloc[i+j], label]

# Parallelize the loop using joblib
num_inputs = len(df_inputs)
for i in range(num_inputs):
    results.extend(Parallel(n_jobs=4)(delayed(process_pair)(i, j) for j in range(1, num_inputs-i)))

# Create DataFrame from results
df = pd.DataFrame(results, columns=['uid', 'vbm_vac1', 'cbm_vac1', 'vbm_vac2', 'cbm_vac2', 'label_type_2'])

# Print and save the DataFrame
print(df)
df.to_csv('Type2/Dataset.csv')