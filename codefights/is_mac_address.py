"""
Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.
input: "02-03-04-05-06-07-"
output: False
"""
import re


def is_mac_48_address(string_in):
    return bool(re.match(r'^([\dA-F]{2}-){5}[\dA-F]{2}$', string_in))


input_list = [
    '00-1B-63-84-45-E6',  # true
    'Z1-1B-63-84-45-E6',  # false
    'not a MAC-48 address',  # false
    'FF-FF-FF-FF-FF-FF',  # true
]

print(*map(is_mac_48_address, input_list), sep='\n')
