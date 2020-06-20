"""
First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]. Next, each substring with length greater than one is
replaced with a concatenation of its length and the repeating character. For example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
input:"aabbbc"
output: "2a3bc"
"""
from itertools import groupby


def line_encoding(string_in):
    groups = [list(y) for x, y in groupby(string_in)]
    number_gram = []
    for g in groups:
        if len(g) > 1:
            number_gram.append(str(len(g)))
            number_gram.append(g[0])
        else:
            number_gram.append(g[0])
    return ''.join(number_gram)


input_list = [
    'aabbbc',  # 2a3bc
    'zzzz',  # 4z
    'wwwwwwwawwwwwww',  # 7wa7w
    'qwertyuioplkjhg',  # qwertyuioplkjhg
]

print(*map(line_encoding, input_list), sep='\n')
