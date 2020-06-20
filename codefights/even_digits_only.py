"""
Check if all digits of the given integer are even.
"""


def even_digits_only(n):
    return all([int(i) % 2 == 0 for i in str(n)])


input_list = [
    '22342352',  # false
    '2468686660',  # true
    '20202020120020024040',  # false
    '2222222222222222222222222'  # true
]
print(*map(even_digits_only, input_list), sep='\n')
