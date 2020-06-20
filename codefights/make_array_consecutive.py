"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative
integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each
statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish
that. Help him figure out the minimum number of additional statues needed.

"""


def make_array_consecutive(statues):
    statues.sort()
    return sum([statues[i + 1] - statues[i] - 1 for i in range(len(statues) - 1)])


statue_list = [
    [6, 2, 3, 8],  # 3
    [0, 3],  # 2
    [5, 4, 6]  # 0
]
print(*list(map(make_array_consecutive, statue_list)), '\n', sep='\n')


# this one is more clear and concise:
def make_array_consecutive_2(statues):
    return max(statues) - min(statues) - (len(statues) - 1)


print(*map(make_array_consecutive_2, statue_list), sep='\n')
