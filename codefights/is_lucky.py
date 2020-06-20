"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first
half of the digits is equal to the sum of the second half. Given a ticket number n, determine if it's lucky or not.
"""


def is_lucky(n):
    half_len = int(len(str(n))/2)
    return sum([int(c) for c in str(n)[half_len:]]) == sum([int(c) for c in str(n)[:half_len]])


num_list = [
    1230,  # true
    239017,  # false
    134008,  # true
]
print(*map(is_lucky, num_list), sep='\n')
