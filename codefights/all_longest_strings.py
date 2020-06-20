"""
Given an array of strings, return another array containing all of its longest strings.
"""


def all_longest_strings(string_list):
    max_length = max([len(string) for string in string_list])
    return [string for string in string_list if len(string) == max_length]


string_lists = [
    ["aba", "aa", "ad", "vcd", "aba"],  # ["aba", "vcd", "aba"]
    ["abc", "eeee", "abcd", "dcd"],  # ["eeee", "abcd"]
    ["onsfnib", "aokbcwthc", "jrfcw"],  # ["aokbcwthc"]
]
print(*map(all_longest_strings, string_lists), sep='\n')
