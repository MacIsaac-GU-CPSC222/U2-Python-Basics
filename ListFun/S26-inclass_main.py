import random

# a list is a sequence of items
# 1D lists like a single row or a single column in Excel
# declare a list using [ ] and a comma separated list of values

#           -4  -3  -2  -1
#            0  1   2   3
list_ints = [2, 100, 5, -10]
print(list_ints[0])
print(list_ints[-4])

# there are unique indexes for each element in the list
# 0-based... meaning the first element is at 0, and the last element is at n - 1
# where n is the number of elements in the list
# use len() to find out how many elements are in a list
list_len = len(list_ints)
print(list_len)
# print out the last element in the list.... suppose we don't know at compile time exactly how many elements are in the list
print(list_ints[len(list_ints)-1])
# types can be mixed in a list
list_nums = [10, -2, -1.7, 12.6]
# lists are mutable (they can be changed)
print(type(list_nums))
list_nums[2] = "listfun"

# use .append() to add an element to the end of a list
list_nums.append("hello")
print(list_nums)

# we can declare an empty list!
empty_list = []
for i in range(0,3):
    empty_list.append(i)
print(empty_list)
# we can have lists of lists (2D or ND)
matrix = [[1,2,3], 7, [8,9]]
print(len(matrix))
print(len(matrix[0]))
matrix[0][1] = 10
print(matrix)

dim_2 = [
            ["00", "01", "02"], # index 0
            ["10", "11", "12"], # index 1
            ["20", "21", "22"]  # index 2
        ]
dim_2[0].append("03")
print(dim_2[0][1])


# looping through list items
candies = ["twix", "reeses", "oreos", "snickers"]

# for item in list
# for candy in candies:
#     print(candy, end = " ") 

# while loop with indexing
# for loop with indexing
for ind in range(len(candies)):
    print(candies[ind], end = " ") 




# common list operators
# list concatenation... adding 2 lists together
print()
candies += ["starbursts", "fruit-by-the-foot"]
print(candies)
# list slicing
# list_name[start : end : step]
print(candies[:4:3])

# : is the slice operator. 
# start index is inclusive
# end index is exclusive
# if you leave an argument empty, it will automatically fill in with:
# - start (first element of the list - inclusive)
# - end (last element of the list - inclusive)
# - step (1)

# if you ever need a copy of a list, you can simply use the : with no start or end indices
list_nums = [0,1,2,3,4,5,6,7,8,9]

# TASK:
# Create a list with 10 numbers, then use slicing to print the following
# First 3 elements
print(list_nums[:3])
# Last 3 elements
print(list_nums[-3:])
# Every other element
print(list_nums[1::2])

# list methods
# remove
candies.remove("twix")


# pop(index) for position based removal

candy = candies.pop(0)
print(candy)
print(candies)

# append 
# extend (for appending items in another list)

# sort
list_ints = [5,10,-2, 7]
# list_ints.sort(reverse=True)
print(list_ints)

# built in list functions
# len
# sum
list_sum = sum(list_ints)
print(list_sum)
# sorted
list_ints_sort = sorted(list_ints)
print(list_ints)
print(list_ints_sort)
# max, min
print(min(list_ints))
print(max(list_ints))


# how to make a list from a string
word = "hello"
list_of_strings2 = list(word)
print(list_of_strings2)
# split is a string method
# default delimiter is
# any whitespace
comma_separated_word = "co,m,pute,r"
list_of_strings3 = comma_separated_word.split(",") 

print(list_of_strings3)


# LIST ALIASING
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
# list2 is a different list object from list1 (though they have the same values)
list1[0] = 10
print(list1, list2)
list3 = list1
# list3 is an "alias" for the same object that list1 refers to
list3[0] = 100
print(list1, list2, list3)


# python is pass by object reference
# functions with a reference to an object passed in
# can modify the object
# pass by object reference
def add_one(nums_list):
    nums_list = [1,2]
    # for i in range(len(nums_list)):
    #     nums_list[i] += 1

add_one(list1)
print(list1)

# add_one_to_each_element(list1) 
# # nums_list will be an alias for list1's object
# print("after call:", list1, list2, list3)


# to make a copy of a 1D list: use the list copy() method
list4 = list1.copy() # "shallow" copy
list1[0] = 10000
print(list1, list2, list3, list4)


# other "hacks" to make a shallow copy
list5 = list1 + []
list6 = list1[:]
list5[0] = 298
list6[0] = 299
print(list1,list2,list3,list4,list5,list6)


# a few more words about strings
# strings are immutable (cannot be changed)
# they support 0-based indexing and slicing
# they have methods, like split() and join()
# strip()

word = "                 a\tb\n\n  basketball\n   \nend\n"

print(word)
print("================")
print(repr(word))
print("================")

word = word.strip()
print(word)
print("================")
print(repr(word))
# print("================")

print(len(word))
# # find()
print(word.find("et"))
print(word.find("k"))
print(word.find("z"))


# List comprehension
# newlist = [expression for item in iterable if condition == True]
# TASK 1:
# What will be in newlist?
fruits = ['apple', 'banana', 'cherries']
newlist = [fruit for fruit in fruits if fruit == 'banana']
newlist = [len(fruit) for fruit in fruits if len(fruit)>5 ]
print(newlist)
# TASK 2:
numbers = [3, 7, 10, 15, 22, 30, 41, 50]
# Using a single list comprehension, create a new list called even_squares that contains the square of each even number in numbers.
even_squares = [number * number for number in numbers if number % 2 == 0]
print(even_squares)