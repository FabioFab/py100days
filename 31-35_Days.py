# # ################################
# # # DAY31
# # ################################
#
# from datetime import datetime as dt
#
# def anagrams(s1, s2):
#     s1 = s1.replace(" ","").lower()
#     s2 = s2.replace(" ","").lower()
#     if sorted(s1) == sorted(s2):
#         return True
#     else:
#         return False
#
# def anagrams_v2(s1, s2):
#     s1 = s1.replace(" ","").lower()
#     s2 = s2.replace(" ","").lower()
#     if len(s1) != len(s2):
#         return False
#     count = {}  # building a dictionary of letters, counting number of each one
#     for letters in s1:
#         if letters in count:
#             count[letters] = count[letters] + 1  # adding
#         else:
#             count[letters] = 1
#     for letters in s2:
#         if letters in count:
#             count[letters] = count[letters] - 1  # reducing
#         else:
#             count[letters] = 1
#     for k in count:
#         if count[k] != 0:  # if they are all zero, inputs were identical
#             return False
#     return True
#
#
# print("Checking 2 sentences and telling you whether they are anagram of each other.")
# print("Capital letters and spaces will be ignored.")
# print("Type word and or sentence 1: ")
# inp1 = input()
# print("Type word and or sentence 2: ")
# inp2 = input()
#
# t0 = dt.now()
# if anagrams(inp1, inp2):
#     print("\n" + inp1 + "\nand\n" + inp2 + "\nare anagrams")
# else:
#     print("The 2 input sentences are not anagrams.")
# finaldt0 = dt.now() - t0
# print("The anagram check operation (v1) took " + str(finaldt0) + " to execute.")
#
#
# t1 = dt.now()
# if anagrams_v2(inp1, inp2):
#     print("\n" + inp1 + "\nand\n" + inp2 + "\nare anagrams")
# else:
#     print("The 2 input sentences are not anagrams.")
# finaldt1 = dt.now() - t1
# print("The anagram check operation (v2) took " + str(finaldt1) + " to execute.")
#
# ## keep this commented: they are too fast and they rerutn error division by zero
# # print("Ration v1/v2 is " + str(finaldt0 / finaldt1) + "\n")
#
# # ################################
# # # DAY32
# # ################################
#
# # given an array of integer, identify any pairs whose sum is an input k value
#
# def pair_comparer(arr, k):
#     if len(arr) < 2:
#         print("input array too small")
#
#     seen = set()
#     output = set()
#     k = int(k)
#
#     for n in arr:
#         target = k - int(n)
#         if target not in seen:
#             seen.add(int(n))
#         else:
#             output.add((min(int(n), target), max(int(n), target)))
#     print("\n".join(map(str, list(output))))
#     print(str(list(output)))
#
# print("Given an array of integer, identify any pairs whose sum is an input k value")
# print("Please type the integer for the array, separate by a comma: ")
# inp = input()
# print("Please provide the number you want the pair be equal to, when summed: ")
# total = input()
# inp_array = []
# inp_array = inp.split(",")
# print(inp)
# print(inp_array)
# print("Here is the list of couple of integers whose sum is " + total)
# print(pair_comparer(inp_array, total))

# ################################
# # DAY33 AND DAY 34 AND DAY 35 (3 days)
# ################################

# array 1 is made of integer numbers
# array 2 is made of similar to array 1, with missing number
# function to identify the missing numbers

import collections


def finder1(arr1, arr2):
    arr1.sort()  # just numbers in input, so no need to lower or remove spaces
    arr2.sort()
    d = collections.defaultdict(int)  # it creates a deafult dictionary of integer numbers
    # print(d)
    for j in arr2:
        d[j] = d[j] + 1
    for j in arr1:
        if d[j] == 0:
            return j
        else:
            d[j] = d[j] -1


def finder2(arr1, arr2):
    arr1.sort()  # just numbers in input, so no need to lower or remove spaces
    arr2.sort()
    for i, j in zip(arr1, arr2):
        if i != j:
            return i
    return arr1[-1]


def finder3(arr1, arr2):  # this is much better, if finds all numbers and does that for both lists
    x1 = set(arr1)  # a set is an unordered of unique elements
    x2 = set(arr2)
    # print(x1)
    # print(x2)
    x = list(x1 - x2)
    y = list(x2 - x1)
    return x, y

print("Type 2 arrays of integer and will identify the numbers not included in the other.")
print("input array 1 please: ")
a0 = input()
a1 = a0.split(",")
int_a1 = [int(i) for i in a1]
print("input array 1 please: ")
a2 = input().split(",")
int_a2 = [int(i) for i in a2]
# print(a0)
# print(a1)
# print(int_a1)
print("\nFirst function shows just the first integer included in the first, but not in the second:")
print(finder1(int_a1, int_a2))
print("\nSecond function shows just the first integer included in the first, but not in the second:")
print(finder2(int_a1, int_a2))
print("\nBest function:")
print("- firsts list is made of numbers in the first input array, not included in the second")
print("- second list is the other way round")
print(finder3(int_a1, int_a2))