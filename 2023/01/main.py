#%%
with open("./input.txt", 'r',encoding='utf8') as f_in:
  lines = f_in.read().splitlines()
# %%
lines
# %%
def extract_digits(line):
  return ''.join(d for d in line if d.isdigit())
# %%
digits = [extract_digits(line) for line in lines]
# %%
digits
# %%
two_digits = [int(str(num[0])+str(num[-1])) for num in digits]
# %%
two_digits
# %%
sum(two_digits)
# %%
