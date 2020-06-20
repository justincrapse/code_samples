"""
Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that
after the rearrangement the strings at consecutive positions would differ by exactly one character.
input: ["abc", "bef", "bcc", "bec", "bbc", "bdc"]
output: True
"""
from itertools import permutations


def strings_rearrangement(list_in):
    combos = list(permutations(list_in))
    for array in combos:
        matches = 0
        for i in range(len(array) - 1):
            array_1 = list(array[i])
            array_2 = list(array[i + 1])
            mismatch = 0
            for x, y in zip(array_1, array_2):
                if x != y:
                    mismatch += 1
            if mismatch == 1:
                matches += 1
        if matches == len(list_in) - 1:
            return True
    return False


input_list = [
    ["zzzzab",
     "zzzzbb",
     "zzzzaa"],  # true
    ["ab",
     "ad",
     "ef",
     "eg"],  # false
    ["abc",
     "bef",
     "bcc",
     "bec",
     "bbc",
     "bdc"],  # true
]

print(*map(strings_rearrangement, input_list), sep='\n')
