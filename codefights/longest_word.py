"""
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.
"""
import re


def longest_word(text):
    return max(re.findall(r'[\w]+', text), key=len)


input_list = [
    'Ready[[[, steady, go!',
    'You are the best!!!!!!!!!!!! CodeFighter ever!',
    'To be or not to be'
]

print(*map(longest_word, input_list), sep='\n')
