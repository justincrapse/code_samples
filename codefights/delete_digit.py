"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.
input: 152
output: 52
"""


def delete_digit(num_in):
    num_list = list(str(num_in))

    for i in range(len(num_list) - 1):
        if num_list[i] < num_list[i + 1]:
            del num_list[i]
            return int(''.join(num_list))
    del num_list[-1]
    return int(''.join(num_list))


input_list = [
    1001,  # 101
    222219,  # 22229
    44435,  # 4445
]

print(*map(delete_digit, input_list), sep='\n')
