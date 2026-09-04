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

print(temperatures[0])
print(temperatures[1])


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

print(len(temperatures))

# a list of length 5 has indexes:
# 0, 1, 2, 4, 5

# the last valid index is:
# len(list) - 1

print(temperatures[len(temperatures) - 1])


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

temperatures[1] = 85

print(temperatures)


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

temperatures = []

# append() adds one value to the end
# this is a method. A method is a special type of function that applies to a specific object
# in this case, the object is the list "temperatures" and the method is "append"
# you can recognize that it is a method based on the . notation
# ie <object>.<method>(<args>)
temperatures.append(72)
temperatures.append(81)

print(temperatures)


# this solves the problem from last class:
# we can collect input AND keep every value

temperatures = []

for day in range(5):
    temperature = float(input("Enter temperature: "))
    temperatures.append(temperature)

print(temperatures)


###############################
# LOOPING THROUGH LIST VALUES
###############################

temperatures = [72, 81, 77, 85, 69]

# when we need each VALUE,
# loop directly through the list

for temperature in temperatures:
    print(temperature)


# TRACE:
# What value does temperature have
# during each iteration?


###############################
# ACCUMULATION WITH LISTS
###############################

# this is the same accumulation pattern
# we used last class

total_temperature = 0

for temperature in temperatures:
    total_temperature += temperature

average_temperature = total_temperature / len(temperatures)

print(average_temperature)


# TASK:
# Count how many temperatures are at least 80

hot_days = 0

for temperature in temperatures:
    if temperature >= 80:
        hot_days += 1

print(hot_days)


###############################
# VALUES VS INDEXES
###############################

# usually, if we just need the values:
# loop directly through the list

for temperature in temperatures:
    print(temperature)


# sometimes we actually need the POSITION

for i in range(len(temperatures)):
    print(i, temperatures[i])


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

temperatures = [72, -5, 81, -2, 77]

for i in range(len(temperatures)):
    if temperatures[i] < 0:
        temperatures[i] = 0

print(temperatures)


###############################
# FUNCTIONS WITH LISTS
###############################

# a function can accept an entire list

def average(values):
    total = 0

    for value in values:
        total += value

    return total / len(values)


temperatures = [72, 81, 77, 85, 69]

print(average(temperatures))


# TASK:
# Write a function that counts
# how many temperatures are at least 80

def count_hot_days(values):
    count = 0

    for value in values:
        if value >= 80:
            count += 1

    return count


print(count_hot_days(temperatures))


###############################
# USEFUL BUILT-IN FUNCTIONS
###############################

# Python already provides some common
# operations for numeric lists

print(sum(temperatures))
print(min(temperatures))
print(max(temperatures))


###############################
# MODIFYING LISTS IN FUNCTIONS
###############################

# lists are mutable
# if a function changes the list itself,
# the original list is changed too

def replace_negatives(values):
    for i in range(len(values)):
        if values[i] < 0:
            values[i] = 0


temperatures = [72, -5, 81, -2, 77]

replace_negatives(temperatures)

print(temperatures)


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

list1 = [1, 2, 3]
list2 = list1

list2[0] = 100

print(list1)
print(list2)


# list1 and list2 refer to the same list


# use .copy() when you want a separate 1D list

list1 = [1, 2, 3]
list2 = list1.copy()

list2[0] = 100

print(list1)
print(list2)


# PREDICT:
#
# What is different about this example?
#
# What prints for list1?
# What prints for list2?


# TASK:
# Make a copy of temperatures called cleaned_temperatures.
#
# Change every negative value in cleaned_temperatures to 0.
#
# The original temperatures list should stay unchanged.

temperatures = [72, -5, 81, -2, 77]

cleaned_temperatures = temperatures.copy()

for i in range(len(cleaned_temperatures)):
    if cleaned_temperatures[i] < 0:
        cleaned_temperatures[i] = 0

print(temperatures)
print(cleaned_temperatures)

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

print(weather_data)


# one index gives us an entire row

print(weather_data[1])


# two indexes give us one value
#
# first index  -> row
# second index -> position within that row

print(weather_data[1][0])
print(weather_data[1][1])


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

for row in weather_data:
    print(row)


# during each iteration,
# row is one of the inner lists

for row in weather_data:
    city = row[0]
    temperature = row[1]

    print(city, temperature)


# TASK:
# Print only the city names


###############################
# ANALYZING A COLUMN
###############################

# conceptually, index 1 represents
# the temperature column

total_temperature = 0

for row in weather_data:
    total_temperature += row[1]

average_temperature = total_temperature / len(weather_data)

print(average_temperature)


# TASK:
# Find the highest temperature in the table


###############################
# MODIFYING VALUES IN A 2D LIST
###############################

# we can modify one value using
# a row index and a column index

weather_data[1][1] = 70

print(weather_data)


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

weather_data = []

row = ["Spokane", 72, 0.0]
weather_data.append(row)

row = ["Seattle", 68, 0.2]
weather_data.append(row)

print(weather_data)


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