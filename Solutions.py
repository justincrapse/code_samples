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
"""
Given a string, find out if its characters can be rearranged to form a palindrome.
input: "abbcabb"
output: True
"""
def palindromeRearranging(inputString):
    return sum([inputString.count(char)%2 for char in set(inputString)]) < 2
###################################################################################################
"""
Call two arms equally strong if the heaviest weights they each are able to lift are equal. Call two people equally
strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are
their weakest arms. Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
input: yourLeft: 10 yourRight: 20 friendsLeft: 10 friendsRight: 20
output: True
"""
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return sorted([yourLeft, yourRight]) == sorted([friendsLeft, friendsRight])
###################################################################################################
"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
input: [-1, 4, 10, 3, -2]
output: 7
"""
def arrayMaximalAdjacentDifference(a):
    return max([abs(a[i]-a[i+1]) for i in range(len(a) - 1)])
###################################################################################################
"""
Given a string, find out if it satisfies the IPv4 address naming rules.
*I have other examples of pure and mixed regex solutions as well for IPv4 and IPv6
input: "1.256.1.1"
output: False
"""
def isIPv4Address(inputString):
    sub_s = inputString.split('.')
    return len(sub_s) == 4 and all([n.isdigit() and int(n) in range(256) for n in sub_s])
###################################################################################################
"""
You are given an array of integers representing coordinates of obstacles situated on a straight line. Assume that
you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length
represented by some integer. Find the minimal length of the jump enough to avoid all the obstacles.
input: [1, 4, 10, 6, 2]
output: 7
"""
def avoidObstacles(inputArray):
    max_in = max(inputArray) + 2
    gaps = [i for i in range(max_in) if i not in inputArray and i not in [0, 1]]
    for gap in gaps:
        hop_multiples = [i for i in range(0, max_in, gap)]
        if len(set(inputArray).intersection(hop_multiples)) == 0:
            return gap
###################################################################################################
"""
Last night you had to study, but decided to party instead. Now there is a black and white photo of you that is about 
to go viral. You cannot let this ruin your reputation, so you want to apply box blur algorithm to the photo to hide 
its content. The algorithm works as follows: each pixel x in the resulting image has a value equal to the average value
of the input image pixels' values from the 3 × 3 square with the center at x. All pixels at the edges are cropped. As 
pixel's value is an integer, all fractions should be rounded down.
input:
image: [[36,0,18,9,9,45,27], 
        [27,0,54,9,0,63,90], 
        [81,63,72,45,18,27,0], 
        [0,0,9,81,27,18,45], 
        [45,45,27,27,90,81,72], 
        [45,18,9,0,9,18,45], 
        [27,81,36,63,63,72,81]]
output:
[[39,30,26,25,31], 
 [34,37,35,32,32], 
 [38,41,44,46,42], 
 [22,24,31,39,45], 
 [37,34,36,47,59]]
"""
def boxBlur(image):
    new_image = []

    m_list = [i[1:-1] for i in image[1:-1]]
    for i1, v1 in enumerate(m_list):
        new_row = []
        for i2, v2 in enumerate(v1):
            pixels = [i[i2:i2+3] for i in image[i1:i1+3]]
            new_row.append(int(sum([sum(i) for i in pixels])/9))
        new_image.append(new_row)
    return new_image
###################################################################################################
"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have
a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement
of mines we want to create a Minesweeper game setup.
input:
[[true,false,false,true], 
 [false,false,true,false], 
 [true,true,false,true]]
output:
[[0,2,2,1], 
 [3,4,3,3], 
 [1,2,3,1]]
 """
def minesweeper(matrix):
    m_list = matrix[:]
    matrix = [[False] + i + [False] for i in matrix]
    matrix.append([False for i in matrix[0]])
    matrix.insert(0, [False for i in matrix[0]])
    new_matrix = []
    for i1, v1 in enumerate(m_list):
        new_row = []
        for i2, v2 in enumerate(v1):
            pixels = [i[i2:i2 + 3] for i in matrix[i1:i1 + 3]]
            pixels[1][1] = False
            new_row.append(int(sum([sum(i) for i in pixels])))
        new_matrix.append(new_row)
    return new_matrix
###################################################################################################
"""
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.
input: [1, 2, 3, 4, 5]
output: [1, 2, 0, 4, 5]
"""
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if i == elemToReplace else i for i in inputArray]
###################################################################################################
"""
Check if all digits of the given integer are even.
input: 642386
output: False
"""
def evenDigitsOnly(n):
    return all([int(i)%2==0 for i in str(n)])
###################################################################################################
"""
Correct variable names consist only of Latin letters, digits and underscores and they can't start with a digit.
Check if the given string is a correct variable name.
input: "variable0"
output: True
"""
def variableName(name):
    return bool(re.match(r'^[^\d\W][\w]*$', name))
###################################################################################################
"""
Given a string, replace each its character by the next one in the English alphabet (z would be replaced by a).
input: "crazy"
output: "dsbaz"
"""
def alphabeticShift(inputString):
    return ''.join([chr(ord(i)+1) if ord(i) < 122 else 'a' for i in inputString])
###################################################################################################
"""
Given a sorted array of integers a, find such an integer x that the value of
abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
is the smallest possible (here abs denotes the absolute value).If there are several possible answers, output the smallest one.
input: [0, 7, 9]
output: 7
"""
def absoluteValuesSumMinimization(a):
    sums = [sum([abs(i - x) for i in a]) for x in a]
    lowest = min(sums)
    return a[sums.index(lowest)]
###################################################################################################
"""
Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that 
after the rearrangement the strings at consecutive positions would differ by exactly one character.
input: ["abc", "bef", "bcc", "bec", "bbc", "bdc"]
output: True
"""
from itertools import permutations

def stringsRearrangement(inputArray):
    combos = list(permutations(inputArray))
    for array in combos:
        matches = 0
        for i in range(len(array) -1):
            array_1 = list(array[i])
            array_2 = list(array[i + 1])
            mismatch = 0
            for x, y in zip(array_1, array_2):
                if x != y:
                    mismatch += 1
            if mismatch == 1:
                matches += 1
        if matches == len(inputArray) - 1:
            return True
    return False
###################################################################################################
"""
Each day a plant is growing by upSpeed meters. Each night that plant's height decreases by downSpeed meters due
to the lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We want
to know when the height of the plant will reach a certain level.
input: upSpeed: 100 downSpeed: 10 desiredHeight: 910
ouput: 10
"""
def growingPlant(upSpeed, downSpeed, desiredHeight):
    current_height = 0
    days = 0
    while current_height < desiredHeight:
        days += 1
        current_height +=  upSpeed
        if current_height >= desiredHeight:
            return days
        else:
            current_height -= downSpeed
###################################################################################################
"""
Let's define digit degree of some positive integer as the number of times we need to replace this number 
with the sum of its digits until we get to a one digit number. Given an integer, find its digit degree.
input: 99
output: 2
"""
def digitDegree(n):
    dig_str = str(n)
    digit_degree = 0
    while len(dig_str) > 1:
        dig_sum = sum([int(i) for i in dig_str])
        dig_str = str(dig_sum)
        digit_degree += 1
    return digit_degree
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

###################################################################################################

###################################################################################################

###################################################################################################

###################################################################################################

###################################################################################################

###################################################################################################

###################################################################################################


