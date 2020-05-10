import pandas as pd
from matplotlib import pyplot as plt

# ############################################
# # pandas 01 - cupofcode youtube
# ############################################
#
# # Reading a file, which is the one that will be processed
# dataframe01 = pd.read_csv("gapminder.tsv", sep="\t")
# # Default separator for "read_csv" would be comma, i.e. "," which is why
# # a tab separator, i.e. "\t" is passed as parameter
#
# # print first 7 rows
# print(dataframe01.head(7), "\n")
#
# # print last 6 rows
# print(dataframe01.tail(6), "\n")
#
# # it shows shape of the table, i.e. now many rows and columns
# # side note: "shape" is an attribute, not a function
# print(dataframe01.shape, "\n")
#
# # it shows columns and type
# print(dataframe01.columns, "\n")
#
# # it shows the type of each column
# print(dataframe01.dtypes, "\n")
#
#
# # "info()" provides a few details about the data (column names, dtype, if anny null, memory usage, ..
# print(dataframe01.info(), "\n")
#
# # get specific columns, e.g. the firsts 7 rows of the "continent" column
# continent_df = dataframe01["continent"]
# print(continent_df.head(7))
#
# # get specific columns, e.g. the last 4 rows of the "continent" column
# continent_df_dotnotation = dataframe01.continent
# print(continent_df_dotnotation.tail(4))
#
# # get a subset of columns
# my_subset01 = dataframe01[["country", "continent", "year"]]
# print(my_subset01.head(3), "\n")
# print(my_subset01.tail(3), "\n")
#
# # calling a column by position, rather than name, i.e. 451st
# my_subset02 = dataframe01.iloc[451]  # iloc means "integer location"
# # get the first 4 value of such row
# print(my_subset02.head(4), "\n")
#
# # get a specific value, providing row and column index
# my_subset03 = dataframe01.iloc[0, 2]  # location 0, i.e. first line and 2 i.e. 3rd column
# print(my_subset03, "\n")
#
# my_subset04 = dataframe01.iloc[0, -1]  # location 0, i.e. first line and -1 i.e. last column
# print(my_subset04, "\n")
#
# # get specific range, by index location
# print(dataframe01.iloc[1204:1214], "\n")
#
# # get specific range, i.e. first 16
# small_range = list(range(16))
# my_subset05 = dataframe01.iloc[small_range]
# print(my_subset05, "\n")
#
# # extracting just column indexed as 3 (i.e. the lifeExp), for the given range
# print(dataframe01.iloc[204:214, 3], "\n")
#
#
# # loc is based on label, not integer location
# # in pandas labels are the index
# # not that you can use iloc[-1] but you can't use loc[-1] cause -1 is not a valid label!
# print("Following commands are based on 'loc'")
# print(dataframe01.loc[13], "\n")
# print(dataframe01.loc[123:124], "\n")
# print(dataframe01.loc[[0, 9, 99]], "\n")
#
# # See below: same data, printed in different ways
# print("Different commands, e.g. iloc[-1] and tail(1), same output in different format: ", "\n")
# print(dataframe01.iloc[-1], "\n")
# print(dataframe01.tail(1), "\n")
# print("and this is because they are different data types: ", "\n")
# print(type(dataframe01.iloc[-1]), "\n")
# print(type(dataframe01.tail(1)), "\n")
#
# ############################################
# # pandas 02 - cupofcode youtube
# ############################################
#
# # This section calculates the average life expectancy for each year and other operations on the data
#
# group_year_dframe01 = dataframe01.groupby("year")
# group_year_lifeExp_dframe01 = group_year_dframe01["lifeExp"]
# print(group_year_dframe01, "\n")  # this prints the object that we created, i.e. its memory location
# print(group_year_lifeExp_dframe01, "\n")  # this prints the object that we created, i.e. its memory location
#
# # a vector of numbers will allow mathematical operation
# # so I can apply the "mean()" command
# print(group_year_lifeExp_dframe01.mean(), "\n")
#
# # and this does it in a single command
# # the command groups the data by "year" and then apply the "mean()" to the "lifeExp" paramenter
# print(dataframe01.groupby("year")["lifeExp"].mean(), "\n")
#
#
# print("Population grouped by year: \n")
# print(dataframe01.groupby("year")["pop"].mean())
# print("GDP grouped by year: \n")
# print(dataframe01.groupby("year")["gdpPercap"].mean())
#
# # this does the same, but groups by year and sub-groups by continent and then
# # it does the mean for lifeExp and GDP
# print(dataframe01.groupby(["year", "continent"])[["lifeExp", "gdpPercap"]].mean(), "\n")
#
# # nunique() function returns number of unique elements in the object
# print("Nunique frequency counts\n")
# print(dataframe01.groupby("continent")["country"].nunique(), "\n")
# print("doing the same, but now looking at occurrences of each value,")
# print("i.e. it hows the actual countried and how many times they appear\n")
# print(dataframe01.groupby("continent")["country"].value_counts(), "\n")
#
# group_year_dframe02 = dataframe01.groupby("year")
# group_year_lifeExp_dframe02 = group_year_dframe01["lifeExp"]
# mean_lifeExp_per_year = group_year_lifeExp_dframe02.mean()
# print(mean_lifeExp_per_year)
#
# # Y axis is life expectancy, and X axis is the year
# plt.plot(mean_lifeExp_per_year)
# plt.show()

############################################
# pandas 03 - cupofcode youtube
############################################

# pandas series is a 1-dimensional container, vector
s01 = pd.Series(["banana", 42])
print(s01, "\n")

# the row number is the index for the series, but they can be renamed
s02 = pd.Series(["Dad1", "Master of universe"], ["Person", "Who"])
print(s02, "\n")
# another way to do it is to pass key-value as a dictionary
s03 = pd.Series({"Person": "Dad2", "Who": "Master of universe"})
print(s03, "\n")

# create a dataframe, i.e. dictionary of a Series objects
science = pd.DataFrame({
    "Name": ["Albert Einstein", "Nikola Tesla"],
    "Job": ["Math", "Physicist"],
    "BornYear": ["1879", "1856"],
    "DeathYear": ["1955", "1943"],
    "Age": [76, 86]
})
print("This is the science series: ")
print(science, "\n")

# create a dataframe, i.e. dictionary of a Series objects
science2 = pd.DataFrame({
    "Name": ["Albert Einstein", "Nikola Tesla"],
    "Job": ["Math", "Physicist"],
    "BornYear": ["1879", "1856"],
    "DeathYear": ["1955", "1943"]},

    index = [76, 86],
    columns = ["Name", "Job", "BornYear", "DeathYear"])

print(science2, "\n")

print("Print just a row: ")
row_I_want = science2.loc[86]
print(type(row_I_want))
print(row_I_want, "\n")

print("Print index and values for just a row: ")
print(row_I_want.index)
print(row_I_want.values, "\n")
print("Print index and values for all dataframe: ")
print(science2.index)
print(science2.values, "\n")

print("Print keys for them all: ")
print(row_I_want.keys())
print(science2.keys())
print(science.keys(), "\n")

print("Print using 'index[1]' which is the second (because it is counting from '0'): ")
print(row_I_want.index[1])
print(science2.keys()[1])