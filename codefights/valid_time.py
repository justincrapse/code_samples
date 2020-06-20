"""
Check if the given string is a correct time representation of the 24-hour clock.
input: "25:51"
output: False
"""
import re


def valid_time(time):
    return bool(re.match(r'([0-1]\d|[2][0-3]):[0-5]\d', time))


input_list = [
    '13:58',  # true
    '25:51',  # false
    '02:76',  # false
]

print(*map(valid_time, input_list), sep='\n')
