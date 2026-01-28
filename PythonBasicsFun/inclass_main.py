# math, datetime, random
import math
from datetime import datetime
import random
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


###############################
# USER INPUT
# fav_num = int(input("What is your favorite num? "))

# print(type(fav_num))
# print(f"your fav num plus one is {fav_num + 1}")


###############################
# CONDITIONALS (AKA if statements)
# we have if elif (else if) else
    # python uses indentation to group statements together (like { })

temp = 90
humidity = 100
if temp < 45:
    print("it is cold out")
elif temp > 80:
    print("it is hot out")
    if humidity > 70:
        print("it is really bad out")
else:
    print("it is nice out")
# you can nest if statements inside if statements
# watch your indentation


###############################
# LOOPS
# we have for loops and while loops
# for item in sequence:
#     body of statements to be repeated

for num in [1,6,7]:
    print(num)

for letter in "hello":
    print(letter)

# we can make our own numeric sequences with range()
# range(stop) [0, stop)
# range(start, stop) [start, stop)
# range(start, stop, step) step to specify a inc/dec other than 1

for i in range(10,6, -1):
    print(i, end=" ")


# TASK: print the first 20 even numbers all on one line
# separated by a comma and a space
# 2, 4, ...., 40
print()
for i in range(2, 39, 2):
    print(i, end= ", ")
print(i+2)

# while loop structure
# while boolean condition is true:
#    body (code we want repeated)
#    progress towards boolean condition being false
x = 0
while x < 5:
    print(x)
    x += 1


# task: rewrite the even number loop using a while loop
x = 2
while x < 40:
    print(x, end=", ")
    x += 2
print(x)

# you can get an early exit from a loop with the break keyword
# while True:
#     user_input = input("enter a word (\"stop\" to exit): ")
#     if user_input == "stop":
#         break
#     if user_input == "next":
#         continue
#     print(user_input)
# print("outside the loop")


# FUNCTIONS
# a function is a named sequence of statements
# functions can accept inputs (arguments when you call; 
# parameters when you define the function)
# they can return 0 or more values
# def function_name(parameter list):
#     body (only executes once you call the function)

def my_msg(msg):
    """
    prints out msg with the date and time appended to the front
    """
    print(f"{datetime.now()}: {msg}")

my_msg("hello")
my_msg("it is very cold today")


def double(x):
    double_val = x* 2
    return double_val, x

number = 3
number, original_val = double(number)

print(number)
print(original_val)
# returning multiple values



# TASK: define/call a function that accepts a radius
# and returns the area and circumference of a circle with that radius
# formula:  area -> pi * r^2
#           circumference -> 2*pi *r

# math.pi

def circle(radius):
    """
    returns the area and circumference of a circle based on radius
    """
    area = math.pi * (radius ** 2)
    cir = 2 * radius * math.pi
    return area, cir

r = 3
area, circumference = circle(r)
print(area, circumference)

# tuples are immutable (can't be changed)
# lists are mutable (can be changed)

# unpacks return values

# RANDOM NUMBERS
# often we need random numbers for simulating random events
# or initializing the state of an algorithm


# if you want the same random numbers each time you run
# your program, "seed" the random number generator
# random.seed(1)

roll1 = random.randint(1,6)
roll2 = random.randint(1,6)
roll3 = random.randint(1,6)
print(roll1,roll2, roll3)