"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
"""


def adjacent_elements_product(list_in):
    return max([list_in[i] * list_in[i + 1] for i in range(len(list_in) - 1)])


array_list = [
    [3, 6, -2, -5, 7, 3],  # 21
    [-1, -2],  # 2
    [5, 1, 2, 3, 1, 4],  # 6
]
print(*map(adjacent_elements_product, array_list), sep='\n')
