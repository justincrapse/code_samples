"""
Given a string, replace each its character by the next one in the English alphabet (z would be replaced by a).
"""


def alphabetic_shift(s):
    return ''.join([chr(ord(i)+1) if ord(i) < 122 else 'a' for i in s])


input_list = [
    'azabaza',
    'korako',
    'YABZZBAY'  # not handled! Oh no
]

print(*map(alphabetic_shift, input_list), sep='\n')
