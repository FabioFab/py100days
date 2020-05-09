import pandas as pd
from matplotlib import pyplot as plt

dataframe01  = pd.read_csv("gapminder.tsv", sep="\t")
# Default separator for "read_csv" would be comma, i.e. "," which is why
# a tab separator, i.e. "\t" is passed as parameter

print(dataframe01.head(7), "\n")
# print first 7 rows

print(dataframe01.tail(6), "\n")
# print last 6 rows

print(dataframe01.shape, "\n")
# tuple = row x columns
# side note: "shape" is an attribute, not a function

print(dataframe01.columns, "\n")

print(dataframe01.dtypes, "\n")
# the panda object type is a python string

# "info()" provides a few details about the data
print(dataframe01.info(), "\n")

# get specific columns
continent_df = dataframe01["continent"]
print(continent_df.head(7))

continent_df_dotnotation = dataframe01.continent
print(continent_df_dotnotation.tail(4))

my_subset01 = dataframe01[["country", "continent", "year"]]
print(my_subset01.head(3), "\n")
print(my_subset01.tail(3), "\n")

# calling a column by position, rather than name
my_subset02 = dataframe01.iloc[451]  #iloc means integer location
print(my_subset02.head(3), "\n")

my_subset03 = dataframe01.iloc[0, 2]  # location 0, i.e. first line and 2 i.e. 3rd column
print(my_subset03, "\n")

my_subset04 = dataframe01.iloc[0, -1]  # location 0, i.e. first line and -1 i.e. last column
print(my_subset04, "\n")

print(dataframe01.iloc[1204:1214], "\n")

#
small_range = list(range(16))
my_subset05 = dataframe01.iloc[small_range]
print(my_subset05, "\n")

# extracting just columned indexed as 3
print(dataframe01.iloc[204:214, 3], "\n")


# loc is based on label, not integer location
# in pandas labels are the index
# not that you can use iloc[-1] but you can't use loc[-1] cause -1 is not a valid label!
print(dataframe01.loc[13], "\n")
print(dataframe01.loc[123:124], "\n")
print(dataframe01.loc[[0, 9, 99]], "\n")

# See below: same data, printed in different ways
print(dataframe01.iloc[-1])
print(dataframe01.tail(1))
# and this is because they are different data types
print(type(dataframe01.iloc[-1]))
print(type(dataframe01.tail(1)))

