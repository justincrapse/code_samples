"""
Given a string, find out if its characters can be rearranged to form a palindrome.
"""


def palindrome_rearranging(str_in):
    return sum([str_in.count(char) % 2 for char in set(str_in)]) < 2


input_list = [
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc',  # false
    'zyyzzzzz',  # true
    'abcad',  # false
    'zaa',  # true
]

print(*map(palindrome_rearranging, input_list), sep='\n')
