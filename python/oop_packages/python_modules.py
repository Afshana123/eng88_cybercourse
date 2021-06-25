# What are Python Modules?

# We have built in modules that we can find on Python's library

# For example:
# if the value is 1.49 and you apply the floor() function, then it will round up to 1
# if the value is 1.50 and you apply the ceil() function, then it will round up to 2

# We have a keyword called import that we can use to call a module

       # this is a class called random that generates random numbers
import random
print(random.random()) # printing a specific function method

# print a random number from random
# generates a random number everytime you run in
# Why are we using it? For example, they use this in lottery

# We can rewrite the code above.
# If you want to call it many times, it is easier to call it this way
#    file name     class
from random import random
print(random())

import math
num1 = 23.66
print(num1)
print(math.ceil(num1))
# rounds up

import math
num1 = 23.66
print(num1)
print(math.floor(num1))
# rounds down

# random generates a number from 0 and 1

# Exercise:

# generate a number with random
# apply if conditions
# if the user input is >= .50 apply ceil
# if the user input is <= .49 apply floor
# user should be asked to input data again if they enter a string

import math
generate_number = float(input("Please enter a number of your choice or press enter to generate a random number: "))
num1 = generate_number
if num1 >= 0.5:
    print(math.ceil(num1))
else:
    print(math.floor(num1))


# Exercise:
from random import random
import math

random_number = random()
print("This is randomly generated " + str(random_number))
if random_number >= 0.5:
    print(math.ceil(random_number))
else:
    print(math.floor(random_number))

# We have a package called os which is used to get information about your localhost/your machine such as name, path etc
# If you want to import more than one package, you can put a comma like the way we have done below

import os, sys, datetime, math
#                   cwd: current working directory
working_dir = os.getcwd()
print("This is your current working directory " + working_dir)

# prints current working directory

system_path = sys.path
print("This is the path " + str(system_path))

# you don't want to this all the time, so we can create a function

def current_system_path():
    print("This is your current path " )
    return sys.path
print(current_system_path())

def current_system_directory():
    print("This is your current working directory ")
    return os.getcwd()
print(current_system_directory())

print(os.cpu_count())
print(datetime.datetime.today()) # checks today's date and time

# provides remainder value %
print(math.remainder(1,5))

import math
print(math.pi)

# lambda has a built in functionality
# lambda is mutable

def add(num1, num2):
    return num1 + num2

# arguments: expression
addition = lambda num1, num2: num1 + num2 # calculating the expression

print("Value returned by add() function")
print(add(2,2))
print("Value returned using Lambda function")
print(addition(7,2))

# How to make data private by adding an underscore:

def _add(num1, num2):
    return num1 + num2

# arguments:expression
addition = lambda num1, num2: num1 + num2 # calculating the expression

print("Value returned by add() function")
print(_add(2,2))
print("Value returned using Lambda function")
print(addition(7,2))

# Now if you call this function in another class, you will not be able to import it
