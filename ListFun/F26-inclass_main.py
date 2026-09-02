import random

# a list is a sequence of items
# 1D lists like a single row or a single column in Excel
# declare a list using [ ] and a comma separated list of values

#           -4  -3  -2  -1
#            0  1   2   3

# there are unique indexes for each element in the list
# 0-based... meaning the first element is at 0, and the last element is at n - 1
# where n is the number of elements in the list
# use len() to find out how many elements are in a list

# print out the last element in the list.... suppose we don't know at compile time exactly how many elements are in the list

# types can be mixed in a list


# lists are mutable (they can be changed)


# use .append() to add an element to the end of a list


# we can declare an empty list!


# we can have lists of lists (2D or ND)


# looping through list items



# while loop with indexing
# for loop with indexing




# common list operators
# list concatenation... adding 2 lists together



# list slicing
# list_name[start : end : step]

# : is the slice operator. 
# start index is inclusive
# end index is exclusive
# if you leave an argument empty, it will automatically fill in with:
# - start (first element of the list - inclusive)
# - end (last element of the list - inclusive)
# - step (1)

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

# sort


# built in list functions
# len
# sum


# sorted


# max, min



# how to make a list from a string


# split is a string method
# default delimiter is
# any whitespace




# LIST ALIASING


# list2 is a different list object from list1 (though they have the same values)


# list3 is an "alias" for the same object that list1 refers to



# python is pass by object reference
# functions with a reference to an object passed in
# can modify the object
# pass by object reference



# # nums_list will be an alias for list1's object


# to make a copy of a 1D list: use the list copy() method


# other "hacks" to make a shallow copy



# a few more words about strings
# strings are immutable (cannot be changed)
# they support 0-based indexing and slicing
# they have methods, like split() and join()
# strip()



# List comprehension
# [<expression> for <item> in <sequence> if  <condition>]
# newlist = [expression for item in iterable if condition == True]
# TASK 1:
# What will be in newlist_1? What will be in newlist_2?
fruits = ['apple', 'banana', 'cherries']
newlist_1 = [fruit for fruit in fruits if fruit == 'banana']

newlist_2 = [len(fruit) for fruit in fruits if len(fruit)>5 ]


# TASK 2:
# Using a single list comprehension, create a new list called even_squares that contains the square of each even number in numbers.
numbers = [3, 7, 10, 15, 22, 30, 41, 50]


"""
Participation:

Write a small program that asks the user to enter a sentence. Split it into a list of words and print the number of words, longest word, and shortest word.

Create at least 1 function to complete these tasks. 

"""