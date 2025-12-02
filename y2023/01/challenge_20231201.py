import re

def lines_split(input_string):
  lines = input_string.strip().split('\n')  
  return [line.strip() for line in lines]
  
def get_first_and_last_digits(input_string):
  digits = [char for char in input_string if char.isdigit()]
  if not digits:
      return 0
  return int(''.join([digits[0], digits[-1]]))

def get_digits(input_list):
  return [get_first_and_last_digits(line) for line in input_list]

def sum_digits(digits_list):
  return sum(digits_list)

def read_lines_from_file(file_path):
  with open(file_path, 'r') as f_in:
      return lines_split(f_in.read())
    
def solve_challenge1(file_path):
  lines = read_lines_from_file(file_path)
  digits = get_digits(lines)
  return sum_digits(digits)

def extract_all_digits(input_string):
  words_to_digits = {
      'one': '1', 'two': '2', 'three': '3', 'four': '4',
      'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
  }
  
  words = words_to_digits.keys()
  pattern = re.compile(r'(?=(' + '|'.join(words) + r'|\d))')
  matches = []
  for match in pattern.finditer(input_string):
    token = match.group(1)
    if token is None:
        continue
    if token.isdigit():
        matches.append(token)
    elif token in words_to_digits:
      matches.append(words_to_digits[token])
  if not matches:
      return 0
  return int(matches[0] + matches[-1])

def solve_challenge2(file_path):
  lines = read_lines_from_file(file_path)
  digits = [extract_all_digits(line) for line in lines]
  return sum_digits(digits)

if __name__ == "__main__":
  print(solve_challenge1('./input.txt'))
  print(solve_challenge2('./input.txt'))