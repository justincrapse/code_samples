"""
Given two strings, find the number of common characters between them. (multiple occurrences are taken into account)
"""
from itertools import starmap


def common_character_count(s1, s2):
    common = set(s1) & set(s2)
    return sum([min(s1.count(ch), s2.count(ch)) for ch in common])


s1_s2_list = [
    ['a', 'aaa'],  # 1
    ['a', 'b'],  # 0
    ['aabcc', 'adcaa']  # 2
]
print(*starmap(common_character_count, s1_s2_list), '\n', sep='\n')


# again, but one iteration through:
def common_character_count_2(s1, s2: str):
    s2_list = list(s2)
    common_count = 0
    for i in s1:
        try:
            s2_list.remove(i)
            common_count += 1
        except ValueError:
            pass
    return common_count


print(*starmap(common_character_count_2, s1_s2_list), sep='\n')
