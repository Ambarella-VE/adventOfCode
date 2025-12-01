import unittest
from parameterized import parameterized
from unittest import TestCase
from challenge_20231201 import lines_split,get_first_and_last_digits,sum_digits,get_digits,read_lines_from_file,solve_challenge1,solve_challenge2,extract_all_digits

class TestChallenge20231201(TestCase):
  
  def test_lines_split(self):
    sample_input = """2q11jdqcbeight
    eight47srvbfive
    s1coneightfoureeight557m38
    xvqeightwosixnine61eightsn2tdczfhx
    msixonexch1twokjbd1hchqk1
    112ninejlhhjmjzkzgdsix
    6six7jr
    878eightgvsqvzfthree
    2jxzhlkhdktxfjjleightdfpgfxjv
    """ 
    
    expected_output = [
      "2q11jdqcbeight",
      "eight47srvbfive",
      "slconeightfoureeight557m38",
      "xvqeightwosixnine61eightsn2tdczfhx",
      "msixonexch1twokjbd1hchqk1",
      "112ninejlhhjmjzkzgdsix",
      "6six7jr",
      "878eightgvsqvzfthree",
      "2jxzhlkhdktxfjjleightdfpgfxjv"
    ]
    
    actual_output = lines_split(sample_input)
    self.assertEqual(actual_output, expected_output)
    self.assertIsInstance(actual_output, list)
    
  @parameterized.expand([
    ("slconeightfoureeight557m38", 58),
    ("xvqeightwosixnine61eightsn2tdczfhx", 62),
    ("msixonexch1twokjbd1hchqk1", 11),
    ("112ninejlhhjmjzkzgdsix", 12),
    ("6six7jr", 67)
  ])
  def test_get_first_and_last_digits(self, sample_input, expected_output):
    actual_output = get_first_and_last_digits(sample_input)
    self.assertEqual(actual_output, expected_output)  
    self.assertIsInstance(actual_output, int)