"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
"""


def add_border(picture):
    for i in range(len(picture)):
        picture[i] = '*' + picture[i] + '*'
    picture.insert(0, '*' * len(picture[0]))
    picture.append('*' * len(picture[0]))
    return picture


list_in = [
    ["abc",
     "ded"],
    ["a"],
    ["aa",
     "**",
     "zz"],
    ["abcde",
     "fghij",
     "klmno",
     "pqrst",
     "uvwxy"]
]

for super_list in map(add_border, list_in):
    print('\n')
    for sub_list in super_list:
        print(sub_list)
