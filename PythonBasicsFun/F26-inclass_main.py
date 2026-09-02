# math, datetime, random
import math
from datetime import datetime
import random
# best practice: put your import statements at top of file

# basic print


###############################
# VARIABLES

# use the built in type() function to determine the type of
# a variable or value

# we can reassign variables


###############################
# OPERATORS
# pretty much the same as C++, with a few exceptions
# / floating point division 
# // integer division 
# % mod
# exponentiation ** 

# another way: import the math module
# and call math.pow()

###############################
# PRINTING AND DECIMAL FORMATTING
# lots of diff ways, choose the one you prefer
# round() or :.2f


###############################
# USER INPUT


###############################
# CONDITIONALS (AKA if statements)
# we have if elif (else if) else
    # python uses indentation to group statements together (like { })


# you can nest if statements inside if statements
# watch your indentation


###############################
# LOOPS
# we have for loops and while loops
# for item in sequence:
#     body of statements to be repeated

# we can make our own numeric sequences with range()
# range(stop) [0, stop)
# range(start, stop) [start, stop)
# range(start, stop, step) step to specify a inc/dec other than 1

# TASK: print the first 20 even numbers all on one line
# separated by a comma and a space
# 2, 4, ...., 40

# while loop structure
# while boolean condition is true:
#    body (code we want repeated)
#    progress towards boolean condition being false


# TASK: rewrite the even number loop using a while loop



# you can get an early exit from a loop with the break keyword



# FUNCTIONS
# a function is a named sequence of statements
# functions can accept inputs (arguments when you call; 
# parameters when you define the function)
# they can return 0 or more values
# def function_name(parameter list):
#     body (only executes once you call the function)




# TASK: define/call a function that accepts a radius
# and returns the area and circumference of a circle with that radius
# formula:  area -> pi * r^2
#           circumference -> 2*pi *r
# math.pi



# tuples are immutable (can't be changed)
# lists are mutable (can be changed)

# unpacks return values

# RANDOM NUMBERS
# often we need random numbers for simulating random events
# or initializing the state of an algorithm


# if you want the same random numbers each time you run
# your program, "seed" the random number generator
# random.seed(1)




"""
Dice Rolling Simulator

Write a program that simulates rolling two six-sided dice.

1. Ask the user how many times they want to roll.
2. For each roll:
   Generate two random numbers from 1 to 6.
   Print both dice and their total.
3. Count how many times doubles are rolled.
4. At the end, print the total number of doubles and the percentage of rolls that were doubles.

If you finish early:

* Put the dice roll into a function that returns both dice values.
* Count how many times the total is 7.
* Count how many times you roll snake eyes (1 + 1) or double sixes (6 + 6).
* Ask the user if they want to run another simulation.

"""