import random

# a list is a sequence of items
# 1D lists like a single row or a single column in Excel
# declare a list using [ ] and a comma separated list of values

#           -4  -3  -2  -1
#            0  1   2   3



# there are unique indexes for each element in the list
# 0-based... meaning the first element is at 0, and the last element is at n - 1
# where n is the number of elements in the list



# types can be mixed in a list



# lists are mutable (they can be changed)




# use len() to find out how many elements are in a list



# use .append() to add an element to the end of a list



# print out the last element in the list.... suppose we don't know at compile time exactly how many elements are in the list



# we can declare an empty list!



# we can have lists of lists (2D or ND)



# looping through list items
candies = ["twix", "reeses", "oreos", "snickers"]
# print(candies)


# for item in list



# while loop with indexing



# for loop with indexing



# common list operators
# list concatenation... adding 2 lists together



# list repetition... repeating elements in a list
bag_o_candies = 5 * ["twix", "snickers"]
# print(f" bag o candies{bag_o_candies}")


# list slicing
# list_name[start : end : step]


# : is the slice operator. start index is inclusive
# end index is exclusive
# if you leave an argument empty, it will automatically fill in with:start (first element of the list), end (last element of the list), step (1)
# if you ever need a copy of a list, you can simply use the : with no start or end indices


# TASK:
# Create a list with 10 numbers, then use slicing to print the following
# First 3 elements
# Last 3 elements
# Every other element


# list methods
# remove



# pop(index) for position based removal


# append 



# extend (for appending items in another list)



# += list concatenate and assign



# built in list functions
# len

# sum

# sort



# lists and strings
# creating a string from a list of strings
# using the string join method

# list_of_strings = ["co", "m", "pute", "r"]
# word = ".".join(list_of_strings)
# print(word)




# how to make a list from a string

# list_of_strings2 = list(word)
# print(list_of_strings2)




# split is a string method
# default delimiter is
# any whitespace

# comma_separated_word = "co,m,pute,r"
# list_of_strings3 = comma_separated_word.split(",") 
# print(list_of_strings3)

# LIST ALIASING

# list1 = [1, 2, 3, 4]
# list2 = [1, 2, 3, 4]
# list2 is a different list object from list1 (though they have the same values)

# list1[0] = 10
# print(list1, list2)
# list3 = list1
# list3 is an "alias" for the same object that list1 refers to
# list3[0] = 100
# print(list1, list2, list3)


# pass by object reference
# def add_one_to_each_element(nums_list):
#     nums_list = []
#     for i in range(len(nums_list)):
#         nums_list[i] += 1


# add_one_to_each_element(list1) 
# # nums_list will be an alias for list1's object
# print("after call:", list1, list2, list3)


# to make a copy of a 1D list: use the list copy() method
# list4 = list1.copy() # "shallow" copy
# list1[0] = 10000
# print(list1, list2, list3, list4)


# python is pass by object reference
# functions with a reference to an object passed in
# can modify the object

# a few more words about strings
# strings are immutable (cannot be changed)
# they support 0-based indexing and slicing
# they have methods, like split() and join()
# strip()

# word = "                 a\tb\n\n  basketball\n   \nend"
# print(word)
# print(repr(word))
# word = word.strip()
# print(word)
# print(repr(word))

# # find()
# print(word.find("et"))
# print(word.find("k"))
# print(word.find("z"))


# List comprehension
# newlist = [expression for item in iterable if condition == True]

# TASK 1:
# What will be in newlist?
# fruits = ['apple', 'banana', 'cherry']
# newlist = [x for x in fruits if x == 'banana']

# TASK 2:
# numbers = [3, 7, 10, 15, 22, 30, 41, 50]
# Using a single list comprehension, create a new list called even_squares that contains the square of each even number in numbers.

