# # ################################
# # # DAY21
# # ################################
# # numpy is a package specialised in multi dimensional array
# #
# # import numpy as np
# # from numpy import *
# #
# # arr01 = {i, [2,3,4,5]}
# # arr02 = array([2, 3, 4, 5], int)
# # print(arr02)
#
# import numpy as np
# print(np.__version__)
#
# # convert a list into a 1D array (np.array)
# print("This example print a list and print the converted 1dimensional array.\n")
# listA = [1, 2, 4.9, 5, 6, 7]
# print("Starting list ", listA)
#
# one_dim_array = np.array(listA, dtype=int)  # 'dtype = int' forces to round to the closest integer
# print("My first 1D array is ", one_dim_array)
#
#
# # I am now to use ARANGE, and this is how it works:
# #
# # start : number, optional
# #     Start of interval. The interval includes this value. The default start value is 0.
# # stop : number
# #     End of interval. The interval does not include this value, except in some cases where step is not an integer and floating point round-off affects the length of out.
# # step : number, optional
# #     Spacing between values. For any output out, this is the distance between two adjacent values, out[i+1] - out[i]. The default step size is 1. If step is specified as a position argument, start must also be given.
# # dtype : dtype
# #     The type of the output array. If dtype is not given, infer the data type from the other input arguments.
#
#
# print("""This is instead the creation of a matrix 3 x 3, with value provided in the range
# (from lower number included to the upper number excluded)""")
# x01 = np.arange(22, 31).reshape(3, 3)
# print(x01)
#
# print("""These instead create a 1D array and a 2D array""")
# x02 = np.arange(32, 41, 2)
# x03 = np.arange(32, 43, 2).reshape(3, 2)
# x04 = np.arange(32, 43, 2).reshape(2, 3)
# print(x02)
# print(x03)
# print(x04)
#
# print("Create an all zero vector, size 10")
# x05 = np.zeros(10)
# print(x05)
# print("Now change values in position 3 and 6")
# x05[3] = 33
# x05[6] = 21
# print(x05)
# print("Now change values in position 2 and 5")
# x05[[2, 5]] = 11
# print(x05)
#
# print("Create an all zero vector, size 10. See the difference from above")
# x06 = np.zeros(10, dtype=int)
# print(x06)
#
#
# print("Create an array and reverse it")
# x07 = np.arange(6, 21)
# print(x07)
# x07 = x07[::-1]
# print(x07)
#
#
#
# # ################################
# # # DAY22
# # ################################
# #
# x, y = 0, 1
#
# while y < 50:
#     print(x, y)
#     x = y
#     y = x+y
#     print(x, y)
#
# # ################################
# # # DAY23
# # ################################
# # Not really useful.. again explanation on how to represent letters with asterisks and spaces. Ref day 13


# ################################
# # DAY24
# ################################
# numpy day

import numpy as np

a01 = np.ones((6, 6))
print("""First example. 
Normal after creation:\n""")
print(a01)

print("After manipulation:\n")
a01[1:-1] = 0  # keep row 0 to value "1"and override all the rest to "0" till the end minus 1
print(a01)


a02 = np.ones((6, 6))
print("""\n\nSecond example. 
Normal after creation:\n""")
print(a02)

print("After manipulation:\n")
a02[1:-1, 1:-1] = 0
# keep row 0 to value "1" and override all the rest to "0" till the last row, minus 1
# likewise keep row 0 to value "1" and override all the rest to "0" till the last column, minus 1
print(a02)

print("\ncreation of an array")
a03 = [10, 20, 30]
print(a03)
print("appending number to the array")
a03 = np.append(a03, [[11, 22, 33], [44, 55, 66]])
print(a03)
print("sorting the array")
a03 = np.sort(a03)
print(a03)

print("\ncreation of an empty array")
a04 = np.empty([6, 6])
print(a04)


