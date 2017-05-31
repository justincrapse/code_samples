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
"""
After becoming famous, CodeBots decided to move to a new building and live together. The building is represented by a 
rectangular matrix of rooms, each cell containing an integer - the price of the room. Some rooms are free (their cost is 0),
but that's probably because they are haunted, so all the bots are afraid of them. That is why any room that is free or is
located anywhere below a free room in the same column is not considered suitable for the bots.
Help the bots calculate the total price of all the rooms that are suitable for them.
input: 
matrix: [[1,1,1,0], 
         [0,5,0,1], 
         [2,1,3,10]]
output: 9
"""
def matrixElementsSum(matrix):
    total = 0
    for row in zip(*matrix):
        for element in row:
            if element == 0:
                break
            total += element
    return total
###################################################################################################
"""
Given an array of strings, return another array containing all of its longest strings.
input: ["aba", "aa", "ad", "vcd", "aba"]
output: ["aba", "vcd", "aba"]
"""
def allLongestStrings(inputArray):
    max_length = max([len(string) for string in inputArray])
    return[string for string in inputArray if len(string) == max_length]
###################################################################################################
"""
Given two strings, find the number of common characters between them. (multiple occurances are taken into account)
input: s1: "aabcc" s2: "adcaa"
output: 3
"""
def commonCharacterCount(s1, s2):
    common = set(s1) & set(s2)
    return sum([min(s1.count(ch), s2.count(ch)) for ch in common])
###################################################################################################
"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the 
first half of the digits is equal to the sum of the second half. Given a ticket number n, determine if it's lucky or not.
input: 239017
output: False
"""
def isLucky(n):
    half_len = int(len(str(n))/2)
    return sum([int(c) for c in str(n)[half_len:]]) == sum([int(c) for c in str(n)[:half_len]])
###################################################################################################
"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange 
the people by their heights in a non-descending order without moving the trees.
input: [-1, 150, 190, 170, -1, -1, 160, 180]
output: [-1, 150, 160, 170, -1, -1, 180, 190]
"""
def sortByHeight(a):
    height_list = sorted([i for i in a if i != -1])
    print(height_list)
    for i, value in enumerate(a):
        if value == -1:
            height_list.insert(i, -1)
    return height_list
###################################################################################################
"""
Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair. 
The results string should not contain any parentheses.
input: "a(bcdefghijkl(mno)p)q"
output: "apmnolkjihgfedcbq"
"""
import re
def reverseParentheses(s):
    if '(' in s:
        ss = re.split(r'(\([\w\s]+\))', s)
        for i, sub_s in enumerate(ss):
            if i % 2 == 1:
                ss[i] = sub_s[1:-1][::-1]
        return reverseParentheses(''.join(ss))
    else:
        return s
###################################################################################################
"""
Several people are standing in a row and need to be divided into two teams. The first person goes into team 1,
the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on. You are given
an array of positive integers - the weights of the people. Return an array of two integers, where the first element
is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.
input: [50, 60, 60, 45, 70]
output: [180, 105]
"""
def alternatingSums(a):
    return [sum(a[::2]), sum(a[1::2])]
###################################################################################################
"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
input:["abc", "ded"]
output: 
["*****",
 "*abc*",
 "*ded*",
 "*****"]
"""
def addBorder(picture):
    for i in range(len(picture)):
        picture[i] = '*' + picture[i] + '*'
    picture.insert(0, '*' * len(picture[0]))
    picture.append('*' * len(picture[0]))

    return picture
###################################################################################################
"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.
input: a: [832, 998, 148, 570, 533, 561, 894, 147, 455, 279] b: [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]
output: False
"""
def areSimilar(A, B):
    return sorted(A)==(sorted(B)) and sum([i!=x for i,x in zip(A,B)]) < 3
###################################################################################################
"""
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. 
Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
input: [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]
output: 13
"""
def arrayChange(inputArray):
    total_moves = 0
    for i in range(len(inputArray) - 1):
        if inputArray[i] >= inputArray[i+1]:
            moves = inputArray[i] - inputArray[i+1] + 1
            inputArray[i+1] += moves
            total_moves += moves
        else:
            continue
    return total_moves
###################################################################################################


###################################################################################################


###################################################################################################

###################################################################################################
