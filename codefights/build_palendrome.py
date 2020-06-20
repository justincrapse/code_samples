"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of
initial string to make it a palindrome.
"""


def build_palindrome(string_in):
    pal_gen = (i for i in string_in)
    length = len(string_in)
    while string_in != ''.join(reversed(string_in)):
        string_in = list(string_in)
        string_in.insert(length, next(pal_gen))
        string_in = ''.join(string_in)
    return string_in


input_list = [
    'abcdc',
    'aaaaba',
    'kebab',
    'cbdbedffcg'
]

print(*map(build_palindrome, input_list), sep='\n')
