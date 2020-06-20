"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one.
Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
"""


def array_change(input_array):
    total_moves = 0
    for i in range(len(input_array) - 1):
        if input_array[i] >= input_array[i + 1]:
            moves = input_array[i] - input_array[i + 1] + 1
            input_array[i + 1] += moves
            total_moves += moves
        else:
            continue
    return total_moves


input_list = [
    [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15],  # 13
    [-1000, 0, -2, 0],  # 5
    [3122, -645, 2616, 13213, -8069],  # 25559
]

print(*map(array_change, input_list), sep='\n')
