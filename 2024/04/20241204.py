#%%
# Part 1
# %%
# Read input
with open('./input.txt', 'r') as f_in:
  data = f_in.read().splitlines()
# %%
 # Convert each string in the list to a list of characters
new_list = []
for string in data:
  new_list.append(list(string))
data = new_list
# %%
# count rows
count_rows = 0

for i in range(len(data)):
  for j in range(len(data[i])-3):
    if data[i][j] == 'X' and data[i][j+1] == 'M' and data[i][j+2] == 'A' and data[i][j+3] == 'S':
      count_rows += 1
    if data[i][j] == 'S' and data[i][j+1] == 'A' and data[i][j+2] == 'M' and data[i][j+3] == 'X':
      count_rows += 1
count_rows
# %%
# count cols
count_cols = 0

for i in range(len(data)-3):
  for j in range(len(data[i])):
    if data[i][j] == 'X' and data[i+1][j] == 'M' and data[i+2][j] == 'A' and data[i+3][j] == 'S':
      count_cols += 1
    if data[i][j] == 'S' and data[i+1][j] == 'A' and data[i+2][j] == 'M' and data[i+3][j] == 'X':
      count_cols += 1
count_cols
# %%
# count diagonals down
count_diagonals_down = 0

for i in range(len(data)-3):
  for j in range(len(data[i])-3):
    if data[i][j] == 'X' and data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S':
      count_diagonals_down += 1
    if data[i][j] == 'S' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'M' and data[i+3][j+3] == 'X':
      count_diagonals_down += 1
count_diagonals_down
# %%
# count diagonals up
count_diagonals_up= 0

for i in range(3, len(data)):
  for j in range(len(data[i])-3):
    if data[i][j] == 'X' and data[i-1][j+1] == 'M' and data[i-2][j+2] == 'A' and data[i-3][j+3] == 'S':
      count_diagonals_up += 1
    if data[i][j] == 'S' and data[i-1][j+1] == 'A' and data[i-2][j+2] == 'M' and data[i-3][j+3] == 'X':
      count_diagonals_up += 1
count_diagonals_up
# %%
# result
result = count_rows+ count_cols+ count_diagonals_down+ count_diagonals_up
result
# %%
# Part 2
# %%
# count X-MAS
count_x_mas = 0
for i in range(len(data)-2):
  for j in range(len(data)-2):
    if data[i][j] == 'M' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'S'  and data[i+2][j]== 'M' and data[i][j+2] == 'S':
      count_x_mas += 1
    if data[i][j] == 'M' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'S'  and data[i+2][j]== 'S' and data[i][j+2] == 'M':
      count_x_mas += 1
    if data[i][j] == 'S' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'M'  and data[i+2][j]== 'M' and data[i][j+2] == 'S':
      count_x_mas += 1
    if data[i][j] == 'S' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'M'  and data[i+2][j]== 'S' and data[i][j+2] == 'M':
      count_x_mas += 1
count_x_mas