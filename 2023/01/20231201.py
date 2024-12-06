# %%
# Part 1

# %%
# Import
import re
# %%
# Read Input
with open('./input.txt', 'r') as f_in:
  data = f_in.read().splitlines()
# %%
# Def functions
def extract_digits(row):
  return ''.join(d for d in row if d.isdigit())
# %%
# Calculate
new_digits = [extract_digits(row) for row in data]
two_digits = [int(str(num[0])+str(num[-1])) for num in new_digits]
# %%
# Result
digits_sum = sum(two_digits)
digits_sum

# %%
# Part 2

# %%
# New digits
digits = [str(d) for d in range(10)] 
named_digits = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
all_digits = digits + named_digits  # Combine both types of digits

# %%
# Updated find_matches function
def find_matches(input_string, elements):
    """
    Finds and returns a list of matches in the input string based on the elements provided.
    
    Args:
        input_string (str): The string to search for matches.
        elements (list): A list of strings to search for in the input string.
        
    Returns:
        list: A list of matches in the order they appear in the input string.
    """
    # Escape elements for regex safety and join with '|'
    pattern = '|'.join(map(re.escape, elements))
    matches = re.findall(pattern, input_string)
    return matches

# %% 
# Tokenize
tokens = [find_matches(row, all_digits) for row in data]
tokens
# %% 
# New 2 digits
def new_2_digits(row):
    if len(row) >= 2:
        return [row[0], row[-1]]
    return row  # Return as-is if the row has less than 2 elements

new_two_digits = [new_2_digits(row) for row in tokens]
new_two_digits

# %% 
# Mapping
digit_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

# %% 
# Map
def map_digits(row):
    return [digit_mapping.get(d, d) for d in row]

mapped_digits = [map_digits(row) for row in new_two_digits]

# %% 
# Result
values = [int(''.join(row)) for row in mapped_digits if len(row) == 2]
result = sum(values)
result
