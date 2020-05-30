# # String is defined by str and is Unicode
# # Bytes use b"word" syntax and you convert (ancode/decode) between bytes and strings
# norsk = "Jeg begynte"
# print(norsk)
# data = norsk.encode("utf8")
# print(data)
# norwegian = data.decode("utf8")
# print(norwegian)

# # Lists are sequences of objects, and are mutable
# a = [1, 3, 5]
# b = ["apple", "orange", "pear"]
# c = ["apple", 9, "pear"]
# d = []
# d.append(3.14)
# print(a[1])
# print(b[2])
# print(d)
# e = ["aba",
#       "ulu",
#       "oio",]
# print(e)
#
# # dictionary maps key to values
# f = {"alice": "234", "bob": "198"}
# print(f)
# print(f["alice"])
# f["alice"] = "999"
# print(f)
# f["tim"] = "777"
# print(f)
# g = {}
# print(g)
# g["alfa"] = "12345"
# print(g)


# Compare the following 2 blocks of code
# # BLOCK 1
# from urllib.request import urlopen
#
# story = urlopen("http://sixty-north.com/c/t.txt")
# story_words = []
# for line in story:
#     # print(line)
#     # data = line.decode("utf8")
#     # print(data)
#     line_words = line.split()
#     # print(line_words)
#     # data2 = []
#     # for i in line_words:
#     #       data2.append(i.decode("utf8"))
#     # print(data2, "\n")
#     for wrd in line_words:
#         story_words.append(wrd)
#
# story.close()
# print(story_words)

# BLOCK 2
from urllib.request import urlopen

# # story is an object class that includes the url
# story = urlopen("http://sixty-north.com/c/t.txt")
# # print(type(story))
# # print(story)
# story_words = []
# for line in story:
#     # print(line)  # this is a byte encoding
#     # data = line.decode("utf8")
#     # print(data)  # this is the same byte decoded into a string
#     line_words = line.decode("utf8").split()
#     print(line_words)  # this is an array of the elements of the same byte decoded as a string
#     data2 = []
#     # these 3 lines below become redundant, because the command above has already done it
#     # for i in line_words:
#     #       data2.append(i)
#     # print(data2, "\n")
#     for wrd in line_words:
#         story_words.append(wrd)
#
# story.close()
# for w in story_words:
#       print(w)

#########
# This section below does the same as above, but it will do it in a function (note: I left the "import" above)
#########

def fetch_words(url_i):
      story = urlopen(url_i)
      story_words = []
      for line in story:
            line_words = line.decode("utf8").split()
            for wrd in line_words:
                  story_words.append(wrd)

      story.close()

      for w in story_words:
            print(w)

if __name__ == "__main__":
      fetch_words("http://sixty-north.com/c/t.txt")

## the url to be called is: "http://sixty-north.com/c/t.txt"
#print("Provide the url you want to fetch words from: ")
#input_url = input()
#fetch_words(input_url)