#%%
# Part 1
#%%
# imports
import re
# %%
# read input
with open('./input.txt','r') as f_in:
    data = f_in.read()
# %%
# find matches
pattern = r'mul\(\d{1,3},\d{1,3}\)'
matches = re.findall(pattern, data)
# %%
# find multipliers
digits_pattern = r'\d{1,3}'
multipliers = []
for text in matches:
    multipliers.append([match for match in re.findall(digits_pattern,text)])
# %%
# multiply
mul_results = []
for mults in multipliers:
    mul_results.append(int(mults[0])*int(mults[1]))
# %%
# sum
result = sum(mul_results)
result
# %%
# Part 2
# %%
new_pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
new_matches = re.findall(new_pattern, data)
new_matches
# %%
valid_matches_bool = []
for i in range(len(new_matches)):
  if i == 0:
    valid_matches_bool.append(True)
  elif new_matches[i] == "do()":
    valid_matches_bool.append(True)
  elif new_matches[i] == "don't()":
    valid_matches_bool.append(False)
  else:
    last_match = valid_matches_bool[-1]
    valid_matches_bool.append(last_match)
valid_matches_bool
# %%
valid_matches = [new_matches[i] for i in range(len(new_matches)) if valid_matches_bool[i]]
valid_matches
# %%
multipliers = []
for text in valid_matches:
    multipliers.append([match for match in re.findall(digits_pattern,text)])
multipliers
# %%
# multiply
mul_results = []
for mults in multipliers:
  if mults:
    mul_results.append(int(mults[0])*int(mults[1]))
# %%
# sum
result = sum(mul_results)
result