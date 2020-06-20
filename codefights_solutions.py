
# ###################################################################################################
# """
# Sudoku checker
# input:
# [[1,2,3,4,5,6,7,8,9],
#  [4,6,5,8,7,9,3,2,1],
#  [7,9,8,2,1,3,6,5,4],
#  [1,2,3,4,5,6,7,8,9],
#  [4,6,5,8,7,9,3,2,1],
#  [7,9,8,2,1,3,6,5,4],
#  [1,2,3,4,5,6,7,8,9],
#  [4,6,5,8,7,9,3,2,1],
#  [7,9,8,2,1,3,6,5,4]]
# output: False
# """
# def sudoku(grid):
#     check_list = [i for i in range(1, 10)]
#
#     if sum([sorted(list) == check_list for list in grid]) != 9:
#         return False
#
#     if sum(([sorted(list) == check_list for list in list(zip(*grid))])) != 9:
#         return False
#
#     for section in range(0, 9, 3):
#         for square in range(0, 9, 3):
#             sub_grid = [[grid[section + e][square + i] for i in range(3)] for e in range(3)]
#             if sorted([i for row in sub_grid for i in row]) != check_list:
#                 return False
#     return True
# ###################################################################################################
# # INTERVIEW PRACTICE SECTION
# ###################################################################################################
# """
# Note: Write a solution with O(n2) time complexity, since this is what you would be asked to do during a real
# interview. You have an array a composed of exactly n elements. Given a number x, determine whether or not a
# contains three elements for which the sum is exactly x.
# input: x: 986
# a: [557, 217, 627, 358, 527, 358, 338, 272, 870, 362, 897, 23, 618, 113, 718, 697, 586, 42, 424, 130, 230, 566, 560, 933]
# output:True
# """
# import itertools
#
# def tripletSum(x, a):
#     below_x = [i for i in a if i < x]
#     for pair in itertools.combinations(below_x, 3):
#         if sum(pair) == x:
#             return True
#     return False
# ###################################################################################################
# """
# Given an array of words and a length l, format the text such that each line has exactly l characters and is
# fully justified on both the left and the right. Words should be packed in a greedy approach; that is, pack
# as many words as possible in each line. Add extra spaces when necessary so that each line has exactly l characters.
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not
# divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text and lines with one word only, the words should be left justified with no extra space
# inserted between them.
# input: ["This", "is", "an", "example", "of", "text", "justification."]
# ouput:
# ["This    is    an",
#  "example  of text",
#  "justification.  "]
#  """
# import textwrap
# def textJustification(words, L):
#     words = [word if len(word) > 0 else '~' for word in words]
#     lines = textwrap.wrap(' '.join(words), L)
#     lines[-1] = lines[-1].ljust(L, ' ')
#     for l in range(len(lines)):
#         if '~' in lines[l]:
#             lines[l] = '{}'.format(' ' * L)
#             continue
#         line_length = len(lines[l])
#         gaps = [gap.regs[0][0] for gap in re.finditer('\s', lines[l])]
#         if not gaps:
#             lines[l] = lines[l].ljust(L, ' ')
#         else:
#             while line_length < L:
#                 for i in range(len(gaps)):
#                     if line_length == L:
#                         break
#                     gap_index = gaps[i]
#                     line_list = [k for k in lines[l]]
#                     line_list.insert(gap_index, ' ')
#                     lines[l] = ''.join(line_list)
#                     line_length += 1
#                     for k in range(i, len(gaps)):
#                         gaps[k] += 1
#     return lines
# ###################################################################################################
# """
# Valid Sudoku Puzzle (Unsolved: '.' equals empty spaces)
# input:
# [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
#  ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
#  ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
#  ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
#  ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
#  ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
#  ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
#  ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
#  ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
# output: False
# """
# def sudoku2(grid):
#     for row in grid:
#         values = [i for i in row if i != '.']
#         if len(values) != len(set(values)):
#             return False
#
#     columns = [i for i in zip(*grid)]
#     for column in columns:
#         values = [i for i in column if i != '.']
#         if len(values) != len(set(values)):
#             return False
#
#     for row in range(0,9,3):
#         for col in range(0,9,3):
#             square = grid[row][col:col + 3] + grid[row + 1][col:col + 3] + grid[row + 2][col:col + 3]
#             values = [i for i in square if i != '.']
#             if len(values) != len(set(values)):
#                 print('lsfkj')
#                 return False
#     return True
# ###################################################################################################
# """
# The string s contains dashes that split it into groups of characters. You are given an integer k that represents
# the number of characters in groups that your output should have. Your goal is to return a new string that breaks
# s into groups with a length of k by placing dashes at the correct intervals. If necessary, the first group of
# characters can be shorter than k. It is guaranteed that there are no consecutive dashes in s.
# input: "?CC?-[yiq2bg-Ie9?z!e-2X1i*k4-8ZMjllM-VEX2v%*"
# output: "?CC?-[yiq2bg-Ie9?z!e-2X1i*k4-8ZMjllM-VEX2v%*"
# """
# def stringReformatting(s, k):
#     rstr = list(re.sub('-', '', s)[::-1])
#     shift = 0
#     for i in range(k, len(rstr), k):
#         rstr.insert(i + shift, '-')
#         shift += 1
#     return ''.join(rstr[::-1])
# ###################################################################################################
# """
# Sort the letters in the string s by the order they occur in the string t.
# input: "weather"
# ouput: "therapyw"
# """
# def sortByString(s, t):
#     s_list = list(s)
#     final_word = []
#     for i in t:
#         if i in s_list:
#             i_count = s_list.count(i)
#             for j in range(i_count):
#                 final_word.append(i)
#     return ''.join(final_word)
# ###################################################################################################
# """
# Given an absolute file path (Unix-style), shorten it to the format /<dir1>/<dir2>/<dir3>/....
# * I need to come back to this one as I have learned a lot about regex since solving this problem
# input: "/mpJN/..///../../ubYgf/tFM/"
# output: "/ubYgf/tFM"
# """
# def simplifyPath(path):
#     s = path
#     s = re.sub(r'\/\.\/', '/', s)
#     s = re.sub(r'\/\.\/', '/', s)
#     print(s)
#     s = re.sub(r'\/{2,}', '/', s)
#     back_count = len(re.findall(r'\/\.\.', s))
#     for i in range(back_count):
#         s = re.sub(r'[\w\.]+\/\.\.', '', s, count=1)
#         s = re.sub(r'\/{2}', '/', s)
#     s = re.sub(r'\.\.', '', s)
#     s = re.sub(r'\/{2}', '/', s)
#     s = re.sub(r'\/$', '', s) if len(s) != 1 else s
#     return s
# ###################################################################################################
# """
# You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).
# Try to solve this in-place - in a real interview, you will only be allowed to use O(1) additional memory.
# * simply problem, but I liked it, so I'm including it
# input:
# [[10,9,6,3,7],
#  [6,10,2,9,7],
#  [7,6,3,8,2],
#  [8,9,7,9,9],
#  [6,8,6,8,2]]
# output:
# [[6,8,7,6,10],
#  [8,9,6,10,9],
#  [6,7,3,2,6],
#  [8,9,8,9,3],
#  [2,9,2,7,7]]
# """
# def rotateImage(a):
#     return [i[::-1] for i in list(zip(*a))]
# ###################################################################################################
# """
# Write a function that takes a string as input and returns the string with only the vowels reversed. (aeior and not y)
# input: "hello, world"
# output: "hollo, werld"
# """
# def reverseVowelsOfString(s):
#     s_list = list(s)
#     vowels = list(re.finditer(r'[aeiou]', s, re.I))
#     values = [i.group() for i in vowels]
#     for i in vowels:
#         pos = i.start()
#         s_list[pos] = values.pop()
#     return ''.join(s_list)
# ###################################################################################################
# """
# Reverse the order of words in a given string sentence. You can assume that sentence does not have any
# leading, trailing or repeating spaces.
# input: "Man bites dog"
# output: "dog bites Man"
# """
# def reverseSentence(sentence):
#     return ' '.join(sentence.split()[::-1])
# ###################################################################################################
# """
# Given a string s, recursively remove any adjacent duplicate characters that it contains.
# input: "acaaabbbacdddd"
# output: "acac"
# """
# def removeDuplicateAdjacent(s):
#     is_duplicate = re.search(r'(\w)\1+', s)
#     if not is_duplicate:
#         return s
#     return removeDuplicateAdjacent(re.sub(r'(\w)\1+', '', s))
# ###################################################################################################
# """
# Note: Avoid using built-in functions that convert integers to their binary representations. Write the solution
# that uses O(k) operations per test, where k is the number of bits set to 1. Write a function that takes an unsigned
# (positive) integer and returns the number of 1 bits its binary representation contains. This value is also known as
# the integer's Hamming weight.
# input: 84618
# output: 7
# """
# def numberOf1Bits(n):
#     bits = 0
#     while n != 0:
#         if n % 2 == 0:
#             n = n >> 1
#         else:
#             n = n >> 1
#             bits += 1
#     return bits
# ###################################################################################################
# """
# Given two strings, s and t, find the length of their longest common substring.
# input: s: "zxabcdezy" t: "yzabcdezx"
# output: 6
# """
# from difflib import SequenceMatcher
#
# def longestCommonSubstring(s, t):
#     return SequenceMatcher(None, s, t).find_longest_match(0, len(s), 0, len(t)).size
# ###################################################################################################
# """
# Determine whether the given number n is a power of two.
# input: 17179869184
# output: True
# """
# def isPowerOfTwo2(n):
#     return bin(n).count('1') == 1
# ###################################################################################################
# """
# A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits,
# such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.
# You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits,
# solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3],
# which should be interpreted as the word1 + word2 = word3 cryptarithm. If crypt, when it is decoded by replacing all
# of the letters in the cryptarithm with digits using the mapping in solution, becomes a valid arithmetic equation
# containing no numbers with leading zeroes, the answer is true. If it does not become a valid arithmetic solution,
# the answer is false.
# imput: crypt: ["SEND", "MORE", "MONEY"]
# solution: [["O","0"], ["M","1"], ["Y","2"], ["E","5"], ["N","6"], ["D","7"], ["R","8"], ["S","9"]]
# output: True
# """
# def isCryptSolution(crypt, solution):
#     c_dict = {i[0]:i[1] for i in solution}
#     n1 = ''.join([c_dict[i] for i in crypt[0]])
#     if re.match('[0][^.]', n1):
#         return False
#     n2 = ''.join([c_dict[i] for i in crypt[1]])
#     if re.match('[0][^.]', n2):
#         return False
#     n3 = ''.join([c_dict[i] for i in crypt[2]])
#     if re.match('[0][^.]', n3):
#         return False
#     return int(n1) + int(n2) == int(n3)
#
# ###################################################################################################
# """
# You have two version strings composed of several non-negative decimal fields that are separated by periods (".").
# Both strings contain an equal number of numeric fields. Return 1 if the first version is higher than the second
# version, -1 if it is smaller, and 0 if the two versions are the same. The syntax follows the regular semver
# (semantic versioning) ordering rules:
# 1.0.5 < 1.1.0 < 1.1.5 < 1.1.10 < 1.2.0 < 1.2.2
# < 1.2.10 < 1.10.2 < 2.0.0 < 10.0.0
# input: ver1: "1.0.1" ver2: "1.01.0"
# output: -1
# """
# def higherVersion2(ver1, ver2):
#     v1_list = [int(i) for i in ver1.split('.')]
#     v2_list = [int(i) for i in ver2.split('.')]
#     if v1_list == v2_list:
#         return 0
#     elif v1_list > v2_list:
#         return 1
#     else:
#         return -1
# ###################################################################################################
# """
# Let's define a group of anagrams as a list of words, where for each pair of words w1 and w2, w1 is an anagram of w2.
# Given a list of words, split it into the smallest possible number of groups of anagrams and return this number as the answer.
# input: ["tea", "eat", "apple", "ate", "vaja", "cut", "java", "utc"]
# output: 4
# """
# def groupsOfAnagrams(words):
#     return len(set([tuple(sorted(i)) for i in words]))
# ###################################################################################################
