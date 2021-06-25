# Let's create a basic function to greet user
# Syntax def name()

# First Iteration
def greetings():
    return "Welcome to Cyber Security!"  # you need to call the function in order for you to execute the command

print(greetings())

# Second Iteration
def greeting_user(name):
    return "Welcome on board " + name + "!"

print(greeting_user("engineering 88"))

# Exercise: Take user name as input() and display it back to them with greeting messages of your choice
user_name = str(input("What is your name? "))

def greet_user(user_name):
    return "Welcome " + user_name

print(greet_user(user_name))

# Create a function that takes 2 args as ints

def add(value1, value2):
    return value1 + value2

print(add(2, 3))


def subtract(value1, value2):
    return value1 - value2

print(add(9, 5))


def multiply(value1, value2):
    return value1 * value2

print(add(2, 3))


def divide(value1, value2):
    return value1 / value2

print(add(8, 2))

# Create a function that calculates the percentage
def percentage(value1, value2):
    return (value1 / value2) * 100

print(percentage(2, 3))
