""" given an array of size n, return the first duplicate """

import random
from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        t_result = f(*args, **kw)
        te = time()
        print(f'{f.__name__} {te-ts} seconds')
        return t_result
    return wrap


@timing
def return_first_dup_linear(num_array):
    max_num = max(num_array)
    found_list = [None] * max_num + [None]
    for i in num_array:
        if not found_list[i]:
            found_list[i] = True
        else:
            return i


@timing  # looks similar to simple list lookup. sometimes marginally faster, but probably fast because
def return_first_dup_dict(num_array):
    found_dict = dict()
    for i in num_array:
        if i in found_dict:
            return i
        found_dict[i] = True


@timing
def return_first_dup_log(num_array):
    num_array.sort()
    for i in range(0, len(num_array) - 1):
        if num_array[i] == num_array[i + 1]:
            return num_array[i]


@timing
def return_first_dup_quadratic(num_array):
    found = []
    for i in num_array:
        if i in found:
            return i
        found.append(i)


# list_len = 100000
list_len = 10000
nums = [i for i in range(0, random.randint(2, list_len))]
random.shuffle(nums)
rand_index = random.randint(1, len(nums) - 1)
rand_index_2 = random.choice(nums[:rand_index] + nums[rand_index + 1:])  # any index besides rand_index
if random.choice([True] * 6 + [False]):  # 1 in 7 chance of there not being a duplicate number.
    nums[rand_index] = nums[rand_index_2]

if __name__ == '__main__':
    print(return_first_dup_linear(num_array=nums))
    print(return_first_dup_dict(num_array=nums))
    print(return_first_dup_log(num_array=nums))
    print(return_first_dup_quadratic(num_array=nums))
