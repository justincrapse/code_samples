###################################################################################################
"""
Takes in a year and returns the centry of that year
input: 1988
output: 20
"""
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
###################################################################################################
"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
input: [9, 5, 10, 2, 24, -1, -48]
output: 50
"""
def adjacentElementsProduct(inputArray):
    return max([inputArray[i] * inputArray[i + 1] for i in range(len(inputArray) - 1)])
###################################################################################################
"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative 
integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue
will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help 
him figure out the minimum number of additional statues needed.
input: [6, 2, 3, 8]
output: 3
"""
def makeArrayConsecutive2(statues):
    statues.sort()
    return sum([statues[i + 1] - statues[i] -1 for i in range(len(statues) -1)])
###################################################################################################


###################################################################################################


###################################################################################################


###################################################################################################


###################################################################################################


###################################################################################################


###################################################################################################


###################################################################################################


###################################################################################################


###################################################################################################


###################################################################################################


###################################################################################################


###################################################################################################

###################################################################################################
