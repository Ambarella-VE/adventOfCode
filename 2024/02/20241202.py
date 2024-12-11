#%%
# Part 1
#%%
# Imports
import pandas as pd

# %%
# Read data
with open('./input.txt', 'r') as f_in:
  data = f_in.read().splitlines()
for i in range(0, len(data)):
  data[i] = data[i].split(" ")
df = pd.DataFrame(data)
df.insert(0, "length",0)
for i,val in enumerate(data):
  df.loc[i,'length'] = len(val)
df
# %%
# Define functions
def order_valuation(row):
  ascending = []
  for i in range(row['length']-1):
    if not pd.isna(row[i]) and not pd.isna(row[i+1]):
      ascending.append(int(row[i]) < int(row[i+1]))
  return ascending
def distance_valuation(row):
  distances = []  
  for i in range(row['length']-1):
    if not pd.isna(row[i]) and not pd.isna(row[i+1]):
      distances.append(abs(int(row[i]) - int(row[i+1])))
  return distances
def is_descending(row):
  return not any(row['check_ascending'])
def is_ascending (row):
  return all(row['check_ascending'])
def distances_validity(row):
  validity = []
  for i in range(len(row['distances'])):
    validity.append(row['distances'][i] > 0 and row['distances'][i] <= 3)
  return all(validity)
# %%
# Create validation values
df ['check_ascending'] = df.apply(order_valuation,axis=1)
df['is_descending'] = df.apply(is_descending,axis=1)
df['is_ascending'] = df.apply(is_ascending,axis=1)
df['distances'] = df.apply(distance_valuation,axis=1)
df['valid_distances'] = df.apply(distances_validity,axis=1)
df['is_valid_report'] = df.apply(lambda row:(row['is_ascending']|row['is_descending']) and row['valid_distances'] ,axis=1)
df
# %%
# Calculate valid reports
valid_reports = len(df['is_valid_report'][df['is_valid_report']])
valid_reports
# %%
# Part 2
# %%
# Calculate new values
df['count_true'] = df.apply(lambda row: sum(row['check_ascending']),axis=1)
df['order_possible'] = False #TODO
df
# %%
