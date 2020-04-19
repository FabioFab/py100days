# # ################################
# # # DAY26 (or 27?)
# # ################################
#
# import numpy as np
#
# # dot product explained
# arr1 = np.array([1, 3])
# arr2 = np.array([2, 4])
# print(type(arr1))
# print(arr1)
# print(arr2)
#
# print("this executes multiplication, i.e. (1*2) + (3*4) = 14")
# print("careful, cause the order matters, so array1 * array2 is very different from array2 * array1!")
# x = np.dot(arr1, arr2)
# print(x)
#
# from datetime import datetime as dt
#
# # This creates 2 arrays of 100 random elements each
# arr3 = np.random.randn(100)
# arr4 = np.random.randn(100)
# T = 100000
# # print(arr3, "\n", arr4)
#
# def slow_dot_product(a, b):
#     result = 0
#     for c, d in zip(a, b):
#         result = result + c*d
#     return result
#
# t0 = dt.now()
# for tt in range(T):
#     slow_dot_product(arr3, arr4)
# finaldt0 = dt.now() - t0
# print("The for loop took " + str(finaldt0) + " to execute.")
#
# t1 = dt.now()
# for tt in range(T):
#     dotstd = np.dot(arr3, arr4)
#     # arr3.dot(arr4)
# finaldt1 = dt.now() - t1
# print("The dot operation took " + str(finaldt1) + " to execute.")
#
# print("so the numpy dot operation is " + str(finaldt0/finaldt1) + " times faster.")
#
# import numpy as np
# arr5 = np.array([[1, 2], [3, 4]])  # array 2x2
# listA = [ [1, 2], [3, 4]]  # list of lists
# print(arr5)
# print(listA)
# print(listA[0])
# print(listA[0][0])
# print(arr5[0][0])
# print(arr5[0, 0])  # this can be done only with array, not with lists
#
# # now I transpose the matrix
# arr6 = np.array([[1, 7, 3], [3, 4, 9]])
# print(arr6)
# print(arr6.T)
#
# print(" 'random' create data follow the Unifom distribution, whereas 'randn' follow Gaussian distribution")
# arr7 = np.random.random((5, 5))  # this has double parentesis
# gaus = np.random.rand(5, 5)
# print(arr7)
# print(gaus)
# mean = gaus.mean()
# variance = gaus.var()
# print(mean)
# print(variance)
#
# # ################################
# # # DAY27 (or 28?)
# # ################################
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# # a few examples of sin and cos diagrams (this is not part of the 100days learning
#
# #
# # create the figure and two axes (two rows, one column)
# #
# figA, (ax1, ax2) = plt.subplots(2, 1)
#
# # create a plot of y = sin(x) on the first row
# x1 = np.linspace(0, 4 * np.pi, 100)
# y1 = np.sin(x1)
# ax1.plot(x1, y1)
#
# # create a plot of y = cos(x) on the second row
# x2 = np.linspace(0, 4 * np.pi, 100)
# y2 = np.cos(x2)
# ax2.plot(x2, y2)
#
# # save the figure
# plt.savefig("sin_cos.png")
#
# #
# # create the figure and two axes (one row, one column)
# #
# figB, (ax3, ax4) = plt.subplots(2, 1)  # I could have typed plt.subplots(1, 1)
#
# # combine the current axes into one plot
# ax4 = ax3.twinx()
#
# # create a plot of y = sin(x) on the first row
# x3 = np.linspace(0, 4 * np.pi, 100)
# y3 = np.sin(x3)
# # Add a label for the legend
# ax3.plot(x1, y3)
#
# # create a plot of y = cos(x) on the second row
# x4 = np.linspace(0, 4 * np.pi, 100)
# y4 = np.cos(x4)
# ax4.plot(x4, y4)
#
# # save the figure
# plt.savefig("sin_cos2.png")
#
#
#
# # create the figure and two axes (two rows, one column), with labels, axis names and title
# figC, (ax5, ax6) = plt.subplots(2, 1)
#
# # combine the current axes into one plot
# ax6 = ax5.twinx()
#
# # create a plot of y = sin(x) on the first row
# x5 = np.linspace(0, 4 * np.pi, 100)
# y5 = np.sin(x5)
# function1 = ax5.plot(x5, y1, "b", label="Sin")
# ax1.plot(x5, y5)
#
# # create a plot of y = cos(x) on the second row
# x6 = np.linspace(0, 4 * np.pi, 100)
# y6 = np.cos(x6)
# function2 = ax6.plot(x6, y6, "r", label="Cos")
# ax2.plot(x6, y6)
#
# functions = function1 + function2
# labels = [f.get_label() for f in functions]
# #  Notice the loc=0 parameter. This sets the location of the legend.
# #  loc=0 automatically selects the best place for the legend
# plt.legend(functions, labels, loc=0)
#
# # Add x-label (only one, since it is shared) and the y-labels
# ax5.set_xlabel("$x$")
# ax5.set_ylabel("$y_1$")
# ax6.set_ylabel("$y_2$")
#
# # Add the title
# plt.title("Sin and Cos")
#
# # Adjust the figure such that all rendering components fit inside the figure
# plt.tight_layout()
#
# # save the figure
# plt.savefig("sin_cos3.png")
#
# #
# #
# # this restart the 100days
# #
# #
#
# plt.style.use("bmh")
#
# # setup  runtime comparisons
# n = np.linspace(1, 20)
# labels = ["constant", "Log", "Linear", "Log Linear", "Quadratic", "Cube", "Exponential"]
# big_o = [np.ones(n.shape), np.log(n), n, n*np.log(n), n**2, n**3, 2**n]
#
# # plot setup
# plt.figure(figsize=(12,10))
# plt.ylim(0, 50)
#
# for i in range(len(big_o)):
#     plt.plot(n, big_o[i], label = labels[i])
#
# plt.legend(loc=0)
# plt.ylabel("Relative Runtime")
# plt.xlabel("n")
#
# plt.savefig("big_o.png")
#
#
# # ################################
# # # DAY28 (or 29?)
# # ################################
#
# # big O examples
#
# # O(1) i.e. constant
# # it prints first value
# def function_constant(values):
#     print(values[0])
#
#
# print("O(1) i.e. constant")
# function_constant([7, 89, 99])
#
# # O(n) i.e. linear
# def function_linear(list):
#     for i in list:
#         print(i)
#
# print("O(n) i.e. linear")
# function_linear([3, 45, 22, 44, 2])
#
# # O(n^2) i.e. quadratic
# def function_quad(list):
#     for i1 in list:
#         for i2 in list:
#             print(i1, i2)
#
#
# print("O(n^2) i.e. quadratic")
# function_quad([7, 89, 99])


# ################################
# # DAY29 (or 30?)
# ################################

# list []
# tuple 9,0
# string (" ")
# they all support indexing

# memory is addressed in byte i.e. 8 bits
# unicode characthers are represented ass 16 bits = 2 bytes
# they are always stored and retrieved in O(1) constant time

# so the word SAMPLE would be made of 6 characters = 12 bytes = array of 6 characters

import sys
n = 10
data = []
print(data)
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)  # give me the size of data in bytes
    print("length: {0:3d}; size in bytes: {1:4d} ".format(a, b))  # 3d means "take 3 integer places"
    print("\n")
    data.append(n)
    print(data)


