###################################################################################################
# Codefights Arcade
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
"""
A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.
Given a string, check whether it is beautiful.
input: "abcdefghijklmnopqrstuvwxyzqwertuiopasdfghjklxcvbnm"
output: True
"""
def isBeautifulString(s):
    return all([s.count(chr(i))>=s.count(chr(i+1)) for i in range(ord('a'), ord('z'))])
###################################################################################################
"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of
initial string to make it a palindrome.
input: "abcdc"
output: "abcdcba"
"""
def buildPalindrome(s):
    pal_gen = (i for i in s)
    length = len(s)
    while s != ''.join(reversed(s)):
        s = list(s)
        s.insert(length, next(pal_gen))
        s = ''.join(s)
    return s
###################################################################################################
"""
Given an array of the numbers of votes given to each of the candidates so far, and an integer k equal to the
number of voters who haven't cast their vote yet, find the number of candidates who still have a chance to win
the election. The winner of the election must secure strictly more votes than any other candidate. If two or more
candidates receive the same (maximum) number of votes, assume there is no winner at all.
input: votes: [2, 3, 5, 2] k: 3
output: 2
"""
def electionsWinners(votes, k):
    m = max(votes)
    if k == 0 and votes.count(m) == 1:
        return 1
    return len([i for i in votes if i + k > m])
###################################################################################################
"""
Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.
input: "02-03-04-05-06-07-"
output: False
"""
def isMAC48Address(inputString):
    return bool(re.match(r'^([\dA-F]{2}-){5}[\dA-F]{2}$', inputString))
###################################################################################################
"""
First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]. Next, each substring with length greater than one is
replaced with a concatenation of its length and the repeating character. For example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
input:"aabbbc"
output: "2a3bc"
"""
from itertools import groupby

def lineEncoding(s):
    groups =  [list(y) for x, y in groupby(s)]
    number_gram = []
    for g in groups:
        if len(g) > 1:
            number_gram.append(str(len(g)))
            number_gram.append(g[0])
        else:
            number_gram.append(g[0])
    return ''.join(number_gram)
###################################################################################################
"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.
input: 152
output: 52
"""
def deleteDigit(n):
    n_list = list(str(n))

    for i in range(len(n_list) -1):
        if n_list[i] < n_list[i+1]:
            del n_list[i]
            return int(''.join(n_list))
    del n_list[-1]
    return int(''.join(n_list))
###################################################################################################
"""
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.
input: "Ready[[[, steady, go!"
output: "steady"
"""
def longestWord(text):
    return max(re.findall(r'[\w]+', text), key=len)
###################################################################################################
"""
Check if the given string is a correct time representation of the 24-hour clock.
input: "25:51"
output: False
"""
def validTime(time):
    return bool(re.match(r'[0-1]\d:[0-5]\d|[2][0-3]:[0-5]\d', time))
###################################################################################################
"""
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.
input:
[[2,5,3,4,3,1,3,2], 
 [4,5,4,1,2,4,1,3], 
 [1,1,2,1,4,1,1,5], 
 [1,3,4,2,3,4,2,4], 
 [1,5,5,2,1,3,1,1], 
 [1,2,3,3,5,1,2,4], 
 [3,1,4,4,4,1,5,5], 
 [5,1,3,3,1,5,3,5], 
 [5,4,4,3,5,4,4,4]]
output: 54
"""
def differentSquares(matrix):
    sub_set = []
    for i in range(len(matrix)-1):
        for i2 in range(len(matrix[i])-1):
            next_set = [matrix[i][i2:i2+2], matrix[i+1][i2:i2+2]]
            if next_set not in sub_set: sub_set.append(next_set)
    return len(sub_set)
###################################################################################################
"""
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names,
the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer
such that the obtained name is not used yet. Return an array of names that will be given to the files.
input: ["dd", "dd(1)", "dd(2)", "dd", "dd(1)", "dd(1)(2)", "dd(1)(1)", "dd", "dd(1)"]
output: ["dd", "dd(1)", "dd(2)", "dd(3)", "dd(1)(1)", "dd(1)(2)", "dd(1)(1)(1)", "dd(4)", "dd(1)(3)"]
"""
def fileNaming(names):

    for i, name in enumerate(names):
        new_index = 1
        new_name = '{}({})'.format(name, new_index)
        if name not in names[:i]:
            continue
        else:
            while new_name in names[:i]:
                new_index += 1
                new_name = '{}({})'.format(name, new_index)
            names[i] = new_name
    return names
###################################################################################################
"""
You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue,
you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. After
some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding
extended ASCII code. Assuming that your hunch is correct, decode the message.
input: "010010000110010101101100011011000110111100100001"
output: "Hello!"
"""
def messageFromBinaryCode(code):
    n = int(code, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
###################################################################################################
"""
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting 
from top-left and in clockwise direction.
input: 5
output:
[[1,2,3,4,5], 
 [16,17,18,19,6], 
 [15,24,25,20,7], 
 [14,23,22,21,8], 
 [13,12,11,10,9]]
* this one was pretty difficult for me and I bet I could come up with a more elegant solution
"""
def spiralNumbers(n):
    steps = 1
    round = 0
    matrix = [[0 for e in range(n)] for i in range(n)]

    while steps <= n * n:
        print(steps)
        first_range = n - round if round == 0 else (n - round * 2)

        for i in range(first_range):
            matrix[round][round + i] = steps
            steps += 1

        for i in range(round + 1, n - round):
            matrix[i][(n - round) - 1] = steps
            steps += 1

        for i in reversed(range((first_range) - 1)):
            matrix[(n - round) - 1][round + i] = steps
            steps += 1
        for i in reversed(range(round + 1, (n - round) - 1)):
            matrix[i][round] = steps
            steps += 1

        round += 1
    return matrix
###################################################################################################
"""
Sudoku checker
input: 
[[1,2,3,4,5,6,7,8,9], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4], 
 [1,2,3,4,5,6,7,8,9], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4], 
 [1,2,3,4,5,6,7,8,9], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4]]
output: False
"""
def sudoku(grid):
    check_list = [i for i in range(1, 10)]

    if sum([sorted(list) == check_list for list in grid]) != 9:
        return False
    
    if sum(([sorted(list) == check_list for list in list(zip(*grid))])) != 9:
        return False

    for section in range(0, 9, 3):
        for square in range(0, 9, 3):
            sub_grid = [[grid[section + e][square + i] for i in range(3)] for e in range(3)]
            if sorted([i for row in sub_grid for i in row]) != check_list:
                return False
    return True
###################################################################################################
# INTERVIEW PRACTICE SECTION
###################################################################################################
"""
Note: Write a solution with O(n2) time complexity, since this is what you would be asked to do during a real 
interview. You have an array a composed of exactly n elements. Given a number x, determine whether or not a 
contains three elements for which the sum is exactly x.
input: x: 986 
a: [557, 217, 627, 358, 527, 358, 338, 272, 870, 362, 897, 23, 618, 113, 718, 697, 586, 42, 424, 130, 230, 566, 560, 933]
output:True
"""
import itertools

def tripletSum(x, a):
    below_x = [i for i in a if i < x]
    for pair in itertools.combinations(below_x, 3):
        if sum(pair) == x:
            return True
    return False
###################################################################################################
"""
Given an array of words and a length l, format the text such that each line has exactly l characters and is
fully justified on both the left and the right. Words should be packed in a greedy approach; that is, pack 
as many words as possible in each line. Add extra spaces when necessary so that each line has exactly l characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not 
divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. 
For the last line of text and lines with one word only, the words should be left justified with no extra space 
inserted between them.
input: ["This", "is", "an", "example", "of", "text", "justification."]
ouput:
["This    is    an",
 "example  of text",
 "justification.  "]
 """
import textwrap
def textJustification(words, L):
    words = [word if len(word) > 0 else '~' for word in words]
    lines = textwrap.wrap(' '.join(words), L)
    lines[-1] = lines[-1].ljust(L, ' ')
    for l in range(len(lines)):
        if '~' in lines[l]:
            lines[l] = '{}'.format(' ' * L)
            continue
        line_length = len(lines[l])
        gaps = [gap.regs[0][0] for gap in re.finditer('\s', lines[l])]
        if not gaps:
            lines[l] = lines[l].ljust(L, ' ')
        else:
            while line_length < L:
                for i in range(len(gaps)):
                    if line_length == L:
                        break
                    gap_index = gaps[i]
                    line_list = [k for k in lines[l]]
                    line_list.insert(gap_index, ' ')
                    lines[l] = ''.join(line_list)
                    line_length += 1
                    for k in range(i, len(gaps)):
                        gaps[k] += 1
    return lines
###################################################################################################
"""
Valid Sudoku Puzzle (Unsolved: '.' equals empty spaces)
input:
[['.', '.', '.', '.', '2', '.', '.', '9', '.'],
 ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
 ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
 ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
 ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
 ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
 ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
 ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
output: False
"""
def sudoku2(grid):
    for row in grid:
        values = [i for i in row if i != '.']
        if len(values) != len(set(values)):
            return False

    columns = [i for i in zip(*grid)]
    for column in columns:
        values = [i for i in column if i != '.']
        if len(values) != len(set(values)):
            return False

    for row in range(0,9,3):
        for col in range(0,9,3):
            square = grid[row][col:col + 3] + grid[row + 1][col:col + 3] + grid[row + 2][col:col + 3]
            values = [i for i in square if i != '.']
            if len(values) != len(set(values)):
                print('lsfkj')
                return False
    return True
###################################################################################################
"""
The string s contains dashes that split it into groups of characters. You are given an integer k that represents
the number of characters in groups that your output should have. Your goal is to return a new string that breaks
s into groups with a length of k by placing dashes at the correct intervals. If necessary, the first group of 
characters can be shorter than k. It is guaranteed that there are no consecutive dashes in s.
input: "?CC?-[yiq2bg-Ie9?z!e-2X1i*k4-8ZMjllM-VEX2v%*"
output: "?CC?-[yiq2bg-Ie9?z!e-2X1i*k4-8ZMjllM-VEX2v%*"
"""
def stringReformatting(s, k):
    rstr = list(re.sub('-', '', s)[::-1])
    shift = 0
    for i in range(k, len(rstr), k):
        rstr.insert(i + shift, '-')
        shift += 1
    return ''.join(rstr[::-1])
###################################################################################################
"""
Sort the letters in the string s by the order they occur in the string t.
input: "weather"
ouput: "therapyw"
"""
def sortByString(s, t):
    s_list = list(s)
    final_word = []
    for i in t:
        if i in s_list:
            i_count = s_list.count(i)
            for j in range(i_count):
                final_word.append(i)
    return ''.join(final_word)
###################################################################################################
"""
Given an absolute file path (Unix-style), shorten it to the format /<dir1>/<dir2>/<dir3>/....
* I need to come back to this one as I have learned a lot about regex since solving this problem
input: "/mpJN/..///../../ubYgf/tFM/"
output: "/ubYgf/tFM"
"""
def simplifyPath(path):
    s = path
    s = re.sub(r'\/\.\/', '/', s)
    s = re.sub(r'\/\.\/', '/', s)
    print(s)
    s = re.sub(r'\/{2,}', '/', s)
    back_count = len(re.findall(r'\/\.\.', s))
    for i in range(back_count):
        s = re.sub(r'[\w\.]+\/\.\.', '', s, count=1)
        s = re.sub(r'\/{2}', '/', s)
    s = re.sub(r'\.\.', '', s)
    s = re.sub(r'\/{2}', '/', s)
    s = re.sub(r'\/$', '', s) if len(s) != 1 else s
    return s
###################################################################################################
"""
You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
Try to solve this in-place - in a real interview, you will only be allowed to use O(1) additional memory.
* simply problem, but I liked it, so I'm including it
input: 
[[10,9,6,3,7], 
 [6,10,2,9,7], 
 [7,6,3,8,2], 
 [8,9,7,9,9], 
 [6,8,6,8,2]]
output:
[[6,8,7,6,10], 
 [8,9,6,10,9], 
 [6,7,3,2,6], 
 [8,9,8,9,3], 
 [2,9,2,7,7]]
"""
def rotateImage(a):
    return [i[::-1] for i in list(zip(*a))]
###################################################################################################
"""
Write a function that takes a string as input and returns the string with only the vowels reversed. (aeior and not y)
input: "hello, world"
output: "hollo, werld"
"""
def reverseVowelsOfString(s):
    s_list = list(s)
    vowels = list(re.finditer(r'[aeiou]', s, re.I))
    values = [i.group() for i in vowels]
    for i in vowels:
        pos = i.start()
        s_list[pos] = values.pop()
    return ''.join(s_list)
###################################################################################################
"""
Reverse the order of words in a given string sentence. You can assume that sentence does not have any 
leading, trailing or repeating spaces.
input: "Man bites dog"
output: "dog bites Man"
"""
def reverseSentence(sentence):
    return ' '.join(sentence.split()[::-1])
###################################################################################################





