"""
Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair.
The results string should not contain any parentheses.
"""
import re


def reverse_parentheses(s):
    if '(' in s:
        ss = re.split(r'(\([\w\s]+\))', s)
        for i, sub_s in enumerate(ss):
            if i % 2 == 1:
                ss[i] = sub_s[1:-1][::-1]
        return reverse_parentheses(''.join(ss))
    else:
        return s


string_list = [
    'foo(bar)baz',  # foorabbaz
    'foo(bar)baz(blim)',  # foorabbazmilb
    'foo(bar(baz))blim',  # foobazrabblim
]

print(*map(reverse_parentheses, string_list), sep='\n')
