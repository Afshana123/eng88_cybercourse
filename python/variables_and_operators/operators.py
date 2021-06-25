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

# We have built in methods available in python that give us boolean outcomes as well

Name = "James"

# we have a method called isalpha() which checks if the value is alphabetical
print(Name.isalpha()) # return the boolean outcome True

print(Name.isdigit()) # checks the value if it is in digits

print(Name.startswith("J")) # checks if it is in capital

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

# Activity: Find the method to cast string into integer and display the value and the type after conversion

print(int(age))
print(First_Name + " " + Last_Name + " " + age)
# Note: you cannot concatenate different variables e.g string with an integer
print(type(int(age)))
