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

# ################################
# # DAY37
# ################################

# Reverse the words in a string, i.e. from "I am free" to "free am I"

def reverse_string(s):
    s = s.split()
    print("\nThis is how 'split' works: ")
    print(s)
    s.reverse()
    print("\nThis is how 'reverse' works: ")
    print(s)
    return " ".join(s)  # note that, if I was reversing and object, i would have used "reversed(object)" with "d"

# a compact method to do the same is this
def reverse_string2(s):
        return " ".join(reversed(s.split()))  # see comment above about reverse vs reverseD

# amd this is just another way:
def reverse_string3(s):
        return " ".join(s.split()[::-1])


print("Please type the string to be reversed: ")
string0 = input()
print("\nThis is how input is stored: ")
print(string0)
print("\nThis is how join 'works':\n" + reverse_string(string0))

print("\nAlternative method 2:\n" + reverse_string2(string0))
print("\nAlternative method 3:\n" + reverse_string3(string0))