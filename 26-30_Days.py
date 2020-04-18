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

# ################################
# # DAY27 (or 28?)
# ################################

