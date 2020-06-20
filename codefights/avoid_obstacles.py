"""
You are given an array of integers representing coordinates of obstacles situated on a straight line. Assume that
you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length
represented by some integer. Find the minimal length of the jump enough to avoid all the obstacles.
"""


def avoid_obstacles(list_in):
    max_in = max(list_in) + 2
    gaps = [i for i in range(max_in) if i not in list_in and i not in [0, 1]]
    for gap in gaps:
        hop_multiples = [i for i in range(0, max_in, gap)]
        if len(set(list_in).intersection(hop_multiples)) == 0:
            return gap


input_list = [
    [1, 4, 10, 6, 2],  # 7
    [5, 3, 6, 7, 9],  # 4
    [1000, 999],  # 6
]

print(*map(avoid_obstacles, input_list), sep='\n')
