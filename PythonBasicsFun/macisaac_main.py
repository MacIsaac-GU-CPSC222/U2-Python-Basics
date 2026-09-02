# math, datetime, random
import math
from datetime import datetime
import random as rn

# best practice: put your import statements at top of file

# basic print
print("Hello World!") # this does a printout

# this is a one line comment

"""
this
is a 
multiline comment
print("test") """


###############################
# VARIABLES
x = 78
y = 10.6

x = "this is a string now"

print(x, type(x))

x = True
x = False
# use the built in type() function to determine the type of
# a variable or value

# we can reassign variables


###############################
# OPERATORS
# pretty much the same as C++, with a few exceptions
# / floating point division 
# // integer division 
# % mod

x = 5//2
print(type(x))

x = 5%2
print(x)

# exponentiation ** 

x = 3 ** 2
print(x)

# another way: import the math module
# and call math.pow()
x = math.pow(3, 2)
print(x)

###############################
# PRINTING AND DECIMAL FORMATTING
# lots of diff ways, choose the one you prefer
# round() or :.2f

x = 10.55678
print(f"this is a string {x}")

print(f"x = {x:.2f}")

print(round(x,2))

# print automatically adds a newline after whatever is output
print("line 1")
print("line 2")
print("line 3")

# change/remove it with end argument
# special type of function argument
# argument is named rather than relying only on position
# named arguments must come after positional arguments
print("line 1", end= ".")
print("line 2", end="next")
print("line 3", end=" ")
print()

###############################
# USER INPUT

# fav_num = int(input("What is your favorite number? "))

# print(f"your fav num is {fav_num}")
# print(type(fav_num))

# print(f"your fave num doubled is {fav_num * 2}")



###############################
# CONDITIONALS (AKA if statements)
# we have if elif (else if) else
    # python uses indentation to group statements together (like { })
temp = 45
if temp < 32:
    print("it is cold")
elif temp < 60:
    print("it is nice out")
else:
    print("it is warm")
# you can nest if statements inside if statements
# watch your indentation


###############################
# LOOPS
# we have for loops and while loops
# for item in sequence:
#     body of statements to be repeated
sum = 0
for x in [1,2,6,7]:
    print(x)
    sum = sum + x
    # sum += x
print(sum)

for char in "hello":
    print(char)

# we can make our own numeric sequences with range()
# range(stop) [0, stop)
# range(start, stop) [start, stop)
# range(start, stop, step) step to specify a inc/dec other than 1

# for x in range()


# TASK: print the first 20 even numbers all on one line
# separated by a comma and a space
# 2, 4, ...., 40




# while loop structure
# while boolean condition is true:
#    body (code we want repeated)
#    progress towards boolean condition being false
# task: rewrite the even number loop using a while loop
x = 0
while x < 10:
    print(x)
    x += 4


# you can get an early exit from a loop with the break keyword
# while True:
#     user_input = input("enter a word (\"stop\" to exit): ")
#     if user_input == "stop":
#         break
# print("outside the loop")



# FUNCTIONS
# a function is a named sequence of statements
# functions can accept inputs (arguments when you call; 
# parameters when you define the function)
# they can return 0 or more values
# def function_name(parameter list):
#     body (only executes once you call the function)

def my_print(msg_str):
    """ docstring
    prepend a timestamp to the msg_str before printing

    returns: None
    """
    print(f"{datetime.now()}: {msg_str}")

my_print("Hello from class")


# returning multiple values

def name_split(fullname):
    """
    splits fullname (str) into two strings
    returns first_name (str), last_name(str)

    fullname = "Dominic MacIsaac"
    return "Dominic", "MacIsaac"
    """
    name_list = fullname.split(" ")
    first_name = name_list[0]
    last_name = name_list[1]
    return first_name, last_name

full = "Dom Mac"
first, last = name_split(full)

print(first)
print(last)
# TASK: define/call a function that accepts a radius
# and returns the area and circumference of a circle with that radius
# formula: pi * r^2




# tuples are immutable (can't be changed)
# lists are mutable (can be changed)

# unpacks return values

# RANDOM NUMBERS
# often we need random numbers for simulating random events
# or initializing the state of an algorithm

# if you want the same random numbers each time you run
# your program, "seed" the random number generator

rn.seed(0)
roll = rn.randint(1,6)
print(f"roll: {roll}")