import math

def centuryFromYear(year):
    if year <= 100 :
        return 1
    elif year > 100:
        integer = (int(math.floor(year / 100)))
        if year % 100 == 0:
            return integer
        else:
            return integer + 1
