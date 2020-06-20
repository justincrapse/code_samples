"""
Call two arms equally strong if the heaviest weights they each are able to lift are equal. Call two people equally
strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are
their weakest arms. Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
"""
from itertools import starmap


def are_equally_strong(your_left, your_right, friends_left, friends_right):
    return sorted([your_left, your_right]) == sorted([friends_left, friends_right])


input_dict_list = [
    {'your_left': 10, 'your_right': 15, 'friends_left': 15, 'friends_right': 10},  # true
    {'your_left': 15, 'your_right': 10, 'friends_left': 15, 'friends_right': 9}  # false  
]


for dict_input in input_dict_list:
    print(are_equally_strong(**dict_input))
