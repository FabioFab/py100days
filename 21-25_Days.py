# ################################
# # DAY21
# ################################
#
# import numpy as np
from numpy import *

# arr01 = {i, [2,3,4,5]}
arr02 = array([2, 3, 4, 5], int)
print(arr02)

import numpy as np
print(np.__version__)

# covert a list into a 1D array (np.array)

listA = [1, 2, 4, 5, 6, 7]
print("Starting list ", listA)

one_dim_array = np.array(listA, int) # or even 'dtype = int' would work
print("My first 1D array is ", one_dim_array)
