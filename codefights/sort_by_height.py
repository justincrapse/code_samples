"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to
rearrange the people by their heights in a non-descending order without moving the trees.
"""


def sort_by_height(a):
    height_list = sorted([i for i in a if i != -1])
    for i, value in enumerate(a):
        if value == -1:
            height_list.insert(i, -1)
    return height_list


height_lists = [
    [-1, 150, 190, 170, -1, -1, 160, 180],  # [-1, 150, 160, 170, -1, -1, 180, 190]
    [2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1],  # [1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2]
    [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3],  # [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]
]

print(*map(sort_by_height, height_lists), sep='\n')
