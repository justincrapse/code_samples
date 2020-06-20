"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
input:
output: 7
"""


def array_maximal_adjacent_difference(a):
    return max([abs(a[i] - a[i + 1]) for i in range(len(a) - 1)])


input_list = [
    [-1, 4, 10, 3, -2],  # 7
    [1, 1, 1, 1],  # 0
    [10, 11, 13],  # 2
]

print(*map(array_maximal_adjacent_difference, input_list), sep='\n')
