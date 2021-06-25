# Python OOP's 

---

OOP (Object oriented programming) is a way of programming that focuses on using objects and classes to design and build applications. There are 4 pillars of OOP:
 
- Inheritance 
- Abstraction
- Encapsulation
- Polymorphism

## Abstraction
To abstract something means to hide away the details inside something. For example, when we are calling a function

It is essentially like the saying 'what you see is what you get' - you do not need to know what's going on behind the scenes

## Inheritance 


Inheritance lets one object acquire the properties and methods of another class 

You can derive classes from a base class 

The benefit of inheritance is that it prevents code duplications meaning you do not have to repeat a code

For example, 

if we created a class called person and in the person's class, we created variables such as the name, DOB, address and gender. We basically have inherited all those things meaning we don't need to rewrite the information again.

When we want to create, you import person from person. Then you can create a separate class

You can inherit a child class from a parent class
  
## Encapsulation 


This is removing access of part of your code and making it private.

You can hide data from the user in situations where you would like to restrict information.

For example, in a bank where only the user can see their own information

You do this by putting an underscore to make it private e.g:
__dob = 01/01/1991

It is available but not accessible unless you are authorised to do so.



## Polymorphism 


Polymorphism means many forms. 

This is when you would like create more functionalities 
You're not changing anything in the parent class, but inheriting more to put into parent class 

Phrases for classes: 
- Super class, base Class, parent class all mean the same thing. 
- Child class is inheriting from the above.

Once you have inherited everything from the previous class, you can override particular attributes or behaviours without affecting the superclass.

## Python Modules
```python
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
```
## Animal Class Exercise 

```python
# We will be creating an animal class
# The behaviours are all the methods
# The attributes are variables
# We will then be creating a reptile class which will inherit from the animal class

# Animal > Reptile > Snake > Python
# Inheritance > Abstract > Encapsulate > Override

# animal file to create Animal class
# class name must start with a capital letter

# class Animal:
#     pass

# You can write the keyword pass if you don't want to create any functionalities at the time

class Animal:

    # if you want to initialise the class
    def __init__(self): # self refers to the current class
        # You create your variables
        # In a normal circumstance, you would create the variables as normal e.g alive = True but when you are dealing with classes, you need to add self.
         self.alive = True
         self.spine = True
         self.eyes = True
         self.lungs = True

    def breathe(self):
        return "Keep breathing to stay alive."

    def eat(self):
        return "nom nom nom nom"

    def move(self):
        return "Moving all around the world! "

# Nothing will be printed until you call the functions
# If you want to use these method functions within the class, we will need to create an object of our Animal class

cat = Animal() # This is how we create an object of our Animal class called cat

print(cat.breathe()) # breathing for cat is abstracted

# Without creating an object (instantiating) the class, you won't be able to call the methods
```

```python
# Creating a reptile class to inherit everything Animal class

from animal import Animal
# in these brackets, we need to pass the name of the class we would like to inherit from
class Reptile(Animal):

    def __init__(self): # initilaises the current class and all of the other functions within the class so that when you call the function, it is able to run it
        # we have a keyword called super which inherits everything from parent class at the time of initilaisation of this class
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None # because not all reptiles ae tetrapods - it won't throw an error - neither true nor false
        self.heart_chabers = [3,4] # could be 3 or 4

    def seek_heat(self):
        return "It's raining and windy, where is the sun?.... "

    def hunt(self):
        return "Keep hunting for food until you get it."

    def use_venom(self):
        return "If I've got it, I'm using it"

reptile_object = Reptile()

# print("This function is from the Reptile class: " + reptile_object.seek_heat())
# print("This function is inherited from the Animal class: " + reptile_object.eat())

# This the amazing benefits of using OOP and inheritance

# What is the difference between a function and a method? A method is a function inside a class.
```
```python
# Creating a reptile class to inherit everything Animal class

from animal import Animal
# in these brackets, we need to pass the name of the class we would like to inherit from
class Reptile(Animal):

    def __init__(self): # initilaises the current class and all of the other functions within the class so that when you call the function, it is able to run it
        # we have a keyword called super which inherits everything from parent class at the time of initilaisation of this class
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None # because not all reptiles ae tetrapods - it won't throw an error - neither true nor false
        self.heart_chabers = [3,4] # could be 3 or 4

    def seek_heat(self):
        return "It's raining and windy, where is the sun?.... "

    def hunt(self):
        return "Keep hunting for food until you get it."

    def use_venom(self):
        return "If I've got it, I'm using it"

reptile_object = Reptile()

print("This function is from the Reptile class: " + reptile_object.seek_heat())
print("This function is inherited from the Animal class: " + reptile_object.eat())

# This the amazing benefits of using OOP and inheritance

# What is the difference between a function and a method? A method is a function inside a class.
```
```python
# Creating snake class as a child class of reptile

from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.forked_tongue = True
        self.venom = None
        self.limbs = False

    def __use_tongue_to_smell(self):
        return "I can smell the taste...:"

snake_object = Snake()
print("This function is from snake class " + snake_object.use_tongue_to_smell())
print("This function is from the reptile class " + snake_object.seek_heat())
print("This function is from animal class " + snake_object.eat())

```
```python
# creating python class

from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return "Yum yum yum..."

    def climb(self):
        return "Up we go..."

    def shed_skin(self):
        return "Time to grow out of myself! "

#T hese essentially mean the same thing, it's like saying name = "Afshana" and first_name = "Afshana", it's just the naming convention that has changed
python_object = Python()
dog_object = Python()


print(" This climb function is from python class " + python_object.climb())
print("This function is from snake class " + python_object.__use_tongue_to_smell()) # this is encapsulation

# You can override your functionalities in your new class
```
## Exercise: Create a simple calculator class

```python
# Prompt the user to take the numbers

class Simple_calc:

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def divide(self, value1, value2):
        return value1/value2

    def multiply(self, value1, value2):
        return value1 * value2

# create an object for this class

calc_object = Simple_calc()

# call the function

print(calc_object.add(2,5))
```

## Exercise: Create a functional calculator task which inherits from the simple calculator class
```python
from oop_calc_task import Simple_calc

class Function_calc(Simple_calc):

    def __init__(self):
        super().__init__()

    def is_number_divisible(self, value1, value2):
        if value1 % value2 == 0:
            return True
        else:
            return False

    def area_of_triangle(self, height, base):
        return 1 / 2 * base * height * 2.54

fun_object = Function_calc()

# print statements for all the functions available in parents class as well as this(child) class
print(fun_object.is_number_divisible(20,5))
print(fun_object.is_number_divisible(7,2))
print(fun_object.area_of_triangle(5,2))
print(fun_object.add(5,2))
print(fun_object.subtract(10,3))
print(fun_object.divide(15,3))
print(fun_object.multiply(4,2))
```

## Exercise: Create a calculator class that receives input from its user
```python
from functional_calc import Function_calc

class User_input(Function_calc):

    def __init__(self):
        super().__init__()

    def value_inputted(self):
        user_prompt = True
        while user_prompt:

            print("The following operations are available:")
            print("add")
            print("subtract")
            print("divide")
            print("multiply")
            print("check for remainder")
            print("area of triangle")

            operation_type = (input("Please type in which you would like to do: "))

            if operation_type == "add":
                value1 = int(input("Please enter your first value: "))
                value2 = int(input("Please enter your second value: "))
                print(user_input.add(value1, value2))
                break

            elif operation_type == "subtract":
                value1 = int(input("Please enter your first value: "))
                value2 = int(input("Please enter your second value: "))
                print(user_input.subtract(value1, value2))
                break

            elif operation_type == "divide":
                value1 = int(input("Please enter your first value: "))
                value2 = int(input("Please enter your second value: "))
                print(user_input.divide(value1, value2))
                break

            elif operation_type == "multiply":
                value1 = int(input("Please enter your first value: "))
                value2 = int(input("Please enter your second value: "))
                print(user_input.multiply(value1, value2))
                break

            elif operation_type == "check for remainder":
                value1 = int(input("Please enter your first value: "))
                value2 = int(input("Please enter your second value: "))
                print(user_input.is_number_divisible(value1, value2))
                break

            elif operation_type == "area of triangle":
                value1 = int(input("Please enter your first value: "))
                value2 = int(input("Please enter your second value: "))
                print(user_input.area_of_triangle(value1, value2))
                break

            else:
                print("Error. Please try again later")
                break


user_input = User_input()
user_input.value_inputted()
```
## Exercise: Create a movie rating class

```python
# Create a class called Movie Rating and functions for each block of code movie rate

class Movie_ratings:

    def ratings_checker(self):
        pg = "Movie A"
        twelve_plus = "Movie B"
        fifteen_plus = "Movie C"
        eighteen_plus = "Movie D"
        universal = "Movie E"

        age = int(input("Welcome! Please enter your age: "))
        if (age >= 18):
            print("No one younger than 18 may see an 18 film in a cinema.")
            print(str(input(
                "The following movies are available: " + pg + ", " + twelve_plus + ", " + fifteen_plus + ", " + eighteen_plus + ", " + universal + ", " + " Please type in which movie you would like to watch: ")))
        elif (age >= 15 and age < 18):
            print("No one younger than 15 may see a 15 film in a cinema.")
            print(str(input(
                "The following movies are available: " + pg + ", " + twelve_plus + ", " + fifteen_plus + " " + universal + ", " + " Please type in which movie you would like to watch: ")))
        elif (age >= 12 and age < 15):
            print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
            print(str(input(
                "The following movies are available: " + pg + ", " + twelve_plus + ", " + universal + ", " + " Please type in which movie you would like to watch: ")))
        elif (age >= 10 and age < 12):
            print("General viewing, but some scenes may be unsuitable for young children")
            print(str(input(
                "The following movies are available: " + pg + ", " + universal + ", " + " Please type in which movie you would like to watch: ")))
        else:
            print("Please try again: ")

        print(str(input("Your ticket has been printed. Please take your ticket to the counter to pay. Thank you. ")))


user_input_movie = Movie_ratings()
user_input_movie.ratings_checker()
```
