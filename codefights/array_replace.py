"""
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.
input: [1, 2, 3, 4, 5], elem_to_replace = 3, substitution_elem = 0
output: [1, 2, 0, 4, 5]
"""


def array_replace(input_array, elem_to_replace, substitution_elem):
    return [substitution_elem if i == elem_to_replace else i for i in input_array]


print(array_replace([1, 2, 3, 4, 5], 3, 0))
