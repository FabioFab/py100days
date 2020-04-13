# ###############################
# DAY11
# ###############################

# It creates a matrix of A x B size, where both A and B are given as input
input_size_matrix = input("Please enter 2 comma separated numbers to have an equal size matrix: ")
# I use the input numbers to create a list of 2 elements
size = [int(x) for x in input_size_matrix.split(",")]
row_size = size[0]
column_size = size[1]

print(size)
print(row_size)
print(column_size)

# Here is the matrix, i.e. a multidimensional array, initialised with all zero's
list = [[0 for column in range(column_size)] for row in range(row_size)]
print(list)
# Here is the matrix, i.e. a multidimensional array, initialised with row*column as the
# value of that specific position
for row in range(row_size):
    for column in range(column_size):
        list[row][column] = row*column
print(list)


def dividableBinaries(bin, num):
    divisors = []
    for i2 in bin:
        # The expression below int(i,2) translates into an integer the "input i" "base 2"
        if (int(i2, 2) % int(num)) == 0:
            divisors.append(i2)
    return divisors


print("This program will calculate what binaries, in the input list, are divisible for a given number")
print("Please type the binaries (e.g. 0101), comma separated: ")
input_binaries = input()
l01 = [x for x in input_binaries.split(",")]
l02 = input_binaries.split(",")
print("Please choose the number to be used as divisor (decimal please, e.g. 7: ")
n = input()

print("A few ways to print the input:\n")
print(input_binaries)
print(l01)
print(l02)
print(n, "\n")
print("This is the result, i.e. the binaries that can be divided by " + str(n) + ": \n")
print(dividableBinaries(l02, n))

# ###############################
# DAY12
# ###############################


# This programs accepts a string and counts number of digits and numbers of letters
def letterDigits(input_string):
    letters, digits = 0, 0
    for i3 in input_string:
        if i3.isalpha():
            letters = letters + 1
        elif i3.isdigit():
            digits = digits + 1
        else:
            pass
    return letters, digits


print("Please type any string or sequence of character, and I'll calculate digits and letters: ")
string = input()
results = letterDigits(string)
print("Numbers of letters are " + str(results[0]) + " and digits are " + str(results[1]))
# print(results)


# This program checks password strength and ensure there is not whitespace
import re


def passwordStrength(pwd):
    #  feedback = "" this is not needed
    if len(pwd) < 6:
        feedback = "Password too short, less than 6 characters"
    elif not re.search("[0-9]", pwd):
        feedback = "Password missing a number"
    elif not re.search("[a-z]", pwd):
        feedback = "Password missing letter"
    elif not re.search("[A-Z]", pwd):
        feedback = "Password missing a capital letter"
    elif re.search("[$#£!?]", pwd):
        feedback = "Password includes a whitespace. Not allowed"
    elif not re.search("\s", pwd):
        feedback = "Password missing a special character"
    else:
        feedback = "Password check successful"
    return feedback


print("Please type the password you'd like to validate: ")
input_pwd = input()

print("Here is the result:\n")
print(passwordStrength(input_pwd))


# find all numbers within X and Y here all digits are even
def allEvenDigits(low, top):
    list4 = []
    for i4 in range(low, top+1):
        s = str(i4)
        if i4 < 10:
            if (int(s[0]) % 2) == 0:
                list4.append(i4)
        elif i4 < 100:
            if ((int(s[0]) % 2) == 0) and ((int(s[1]) % 2) == 0):
                list4.append(i4)
        elif (i4 >= 100) and (i4 < 1000):
            if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
                list4.append(i4)
    return list4


print("This program finds all numbers within X and Y here all digits are even.")
print("Please type the range, i.e. the bottom and top numbers of the range, separated by comma: ")
input_numbers = input()
numbers = [x for x in input_numbers.split(",")]
lst = allEvenDigits(int(numbers[0]), int(numbers[1]))

if int(numbers[1]) < 1000:
    print("List of numbers in range with all even digits is", lst)
#    print("or, alternatively")
#    print("List of numbers in range with all even digits is". join(str(lst)))
    print("or, alternatively")
    incr = 1
    for i in lst:
        print(str(incr) + ". " + str(i))
        incr = incr + 1
else:
    print("Upper value must be <1000")


# ###############################
# DAY13
# ###############################


# make a grid and find out how to make symbols e.g. letter "S" and "X"
def letterS():
    target_letter = ""
    for row in range(0, 7):
        for col in range(0, 7):
            if (row == 0 or row == 3 or row == 6):  # and col>0 and col<7 is this needed?!
                target_letter = target_letter + "*"
            elif (row == 1 or row == 2) and (col == 0):
                target_letter = target_letter + "*"
            elif (row == 4 or row == 5) and (col == 6):
                target_letter = target_letter + "*"
            else:
                target_letter = target_letter + " "
        target_letter = target_letter + "\n"
    return target_letter


def letterX():
    target_letter = ""
    for row in range(0, 7):
        for col in range(0, 7):
            if (row == 0 or row == 6) and (col == 0 or col == 6):
                target_letter = target_letter + "*"
            elif (row == 1 or row == 5) and (col == 1 or col == 5):
                target_letter = target_letter + "*"
            elif (row == 2 or row == 4) and (col == 2 or col == 4):
                target_letter = target_letter + "*"
            elif (row == 3) and (col == 3):
                target_letter = target_letter + "*"
            else:
                target_letter = target_letter + " "
        target_letter = target_letter + "\n"
    return target_letter


print("Please input the letter you'd like to see represented, either 'S' or 'X': ")
lett = input()
if lett == "s":
    print("Representation of letter S:\n")
    print(letterS())

if lett == "x":
    print("Representation of letter X:\n")
    print(letterX())


# count dog years (dog year 0 to 2 = 10.5 each, and 4 year each after that

def dogAge(age):
    if int(age) < 0:
        print("Dog age must be a positive number")
        exit()
    elif int(age) == 1:
        return 10.5
    elif int(age) == 2:
        return 21
    else:
        unit = 4
        topping = 0
        for i5 in range(3, (int(age)+1)):
            topping = (topping + unit)
        return 21 + topping


print("Function will calculate dog age in god years. What's dog age in human years?")
years = input()
print("Dog age is " + str(dogAge(years)))


# vowel check

def letter(x):
    if x in ("a", "e", "i", "o", "u"):
        print("{} is a vowel".format(x))
    else:
        print("{} is a consonant".format(x))


print("Type a letter: ")
xx = input()
letter(xx)


# It returns number of days in a  month, zero if input is not a month name
def daysMonth(x):
    x = x.lower()
    if x in ("november", "april", "june", "september", "nov", "apr", "jun", "sep"):
        return 30
    elif x == "february" or "feb":
        return 28
    elif x in ("january", "march", "may", "july", "august", "october", "december", "jan", "mar", "jul", "aug", "oct", "dec"):
        return 31
    else:
        return 0


print("Choose a month: ")
x = input()
if daysMonth(x) == 0:
    print("Type a valid month please")
else:
    print(x + " has " + str(daysMonth(x)) + " days")


# ###############################
# DAY14
# ###############################

# Input month and day, it returns season


def season(strmonth, strday):
    # spring_months = ("march", "april", "may" "june", "mar", "apr", "jun")
    # summer_months = ("june", "july", "august" "september", "jun", "jul", "aug", "sep")
    # autumn_months = ("september", "october", "november", "december", "sep", "oct", "nov", "dec")
    full_spring_months = ("april", "may", "apr", "may")
    full_summer_months = ("july", "august", "jul", "aug")
    full_autumn_months = ("october", "november", "oct", "nov")
    full_winter_months = ("january", "february", "jan", "feb")
    mar = ("march", "mar")
    jun = ("june", "jun")
    sep = ("september", "sep")
    dec = ("december", "dec")
    feb = ("february", "feb")
    day = int(strday)
    month = strmonth.lower()
    if day >= 32 or day <= 0:
        return "err01"
    elif day >= 29 and month in feb:
        return "err02"
    elif (month in full_spring_months) or (day >= 21 and month in mar) or (day < 21 and month in jun):
        return "Spring"
    elif (month in full_summer_months) or (day >= 21 and month in jun) or (day < 21 and month in sep):
        return "Summer"
    elif (month in full_autumn_months) or (day >= 21 and month in sep) or (day < 21 and month in dec):
        return "Autumn"
    else:
        return "Winter"


print("Season detector based of the day entered as input.")
print("Type the name of the month: ")
chosen_month = input()
print("type the day of the month (numerical): ")
chosen_day = input()

result = season(chosen_month, chosen_day)
if result == "err01":
    print("Invalid day number")
elif result == "err02":
    print("Invalid day number for February")
else:
    print("Day " + chosen_day + " in " + chosen_month + " is in " + result)


# Identify the average and the middle number, given 3 values

def average(vv1,vv2,vv3):
    total = vv1 + vv2 + vv3
    ave = total / 3
    return ave

def middleNum(vv1,vv2,vv3):
    if (vv1 > vv2) and (vv2 > vv3):
        return vv2
    elif (vv1 > vv2) and (vv3 > vv2) and (vv1 > vv3):
        return vv3
    elif (vv1 < vv2) and (vv1 < vv3) and (vv2 > vv3):
        return vv3
    elif (vv1 < vv2) and (vv1 < vv3) and (vv2 < vv3):
        return vv2
    else:
        return vv1


print("Function calculates medium number and average, given 3 numbers.")
print("please provide value 1: ")
v1 = float(input())
print("please provide value 2: ")
v2 = float(input())
print("please provide value 3: ")
v3 = float(input())
print("Average is " + str(average(v1,v2,v3)))
print("Middle number is " + str(middleNum(v1,v2,v3)))



# Identify the average of n values

def average_n(input_list):
    total = 0
    for i in input_list:
        total = total + float(i)
    average = total / len(input_list)
    return average


print("Function calculates medium, given n numbers.")
list = []
stop = "cont"
while stop == "cont":
    print("please provide value (type 's' when completed): ")
    inp = input()
    if inp == "s":
        stop = inp
    if inp != "s":
        try:
            value = float(inp)
            list.append(value)
        except ValueError:
            print("Input not valid\n")
            stop = "s"

if len(list) > 0:
    print("Average is " + str(average_n(list)))
else:
    print("Empty list")


# Create e multiplication table
def mult_table(num1, mult2):
    list = []
    for i in range(1, int(mult2)+1):
        x = float(num1) * float(i)
        y = str(x)
        list.append(y)
    return list


print("Please provide the input number for the multiplication table: ")
num = input()
print("Please provide the upper limit of the table, e.g. 12: ")
upp = input()
print("Result is: \n")
incr = 1
for i in mult_table(num, upp):
    print(str(incr) + ". " + str(i))
    incr = incr + 1

# it prints a numeric value as many times as the value itself
for i in range(30):
    print(str(i) * i)