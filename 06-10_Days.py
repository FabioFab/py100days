# https://www.youtube.com/watch?v=D3cWPAYf44s
# ###############################
# DAY06
# ###############################
# create a calculator, that, given d, will execute "squared root of (2*c*d)/h"
# this same calculator will accept a list in input too

c = 50
h = 30
import math
x = []
y = [i for i in input("Please enter a number or a comma separated lists of numbers (all different): ").split(",")]
for d in y:
    x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

# printing both input and result
# side note: the "for" below is bad coding, it works only if you input numbers different one another
for d in y:
    print("Here is the result of squared root of (2*" + str(c) + "*" + str(d) + ")/" + str(h) + "): ")
    for i in range(0, len(y)):
        if y[i] == d:
            print(x[i])

# Printing examples of the result
print("First result is " + str(x[0]))
print("Second result is " + str(x[1]))
print(",".join(x))
print(x)





# ###############################
# DAY07
# ###############################
# This day includes many different small excercises

# It creates a matrix of A x B size, where both A and B are given as input
input_size_matrix = input("Please enter 2 comma separated numbers to have an equal size matrix: ")
# I use the input numbers to create a list of 2 elements
size = [int(x) for x in input_size_matrix.split(",")]
row_size = size[0]
column_size = size[1]

# Here is the matrix, i.e. a multidimensional array, initialised with all zero's
list = [[0 for column in range(column_size)] for row in range(row_size)]
print(list)
# Here is the matrix, i.e. a multidimensional array, initialised with all zero's
for row in range(row_size):
    for column in range(column_size):
        list[row][column] = row*column
print(list)

# ###############################
# DAY08
# ###############################
# List and mechanisms to print it
pets = ["dog", "cat", "bird", "rabbit", "fish"]

print(pets[0])
print(pets[1])
print(pets[2])
print(pets[3])
print(pets[4],"\n")

for varloop in pets:
    print(varloop)

# Basic example of a while loop

random_variable = 20

while random_variable < 25:
    print("My variable is " + str(random_variable) + " and is < 25")
    random_variable += 1
print("My variable is over the limit!")

# Basic example of for loop that print on screen
# the numbers in a range that have 0 as result of MOD operation for both 5 and 7
for i in range(1500, 1530):
    if i%7==0 and i%5==0:
        print(i)

# Guess a number between 1 and 10
import random
# line below is eqivalent to declare 2 variables
# target_number = random.randint(1,10)
# guess_number = 0
target_number, guess_number = random.randint(1,10), 0
while target_number != guess_number:
    guess_number = int(input("Try to guess a number between 1 and 10: "))
    if target_number != guess_number:
        print("Nope!\n")
print("Well done!")

# Create e triangle of asterisks
count = 0
for for_var in range(7):
    count += 1
    print("*" * count)
for for_var in range(6):
    count -= 1
    print("*" * count)





# ###############################
# DAY09
# ###############################

# Create an array of 5 integers
from array import *
my_array = array("i", [1,3,5,7,9])

for i in my_array:
    print(i)

print("Access a few items individually, e.g. first element and second element\n")
print(my_array[0])
print(my_array[1])

# Append an item to the end of an existing array
print("Append an item to the end of an existing array")
print("Starting array: ", my_array)
my_array.append(11)
print("New array: ", my_array)

# Print in reverse order and normally
print("Print in reverse order and normally")
print(my_array[::-1])
print(my_array)

# Add an element at position 2
print("Add an element at index position 2 (counting from 0)")
my_array.insert(2,21)
print(my_array)

# Remove element at position 1
print("Remove an element at index position 1 (counting from 0)")
my_array.pop(1)
print(my_array)

# Remove first occurrence of a specific element
my_new_array = array("i", [1,19,5,19,7,19,9,11])
print("Remove first occurrence of a specific element, e.g. 19")
print(my_new_array)
my_new_array.remove(19)
print(my_new_array)

# Convert an array into a list
print("Convert an array into a list")
print("My array: ")
print(my_array)
print("Type of array: ")
print(type(my_array))
my_list = my_array.tolist()
print("My list: ")
print(my_list)
print("Type of list: ")
print(type(my_list))


###############################
# DAY10
###############################

# Reverse an input string
x = input("Type the input you'd like to be reversed: ")
print(x)
b = "".join(x)
print(b)
c = "".join(reversed(x))
print(c)
# Alternative method, from beginning of the string, i.e. ":" to the end of the string, i.e. ":"
# print and go backward i.e. "-1". It will give you the same result
print(x[::-1])

# Creating sub-list of een and odd numbers, given a list in input
# Counting odd and even numbers

def createListOdd(input_list):
    my_odd = []
    # print(my_odd)

    for x in input_list:
        if int(x)%2 == 1:
            my_odd.append(x)
    return my_odd


def totalOddInList(input_list):
    total = 0

    for x in input_list:
        if int(x)%2 == 1:
            total += 1
    return total


def createListEven(input_list):
    my_even = []
    # print(my_even)

    for x in input_list:
        if int(x)%2 == 0:
            my_even.append(x)
    return my_even


def totalEvenInList(input_list):
    total = 0

    for x in input_list:
        if int(x) % 2 == 0:
            total += 1
    return total

print("Please type list integer numbers comma separated: ")
values= input()
my_list = values.split(",")
print("You have chosen this list: ")
print(my_list)
print("The lists of even numbers is " + str(createListEven(my_list)))
print("The lists of odd numbers is " + str(createListOdd(my_list)))
print("Total even number is " + str(totalEvenInList(my_list)))
print("Total odd number is " + str(totalOddInList(my_list)))


# print the list below aling with the type
my_data = [1452, 12.3, 1+2j, True, "Pastrelli", (0,2), [3,56], {"class":"V", "section":"A"}]
for x in my_data:
    print("Type of ", x, " is ", type(x))

# create fibonacci sequence
def fibonacci(rng):
    x, y = 0, 1
    my_fib = []
    for i in range(rng):
        new_num = x+y
        x = y
        y = new_num
        my_fib.append(new_num)
    return my_fib


print("I will run a fibonacci sequence up to the number of entries you'll enter \n")
print("(e.g. type 3 and you'll have a sequence of 3): ")
print(fibonacci(int(input())))

# given a number, it will return the number divisible by two additional provided input numbers
def divisors(big_num, a, b):
    divisors_list = []
    for i in range(int(big_num)):
        if (i != 0) and (i % int(a)) == 0 and (i % int(b)) == 0:
            divisors_list.append(i)
    return divisors_list


print("Given a number, it will return the divisors divisible by two additional provided input numbers.\n")
print("Please input the number: ")
input_num = input()
print("Please input the first divisor: ")
div01 = input()
print("please input the second divisor: ")
div02 = input()
print("List is ", divisors(input_num, div01, div02))
print("List is " + str(divisors(input_num, div01, div02)))
