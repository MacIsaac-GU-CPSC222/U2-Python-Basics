# LISTS REVIEW
#
# Goal:
# Store multiple values so that we can use them again later.
#
# We will focus on:
# - creating lists
# - indexing
# - changing values
# - append()
# - looping through lists
# - accumulation and counting
# - lists and functions

###############################
# INDEXES AND VALUES
###############################

# every value in a list has an index
# Python indexes start at 0

# index:        0   1   2   3   4 
temperatures = [72, 81, 77, 54, 23]


# PREDICT:
# What does each expression produce?
#
# temperatures[4]
# temperatures[2]


# IMPORTANT:
# an index is a POSITION
# the value is what is stored at that position

# TASK:
# What is the index of 54?


###############################
# LEN()
###############################

# len() tells us how many values are in a list



# a list of length 5 has indexes:
# 0, 1, 2, 4, 5

# the last valid index is:
# len(list) - 1


# PREDICT:
values = [10, 20, 30, 40]

# What does this print?
# print(len(values))

# What does this print?
# print(values[len(values) - 2])


###############################
# LISTS ARE MUTABLE
###############################

# mutable means the list can be changed


# PREDICT:
values = [10, 20, 30]
values[1] = 99

# What prints?
# print(values)


# TASK:
# Change the first temperature to 75


###############################
# BUILDING A LIST
###############################

# lists can start empty


# append() adds one value to the end
# this is a method. A method is a special type of function that applies to a specific object
# in this case, the object is the list "temperatures" and the method is "append"
# you can recognize that it is a method based on the . notation
# ie <object>.<method>(<args>)

###############################
# LOOPING THROUGH LIST VALUES
###############################
# when we need each VALUE,
# loop directly through the list


# TRACE:
# What value does temperature have
# during each iteration?


###############################
# ACCUMULATION WITH LISTS
###############################

# calculating average of values in a list

# TASK:
# Count how many temperatures are at least 80


###############################
# VALUES VS INDEXES
###############################

# usually, if we just need the values:
# loop directly through the list

# sometimes we actually need the POSITION
# for example: you need the index to modify the value in the list

# DECIDE:
#
# Which loop style makes more sense?
#
# 1. Print every temperature
#
# 2. Print each temperature with its index
#
# 3. Calculate the total
#
# 4. Replace every negative temperature with 0


# TASK:
# Replace every negative value with 0
values = [100, -10, 23, 10, -5]


###############################
# FUNCTIONS WITH LISTS
###############################

# a function can accept an entire list



# TASK:
# Write a function that counts
# how many temperatures are at least 80


###############################
# USEFUL BUILT-IN FUNCTIONS
###############################

# Python already provides some common
# operations for numeric lists



###############################
# MODIFYING LISTS IN FUNCTIONS
###############################

# lists are mutable
# if a function changes the list itself,
# the original list is changed too



# PREDICT:
#
# What does this print?
#
# Why did temperatures change
# even though the function did not return anything?


###############################
# COPYING LISTS
###############################

# assignment does NOT make a new list


# list1 and list2 refer to the same list


# use .copy() when you want a separate 1D list



# PREDICT:
#
# What is different about this example?
list1 = [1,2,3]
list2 = list1
list2[0] *= 7
list3 = list1.copy()
list3[0] = 5

# print(list1)
# print(list2)
# print(list3)


# TASK:
# Make a copy of temperatures called cleaned_temperatures.
#
# Change every negative value in cleaned_temperatures to 0.
#
# The original temperatures list should stay unchanged.


###############################
# TASK: DAILY TEMPERATURE ANALYZER
###############################

# Write a program that:
#
# 1. creates an empty list
# 2. asks the user for 5 temperatures
# 3. stores each temperature using append()
# 4. prints all stored temperatures
# 5. calculates the average temperature
# 6. counts how many temperatures are at least 80
#
# Use at least one function.


###############################
# WORKING WITH 2D LISTS
###############################

# a 2D list is a list that contains other lists

# each inner list can represent one row of data

weather_data = [
    ["Spokane", 72, 0.0],
    ["Seattle", 68, 0.2],
    ["Portland", 75, 0.0]
]



# one index gives us an entire row




# two indexes give us one value
#
# first index  -> row
# second index -> position within that row


# PREDICT:
#
# What does each expression produce?
#
# weather_data[0]
#
# weather_data[2][0]
#
# weather_data[0][2]


###############################
# LOOPING THROUGH ROWS
###############################

# usually it is easiest to loop through
# the rows of a table directly


# during each iteration,
# row is one of the inner lists



# TASK:
# Print only the city names


###############################
# ANALYZING A COLUMN
###############################

# conceptually, index 1 represents
# the temperature column




# TASK:
# Find the highest temperature in the table


###############################
# MODIFYING VALUES IN A 2D LIST
###############################

# we can modify one value using
# a row index and a column index



# PREDICT:
#
# Which value changed?
#
# What does weather_data[1] contain now?


# TASK:
# Increase Portland's temperature by 5 degrees


###############################
# BUILDING A 2D LIST
###############################

# we can also build a table one row at a time


# TASK:
# Add a row for Portland:
#
# city: Portland
# temperature: 75
# precipitation: 0.0


###############################
# TABLE MENTAL MODEL
###############################

weather_data = [
    ["Spokane", 72, 0.0],
    ["Seattle", 68, 0.2],
    ["Portland", 75, 0.0]
]

# weather_data
# -> the entire table
#
# weather_data[1]
# -> one row
#
# weather_data[1][2]
# -> one value
#
# row[0]
# -> city value for a particular row
#
# row[1]
# -> temperature value for a particular row


# FINAL CHECK:
#
# 1. What does weather_data[2] produce?
#
# 2. What does weather_data[2][0] produce?
#
# 3. How would you print every city?
#
# 4. How would you calculate the average temperature?
#
# 5. How would you change Spokane's precipitation to 0.5?