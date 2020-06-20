"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the
arrays.
"""
from itertools import starmap


def are_similar(a, b):
    return sorted(a) == (sorted(b)) and sum([i != x for i, x in zip(a, b)]) < 3


list_in = [
    [[1, 2, 3], [2, 1, 3]],  # true
    [[1, 2, 2], [2, 1, 1]],  # false
    [[832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]],  # true
    [[832, 998, 148, 570, 533, 561, 894, 147, 455, 279], [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]],  # false
]

print(*starmap(are_similar, list_in ), sep='\n')
