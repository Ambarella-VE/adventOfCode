# %%
# Part 1

# %%
# imports
import pandas as pd
# %%
# Read input
df = pd.read_csv('./input.txt', header= None, delimiter='-')
df
# %%
# Transponse
dfT = df.T
dfT
# %%
# Sort
dfT_sorted = dfT.apply(sorted,axis=0)
dfT_sorted
# %%
# Transpose back
sorted_df = dfT_sorted.T
sorted_df
# %%
# Remove duplicates
df_unique = sorted_df.drop_duplicates()
df_unique
# %%
