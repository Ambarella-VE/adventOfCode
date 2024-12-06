#%%
# Part 1
#%%
# Imports
import pandas as pd

# %%
# Read Input
data = pd.read_csv('./input.txt', delimiter = " ",header=None)
data
#%%
# Drop NaNs and reset index
data = data.dropna(axis=1,how='all')
data.columns = [col for col in range(data.columns.shape[0])]
data
# %%
# Sort in df
df = pd.DataFrame()
for i in data.columns:
  df[i] = data[i].sort_values().reset_index(drop=True)
df
# %%
# Measure distance between columns
df['distance'] = abs(df[0] - df[1])
df

# %%
# Sum distance

total_distance = df['distance'].sum()
total_distance
# %%
# Part 2
# %%
# Calculate similarity between columns
df['times'] = 0
for index,row in df.iterrows():
  df['times'][index] = (df[1]==row[0]).sum()
df
# %%
# Calculate similarity
df['similarity'] = df[0]*df['times']
similarity = df['similarity'].sum()
similarity