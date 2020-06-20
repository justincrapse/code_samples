import math

"""
Takes in a year and returns the century of that year
"""


def century_from_year(year):
    if year <= 100:
        return 1
    elif year > 100:
        integer = (int(math.floor(year / 100)))
        if year % 100 == 0:
            return integer
        else:
            return integer + 1


year_list = [
    1988,  # 20
    1700,  # 17
    200,  # 2
]
print(*map(century_from_year, year_list), sep='\n')
