# # ################################
# # # DAY41
# # ################################
#
# # Identify the most frequent element in an array
# # It creates a dictionary and keep count of the occurrences
# from collections import Counter
#
#
# # given and array as input, it creates a dictionary that counts the freq of elements
# def dict_create(arr):
#     # freq_dict = dict()
#     freq_dict = {}
#     for i in arr:
#         if i in freq_dict:
#             # increment value
#             freq_dict[i] = freq_dict[i] + 1
#         else:
#             # append value
#             # freq_dict[i] = 1
#             # freq_dict.update({i: 1})
#             freq_dict[i] = 1
#     return freq_dict
#
# # given a dict, it gives you the most common element
# def max_count(dictio):
#     x = Counter(dictio)
#     # most_freq = x.most_common(1)
#     # print(most_freq[0][0])
#     return x.most_common(1)[0][0]
#
#
# # another version to solve it
# def max_frequent(list_inp):
#     my_dict = {}
#     max_cnt = 0
#     max_item = None
#
#     for i in list_inp:
#         if i not in my_dict:
#             my_dict[i] = 1
#         else:
#             my_dict[i] += 1
#
#         if my_dict[i] > max_cnt:
#             max_cnt = max_cnt + 1
#             max_item = i
#     return max_item, max_cnt
#
#
# print("Type list of characters, comma separated: ")
# lst = input().split(",")
# dct = dict_create(lst)
# print(">> Version 1 <<")
# print("This is the frequency of characters: ")
# print(dct)
# print("The most common character is :")
# print(max_count(dct))
# print(">> Version 2 <<")
# outcome = max_frequent(lst)
# for i in range(0, 2):
#     if i == 0:
#         print("The most common value is: ")
#         print(outcome[i])
#     else:
#         print("which appears " + str(outcome[i]) + " times.")
#
#
#
# ################################
# # DAY42
# ################################
#
#
# # Given a string, check that all characters are unique
# def uniqueness(input_string):
#     # first, spaces are to be removed
#     input_string = input_string.replace(" ", "")
#     # "set" creates an unordered collection of unique elements
#     # print(set(input_string))
#     return len(set(input_string)) == len(input_string)
#
#
# def uniqueness2(input_string):
#     # first, spaces are to be removed
#     input_string = input_string.replace(" ", "")
#     char_in_list = set()
#     for characters in input_string:
#         if characters in char_in_list:
#             return False
#         else:
#             char_in_list.add(characters)
#     return True
#
#
#
# print(" Please type a string ")
# str_in = input()
#
# print(">> Version 1 <<")
# if uniqueness(str_in):
#     print("All characters are unique, well done!")
# else:
#     print("Not all characters in the string are unique")
#
# print(">> Version 2 <<")
# if uniqueness2(str_in):
#     print("All characters are unique, well done!")
# else:
#     print("Not all characters in the string are unique")
#

# ################################
# # DAY43
# ################################


# Given a string, return unique characters and only 1 occurrence of not unique
def non_repeating(input_string):
    # first, spaces are to be removed
    input_string = input_string.replace(" ", "")
    # second, all lowercase
    input_string = input_string.lower()

    char_in_list = {}
    for c in input_string:
        if c in char_in_list:
            char_in_list[c] += 1
        else:
            char_in_list[c] = 1

    all_uniques = []
    # x[1] represents the second element, i.e. the number of occurrences rather then the character itself
    y = sorted(char_in_list.items(), key=lambda x: x[1])
    print(y)
    for item in y:
        if item[1] == y[0][1]:
            all_uniques.append(item)
    return all_uniques


print(" Please type a string ")
str_in = input()
print("These are the unique characters: ")
print(non_repeating(str_in))