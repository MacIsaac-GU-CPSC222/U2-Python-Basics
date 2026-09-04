# PYTHON BASICS REVIEW
#
# Goal:
# Review the Python ideas we will use constantly when working with data.
#
# Today we will focus on:
# - variables and assignment
# - types and expressions
# - user input
# - Boolean expressions
# - conditionals
# - for loops and range()
# - accumulation and counting
# - functions
# - parameters, arguments, and return values
#
# We will work with lists and larger collections of data next.


###############################
# QUICK PYTHON BASICS REFRESHER
###############################

# variables store values
# common types: int, float, str, bool




# = is assignment
# Python evaluates the RIGHT side first,
# then stores the result on the LEFT




# common numeric operators:
# /  floating-point division
# // floor division
# %  remainder
# ** exponentiation

# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(2 ** 3)


# input() always returns a string
# convert the result when you need a number

# temperature = float(input("Enter the temperature: "))
# print(temperature)


# f-strings can format output



# PREDICT:
# without running the code, determine the final value of rainfall

# rainfall = 1.0
# rainfall += 0.5
# rainfall *= 2
# rainfall -= 1

# print(rainfall)


###############################
# BOOLEAN EXPRESSIONS + CONDITIONALS
###############################

# comparison expressions evaluate to True or False


# common comparison operators:
# >   greater than
# <   less than
# >=  greater than or equal to
# <=  less than or equal to
# ==  equal to
# !=  not equal to

# IMPORTANT:
# =  means assignment
# == means comparison


# if statements use Boolean expressions
# to decide whether code should run


# use else when there are two possibilities


# use elif when there are several possibilities



# conditions can also be combined:
# and -> both conditions must be True
# or  -> at least one condition must be True
# not -> reverses True/False

# PREDICT:
# what is printed?
"""
temperature = 80 
if temperature >= 70 and temperature < 90:
    print("comfortable") 
elif temperature < 50 or temperature > 100:
    print("extreme") 
else:
    print("moderate")
"""
# TASK:
# modify the code below so that it prints:
#
# "freezing" for temperatures <= 32
# "cold"     for temperatures from 33 through 49
# "mild"     for temperatures from 50 through 79
# "hot"      for temperatures >= 80

temperature = 55


###############################
# FOR LOOPS + RANGE() + TRACING
###############################

# for loops repeat code
# the loop variable receives one value from a sequence
# during each iteration


# range() creates a sequence of integers
#
# common forms:
# range(stop)                -> starts at 0, stops before stop
# range(start, stop)         -> starts at start, stops before stop
# range(start, stop, step)   -> same idea, but changes by step
#
# IMPORTANT:
# the stop value is NOT included

# examples:
# range(5)          -> 0, 1, 2, 3, 4
# range(2, 6)       -> 2, 3, 4, 5
# range(2, 10, 2)   -> 2, 4, 6, 8
# range(5, 0, -1)   -> 5, 4, 3, 2, 1


# PREDICT:
# write out the exact sequence produced by each range()

# range(4)

# range(1, 5)

# range(2, 8, 2)

# range(5, 0, -1)


# when tracing a loop, ask:
#
# 1. what values will the loop variable receive?
# 2. what happens during one iteration?
# 3. what changes before the next iteration?


# TRACE:
# complete the table before running the code
#
#                   day      temperature
# before loop        --          60
# iteration 1
# iteration 2
# iteration 3
# iteration 4
# iteration 5


###############################
# ACCUMULATION & COUNTING
###############################

# DEMO:
# often we want to combine information across
# many iterations of a loop

# an accumulator stores a running result


# another common pattern is counting how often
# something happens


# Predict outcome
# print("hot days:", hot_days)


# IMPORTANT:
# accumulation and counting have the same general pattern:
#
# 1. initialize something BEFORE the loop
# 2. update it INSIDE the loop
# 3. use the final result AFTER the loop




###############################
# FUNCTIONS
###############################

# DEMO:
# a function is a named block of reusable code

# defining a function does NOT execute its body



# the function executes when we CALL it
# how to consider return values: 
# result = <whatever the function returns>

# TERMINOLOGY:
#
# temperature is a PARAMETER
#
#              parameter
#                  |
#                  v
# def f_to_c(temperature):
#
#
# 72 is an ARGUMENT
#
#      argument
#         |
#         v
# f_to_c(72)


###############################
# FUNCTION TASK
###############################

# TASK:
# write a function named classify_temperature()
#
# it should accept one temperature as a parameter
#
# return:
#
# "cold" if temperature < 50
# "mild" if temperature is from 50 through 79
# "hot" if temperature >= 80


# def classify_temperature(temperature):
#     ...


# Test your function with several values:
#
# print(classify_temperature(40))
# print(classify_temperature(65))
# print(classify_temperature(90))



########################################################
# CULMINATING TASK: DAILY TEMPERATURE ANALYZER
########################################################

"""
TASK:

Write a small program that analyzes 5 daily temperature readings.

For each day:

1. Ask the user to enter the temperature.
2. Convert the user's input to a float.
3. Add the temperature to a running total.
4. Count the day as a hot day if the temperature
   is 80 degrees or higher.

After all 5 temperatures have been entered:

1. Calculate the average temperature.
2. Print the average temperature.
3. Print the number of hot days.


Example:

Day 1 temperature: 72
Day 2 temperature: 81
Day 3 temperature: 77
Day 4 temperature: 85
Day 5 temperature: 69

Average temperature: 76.8
Hot days: 2


Think about the structure BEFORE writing code:

What variables need to exist before the loop?

What needs to happen during each iteration?

What calculations can only happen after the loop?


Suggested starting point:

total_temperature = 0
hot_days = 0

for day in range(...):
    ...


IF YOU FINISH EARLY:

1. Use your f_to_c() function to also
   print the average temperature in Celsius.

2. Ask the user what temperature should count as "hot"
   instead of always using 80.

3. Write a function that accepts an average temperature
   and returns "cold", "mild", or "hot".


QUESTION FOR NEXT TIME:

Right now we can calculate an average and count hot days,
but we do not actually KEEP each temperature after processing it.

What if we wanted to save all 5 temperatures so that
we could use them again later?

That is the problem we will solve with lists.
"""