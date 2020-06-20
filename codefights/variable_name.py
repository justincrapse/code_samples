"""
Correct variable names consist only of Latin letters, digits and underscores and they can't start with a digit.
Check if the given string is a correct variable name.
"""
import re


def variable_name(name):
    return bool(re.match(r'^[^\d\W][\w]*$', name))


input_list = [
    '4gum',  # false
    'killer_miller',  # true
    'train34',  # true
    'fruit_*&^',  # false
]

print(*map(variable_name, input_list), sep='\n')
