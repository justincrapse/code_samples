"""
After becoming famous, CodeBots decided to move to a new building and live together. The building is represented by a
rectangular matrix of rooms, each cell containing an integer - the price of the room. Some rooms are free
(their cost is 0), but that's probably because they are haunted, so all the bots are afraid of them. That is why any
room that is free or is located anywhere below a free room in the same column is not considered suitable for the bots.
Help the bots calculate the total price of all the rooms that are suitable for them.
"""


def matrix_elements_sum(matrix):
    total = 0
    for row in zip(*matrix):
        for element in row:
            if element == 0:
                break
            total += element
    return total


matrix_list = [
    [
        [1, 1, 1, 0],
        [0, 5, 0, 1],
        [2, 1, 3, 10]
    ],  # 9
    [
        [1, 2, 3, 4, 5]
    ],  # 15
    [
        [4, 0, 1],
        [10, 7, 0],
        [0, 0, 0],
        [9, 1, 2]
    ]  # 15
]

print(*map(matrix_elements_sum, matrix_list), sep='\n')
