# # ################################
# # # DAY36
# # ################################
#
# # Input array of integer, positive and negative, and makes the maximum sum (i.e. ignores the negatives)
#
#
# def sum(arr):
#     if len(arr) == 0:
#         return 0
#     max_sum = arr[0]
#     current_sum = arr[0]
#     for i in range(1, len(arr)):  # or, for i in arr[1:]:
#         current_sum = current_sum + arr[i]
#         if current_sum > max_sum:
#             max_sum = current_sum
#         else:
#             current_sum = current_sum - arr[i]
#     if arr[0] < 0:
#         max_sum = max_sum - arr[0]
#     return max_sum
#
#
# def sum2(arr): # this execute a different operation, i.e. counts continuous increment
#     if len(arr) == 0:
#         return 0
#     max_sum = arr[0]
#     current_sum = arr[0]
#     for i in range(1, len(arr)):  # or, "for i in arr[1:]:" and then i is the content, not just the index
#         current_sum = max((current_sum + arr[i]), arr[i])
#         max_sum = max(current_sum, max_sum)
#     return max_sum
#
#
# print("Input array of integer, positive and negative, and I will provide the maximum total: ")
# # # a0 = input()
# # # a1 = a0.split(",")
# # # int_a1 = [int(i) for i in a1]
# # # print(a0)
# # # print(a1)
# # # print(int_a1)
# int_a1 = [int(i) for i in input().split(",")]
# print("This is the maximum total: ")
# x = sum(int_a1)
# if x == 0:
#     print("Invalid input, please provide longer array.")
# else:
#     print(sum(int_a1))
#
# print("This counts continuous increment: ")
# print(sum2(int_a1))
#
#################################
## DAY37
#################################
#
# # Reverse the words in a string, i.e. from "I am free" to "free am I"
#
# def reverse_string(s):
#     s = s.split()
#     print("\nThis is how 'split' works: ")
#     print(s)
#     s.reverse()
#     print("\nThis is how 'reverse' works: ")
#     print(s)
#     return " ".join(s)  # note that, if I was reversing and object, i would have used "reversed(object)" with "d"
#
# # a compact method to do the same is this
# def reverse_string2(s):
#         return " ".join(reversed(s.split()))  # see comment above about 'reverse' vs 'reversed'
#
# # amd this is just another way:
# def reverse_string3(s):
#         return " ".join(s.split()[::-1])
#
# # amd this is just another way:
# def reverse_string_and_words4(s):
#         length = len(s)
#         i = 0
#         a_word = []
#
#         while i < length:
#             if s[i] != " ":
#                 word_start = i  # this is just telling me where words start
#                 while i < length and s[i] != " ":
#                     i = i + 1
#                 a_word.append(s[word_start:i])
#
#             i = i + 1
#
#         return "".join(reversed(s))
#
#
# print("Please type the string to be reversed: ")
# string0 = input()
# print("\nThis is how input is stored: ")
# print(string0)
# print("\nThis is the final result, i.e. how 'join' works:\n" + reverse_string(string0))
#
# print("\nAlternative method 2:\n" + reverse_string2(string0))
# print("\nAlternative method 3:\n" + reverse_string3(string0))
# print("\nAlternative method to reverse and words:\n" + reverse_string_and_words4(string0))
#
#
#
# # ################################
# # # DAY38
# # ################################
#
# # Compare 2 arrays and return True/False if they have same letters, just shifted
# # array don't have duplicated letters
#
#
# def rotation(l1, l2):
#
#     if len(l1) != len(l2):
#         return False
#
#     key = l1[0]
#     key_index = 0
#
#     for i in range(len(l2)):
#         if l2[i] == key:
#             key_index = i
#             break
#
#     if key_index == 0:  # this is true if we didn't find any key
#         return False
#
#     for x in range(len(l1)):
#         l2index = (key_index + x) % len(l1)
#
#         if l1[x] != l2[l2index]:
#             return False
#     return True
#
#
# print("Given 2 lists of characters, it compares and return True if they are identical and")
# print("have only a different starting index position, e.g. a,3,w,f and w,f,a,3.")
# print("Type first list of characters, comma separated and no replications: ")
# in1 = input()
# in1 = in1.split(",")
# print("Type second list of characters, comma separated and no replications: ")
# in2 = input()
# in2 = in2.split(",")
# # print(in1)
# print("\n")
# # print(in2)
# print("Comparison check: " + str(rotation(in1, in2)))
# # print("Comparison check: " + str(rotation([1,2,3], [3,1,2])))
#
#
# # ################################
# # # DAY39
# # ################################
#
# # Compare 2 arrays and return common elements
#
# def comparison(x1, x2):
#     p1 = 0
#     p2 = 0
#     common = []
#
#     while p1 < len(x1) and p2 < len(x2):
#         if x1[p1] == x2[p2]:
#             common.append(x1[p1])
#             p1 = p1 + 1
#             p2 = p2 + 1
#         elif x1[p1] > x2[p2]:
#             p2 = p2 + 1
#         else:
#             p1 = p1 + 1
#     return common
#
#
#
#
# print("Type 2 arrays of integer and will identify the numbers not included in the other.")
# print("input array 1 please: ")
# a0 = input()
# a1 = a0.split(",")
# int_a1 = [int(i) for i in a1]
# print("input array 1 please: ")
# a2 = input().split(",")
# int_a2 = [int(i) for i in a2]
# #print(a0)
# #print(a1)
# print(comparison(int_a1, int_a2))


# ################################
# # DAY40
# ################################

# "mine sweeper" takes 3 arguments as input
# firsts one is the list of bomb locations
# and the other two arguments are row and columns

def mine_sweeper(bombs, num_r, num_c):
    # this creates a fields full of zeroes in each cell
    field = [[0 for i in range(num_c)] for j in range(num_r)]
    # print(field)
    for bomb_location in bombs:
        # this way I place a "-1" in each bomb location
        (bomb_row, bomb_col) = bomb_location
        field[bomb_row][bomb_col] = -1
        # print(field)

         # "+2" here below just because it's used as range in the following code
        row_range = range(bomb_row - 1, bomb_row + 2)
        col_range = range(bomb_col - 1, bomb_col + 2)
        for i in row_range:
            ci = 1
            for j in col_range:
                cj = j
                if ( (i >= 0) and (i < num_r) and (j >= 0) and (j < num_c) and (field[i][j] != -1)):
                    field[i][j] += 1
    return field





print("Create a mine sweeper field. Inputs are:"
      "1. list of bomb positions"
      "2. rows of field"
      "3. column of the field")
print("enter the number of bombs you want to add:")
n_bmb = int(input())
bomb_list = []
for i in range(1, n_bmb+1):
    print("Input bomb coordinate with comma separator:")
    bmb = input().split(",")
    bmb = [int(i) for i in bmb]
    # print(bmb)
    bomb_list.append(bmb)
    print(bomb_list)


print("input row field size please: ")
rw = int(input())
print("input col field size please: ")
cl = int(input())

print(mine_sweeper(bomb_list, rw, cl))