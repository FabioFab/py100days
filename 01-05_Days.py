# ###############################
# DAY01
# ###############################
# It creates a list of leap years, given a fixed range
my_leap_years = []

for i in range(1790, 2021):
    if (i % 4 == 0):  # can be divided by 4
        if (i % 100 != 0):  # can't be divided by 100
            my_leap_years.append(str(i))
        elif (i % 400 == 0):  # divisible by 400
            my_leap_years.append(str(i))


print(','.join(my_leap_years))
print(my_leap_years)
print(my_leap_years[0])
print(my_leap_years[1])


# ###############################
# DAY02
# ###############################
# A function to check whether a given integer is positive
def positive_integer_check(number):
    if number > 0:
        return True
    else:
        return False


# A function to run factorial operation of a given number
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print("Enter an integer number please, and I'll return the factorial: ")
num = int(input())
print(factorial(num))


# ###############################
# DAY03
# ###############################
# Given a number in input, it creates a dictionary of squares numbers
# from 1 to given number (e.g. input 4, output {1:1, 2:4, 3:9, 4:14} )
def dictionary_of_squares(number):
    d = dict()
    for i in range(1, number + 1):  # Memo: range goes from "first" number to "last minus 1"
        d[i] = i * i
    return d


print("Enter an integer number please, and I'll return a dictionary of squares from 1 to your number: ")
num = int(input())
print(dictionary_of_squares(num))


# ###############################
# DAY04
# ###############################
# put input into a list
def values_in_list(inputvalues):
    list = inputvalues.split(",")
    return list


# Convert list into a tuple
def list_to_tuple(list):
    return tuple(list)


print("Please enter some comma separated numbers, and I'll return a list and a tuple: ")
values = input()
print(values_in_list(values))
tuple = list_to_tuple(values_in_list(values))
print(tuple)


# ###############################
# DAY05
# ###############################
# creation of 1 class and 2 methods

class SampleClass(object):
    # initialise function to define attributes, if any, for the data type
    def __init__(self):
        self.s = ''

    def def_string(self):
        self.s = input("Please type a string: ")

    def print_upper_string(self):
        print(self.s.upper())


# This line of code will call the class SampleClass and the next one print the memory location
x = SampleClass()
print(x)
# This code executes the methods in the class, calling them
x.def_string()
x.print_upper_string()
