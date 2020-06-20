"""
Given a string, find out if it satisfies the IPv4 address naming rules.
*I have other examples of pure and mixed regex solutions as well for IPv4 and IPv6
"""


def is_ipv4_address(s):
    sub_s = s.split('.')
    return len(sub_s) == 4 and all([n.isdigit() and int(n) in range(256) for n in sub_s])


input_list = [
    '1.256.1.1',  # false
    '172.16.254.1',  # true
    '172.316.254.1',  # false
]

print(*map(is_ipv4_address, input_list), sep='\n')
