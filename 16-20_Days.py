# ################################
# # DAY16
# ################################
#
# import time
# import webbrowser
#
# time_breaks = 3
# count = 0
#
# print("This time started at " + time.ctime())
#
# while count < time_breaks:
#     time.sleep(10)  # 10 secs of program pausing
#     webbrowser.open("https://www.ilpost.it/2020/04/12/amazon-prime-video-50-film-migliori/")
#     count = count + 1
#
#
# ################################
# # DAY17
# ################################
#
#
# import time
# import random
#
#
# def displayIntro():
#     print("You are in a land full of dragons")
#     time.sleep(1)
#     print("""In front of you there are 2 caves:
#     one with a friendly dragon,
#     one with a angry adn hungry one.""", "\n")
#     time.sleep(1)
#
#
# def chooseCave():
#     print("Choose a cave.\n")
#     cave = ""
#     while cave != "1" and cave != "2":
#         print("What cave do you choose (1 or 2)?")
#         cave = input()
#     return cave
#         # the 'return' cave above makes the lines below useless..
#         # if cave = 1:
#         #     return cave
#         # elif cave = 2:
#         #     return cave
#
# def checkCave(chosencave):
#     print("You approach the cave..")
#     time.sleep(2)
#     print(".. it is large and spooky.")
#     time.sleep(2)
#     print("A dragon appears in front of you and..")
#     time.sleep(2)
#
#     friendlycave = random.randint(1, 2)
#
#     if int(chosencave) == friendlycave:
#         print("..gives you the treasure!")
#     else:
#         print("..eats you in a single bite!")
#
#
# play_again = "yes"
#
# while play_again == "yes" or play_again == "y":
#     displayIntro()
#     cave = chooseCave()
#     checkCave(cave)
#     print("Do you want to play again (yes or no)?")
#     play_again = input()
#
# #################################
# # DAY18
# #################################
#
# print("list and list components example")
# x = "blue red green".split(" ")
# print(x)
# print(type(x))
#
# a, b, c = x
# print(a)
# print(b)
# print(c)
#
# words = "This is a random sentence".split(" ")
# print(words)
# print(type(words))
#
# print("split input example")
# print(input("Give me a sentence: ").split(" "))
#
# print("Dictionary example")
# dict01 = {1: "value", "2": "tree", "key": "ran"}
# print("this is the dictionary:")
# print(dict01)
# print("\n")
# print("This is the length of the dictionary " + str(len(dict01)) + "\n")
# print("print keys:")
# print(list(dict01.keys()))
# print("\n")
# print("print values:")
# print(list(dict01.values()))
# print("\n")
# for i in dict01:
#     print("This print the key ", i)
#     print("\n")
#     print("This print the value ", dict01[i])
#     print("\n")
#
# print("I now create 2 dict with same values in different orders")
# print("They are: ")
# dict02 = {1: "value", "2": "tree", "key": "ran"}
# dict03 = {"key": "ran", 1: "value", "2": "tree"}
# print(dict02)
# print(dict03)
# print("are they the same? ", dict02 == dict03)
#
#
# print("Interesting.. I wonder if the same applies to lists")
# print("They are: ")
# listA = ["abba", "strokes", "pulp"]
# listB = ["pulp", "abba", "strokes"]
# print(listA)
# print(listB)
# print("are they the same? ", listA == listB)
#
# #################################
# # DAY19
# #################################
# # This was just a summary of the content of the lessons, no coding

#################################
# DAY20
#################################

def sumNumbers(num_list):
    total = 0
    for num in num_list:
        total = total + float(num)
    return total


def multNumbers(num_list):
    total = 1
    for num in num_list:
        total = total * float(num)
    return total


def highestNumber(num_list):
    highest = 0
    for num in num_list:
        if float(num) > highest:
            highest = float(num)
    return highest


print("Type a few numbers, comma separated, and I will return the sum and the mutiplication: ")
input_numbers = input()
list01 = [x for x in input_numbers.split(",")]

print("Sum is " + str(sumNumbers(list01)))
print("Multiplication is " + str(multNumbers(list01)))
print("Highest number is " + str(highestNumber(list01)))


def reverseString(inp):
    reversed = ""
    count = len(inp)
    while count > 0:
        reversed = reversed + inp[count-1]
        count = count - 1
    return reversed


print("Type a string, to have it reversed: ")
chosen_string = input()

print("Reversed string is " + reverseString(chosen_string))