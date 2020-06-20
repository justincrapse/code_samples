"""
A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.
Given a string, check whether it is beautiful.
input: "abcdefghijklmnopqrstuvwxyzqwertuiopasdfghjklxcvbnm"
output: True
"""


def is_beautiful_string(s):
    return all([s.count(chr(i)) >= s.count(chr(i + 1)) for i in range(ord('a'), ord('z'))])


input_list = [
    'bbbaacdafe',  # true
    'aabbb',  # false
    'abcdefghijklmnopqrstuvwxyzz',  # false
    'abcdefghijklmnopqrstuvwxyzqwertuiopasdfghjklxcvbnm',  # true
]

print(*map(is_beautiful_string, input_list), sep='\n')
