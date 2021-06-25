# Python

---
*Python installation (Version 3.9.5)*

## Pycharm set up


Documentation with README.md to store on Git-hub

Dynamically typed language 
- Testing the python env `print("Hello World")`


## Introduction

---

### What is DevSecOps and what does the role entail?

DevSecOps which stands for Development, Security and Operations is a role which incorporates security throughout the application development cycle. It is an early integration of secure culture, tools and practices into each phase of the development and operations processes.

A DevSops framework is one that uses tools ensuring security is built into applications rather than doing it at the end of testing an application just to check that its secure. Sometimes, that could be damaging because a hacker could deploy malware into an application during the built process and the malware might not been discovered until the application has been distributed.

Some of the general roles of DevSecOps includes:

- Spotting vulnerabilities and bugs early
- Automating different phases of the DevOps pipeline
- Managing the IT infrastructure
- Choosing the best tools and technologies the team requires to meet the business needs
- Designing, building, testing and maintain the continuous integration and delivery process
- Integrating and connecting application elements

#
### Why Python and how does it fit into DevSecOps Engineering?

Python is open source which means that it is freely usable and distributable even for commercial use

It is a multi-platform and is widely utilised on windows, mac and Linux

Used in multiple industries.

It has a huge list of supporting libraries to help accelerate development in many areas. Its vast libraries for DevSecOps toolsets are also preferred when comparing it to others because of its ease of access and flexibility.

Using Python for DevSecOps is a great scripting language for use in DevOps automation. For example: automating the DevOps life cycle management.

It is ahead of other coding languages. For example: to debug and code - it is more ahead than Ruby

You are also able to build web applications, data visualisation as well as build custom utilities

#
### Why do you want to become a DevSecOps Consultant?

The IT industry has been going through tremendous changes over the past decade. Organisations nowadays are looking to thrive and grow their business using advanced applications, automation, and services. DevOps application have been proven to be successful for organisations but there has a growing need for security as hackers become more creative in looking for ways to deploy malware. That is why DevSecOps is needed and I would like to become a DevSecOps consultant in order to help companies defeat this challenge faced.

I also want to contribute and grown within my role of becoming a DevSecOps consultant knowing that I am helping and preventing an organisation from damage from hackers and security breaches keeping the companies reputations as a priority through the implementation of development, security and operation.


## Variables

---

What are variables?

- Variables work as a place-holder to store data
- Strings, Boolean, Integers
- "Is considered a String"
- Boolean is True or False
- Numbers are ints
  

``` python
# # Let's create a variable for first name, last name and DOB
# # syntax name of the variable = value to store in the variable
# # Naming Convention to follow

first_name = "Afshana" # string
last_name = 'Begum' #string
salary = 111 # integer

print(last_name)
print(last_name)
print(salary)
```

``` python
float_value = 111.12 

# float values: anything with a decimal is considered a float
# to find out the type of variable, we have method called type()

print(type(float_value))
print(type(salary))
print(type(first_name))
```

``` python
# Taking user input - we have a method called input()
print("Please enter your name ")
name = input("")
print("Hello")
print(name)
```
Task: Ask the user to input their name, age and date of birth

```python
# Activity: Ask the user for their name, age and DOB 

print("Please enter your name: ")
name = input("")
print("Hello" + name)
print(name)

print("Please enter your age: ")
age = input("")
print("Hello, you are")
print(age)
print("years of age")

print("Please enter your date of birth: ")
date_of_birth = input("")
print("Thank you")#
print(name)
```


## Operators 

---

**Arithmetic Operators**
` + - * /  `

**Comparison Operators**
` > < == != >= <= `
` % ` Modulus - remainder of the division of left operand by the right 

Note: if you right-click on line 53, and click on soft-wrap then it will move the text so that you can view everything 

### Arithmetic Operators

| Operand | Description | Example |
|:---------: |:----------------------------: |:--------: |
| + | add two operands (variables) together| X + y + 2 |
| - | subtract two operands (variables) | X - y - 2 |
| * | multiply two operands (variables) | X - y - 2 |
| / | divide two operands (variables) | X - y - 2 |
| % | Modulus - remainder of the division of left operand by the right | X - y - 2 |
| + | add two operands (variables) together| X + y + 2 |



### Comparison Operators

| Operand | Description | Example |
|:---------: |:----------------------------: |:--------: |
| > | True if left operand is greater than the right| x > y |
| < | True if left operand is less than the right| x < y |
| == | True if both operands are equal | x == y |
| != | True if both operands are equal | x != y |
| >= | True if left operand is greater than or equal to the right| x >= y |
| <= | True if left operand is less than or equal to the right| x <= y |

```python
# Arithmetic Operators
# + - * /

# Comparison Operators
# >
# <
# ==

value1 = 6
value2 = 7

print(value2 > value1) # checking if value2 greater than value1 (this is a Boolean type)
print(value1 > value2) # checking if value 1 is greater that value 2
print(value1 + value2) # adding the values
print(value1 - value2) # subtracting the values
print(value1 >= value2) # checks if value1 is greater than or equal to value2
print(value1 != value2) # checks if they are not equal to each other
```
```python
# We have built in methods available in python that give us boolean outcomes as well

Name = "James"

# we have a method called isalpha() which checks if the value is alphabetical
print(Name.isalpha()) # return the boolean outcome True

print(Name.isdigit()) # checks the value if it is in digits

print(Name.startswith("J")) # checks if it is in capital
```
```python
# Strings, Concatenation and Casting

# Indexing
# greetings = "Hello World!"
# H E L L O   W O R L D  !
# 0 1 2 3 4 5 6 7 8 9 10 11

#To find out the length of characters in the string, we use the method len()
print(len(greetings))

# String Slicing
#We want it to only display index elements 0 and 1
print(greetings[0:2])

white_spaces = "lot's of spaces at the end                         "
print(len(white_spaces))
print("strings with empty spaces")
# We want to get rid of white spaces
print(len(white_spaces.strip()))
print("strings without empty spaces")

Example_text = "Here's some text with lot's of text"
# counts words that appear more than once
print(Example_text.count("text")) # counts how many times 'text' is written in the string stored in example_text

print(Example_text.lower()) # changes the string to lower case
print(Example_text.upper()) # changes the string to upper case
print(Example_text.capitalize()) # changes the first letter to a capital letter
print(Example_text.replace("with", ",")) # replaces "with" with a comma

```
```python
# Concatenation - combining values, variables, strings together

First_Name = "James"
Last_Name ="Bond"
age = "99"
# print(First_Name)
# print(Last_Name)

# There are two ways of concatenating 
# Using the style below
print(First_Name + " " + Last_Name + " " + str(age))

# or you can do the formatting method:
print(f"{First_Name} {Last_Name} is {age} old")

# str() is the method that converts integer value into string
#
# Casting - casting string into int or int into string

print(type(str(age)))
# Now the output will class age as a string because it has been converted
```

```python
# Activity: Find the method to cast string into integer and display the value and the type after conversion

print(int(age))
print(First_Name + " " + Last_Name + " " + age)
# Note: you cannot concatenate different variables e.g string with an integer
print(type(int(age)))
```

***Notes:***

*- Casting: casting string into an integer or an integer into a string*

*- You cannot concatenate different variables for example: A string with an integer*

*- Look at example above for the two ways of concatenation*
