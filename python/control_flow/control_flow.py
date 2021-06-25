# We use the if, elif and else statements when we have multiple conditions. These are used in Python for decision making.

# if, elif and else statement:
# ----------------------------------------------------------------------------------------------------------------------

weather = "rainy"

if weather == "thinking":
   print("Enjoy the weather ") # If true, then this line will be executed
else:
   print ("Oops sorry, something went wrong. Please try later.") # If false, this line will be executed

# add a condition to use elif when the condition is False

if weather == "sunny":
    print("Enjoy the weather!") # If true, this line will be executed
elif weather == 'rainy':
    print("Remember to take an umbrella!")
else:
    print ("Oops sorry, something went wrong. Please try again later.") # If false, this line will be executed

# Loops
# ----------------------------------------------------------------------------------------------------------------------
# Loops are used to iterate through data such as lists, dictionaries and sets etc.

# The for loop:
------------------------------------------------------------------------------------------------------------------------
list_data = [1, 2, 3, 4, 5]
print(list_data)
for list in list_data:
    print(list)

# this is saying to go and look for the list from the list data and iterate through the list until it reaches the last number

# Break keyword
-----------------------------------------------------------------------------------------------------------------------
# list_data = [1, 2, 3, 4, 5]

for list in list_data:
    if list == 3:
        break
    print(list) # this will iterate through until it reaches 3 and print everything before 3

# example

list_data = [1, 2, 3, 4, 5]

for list in list_data:
   if list == 3:
       print("Now I found 3.")
   if list == 2:
       print("I found 2.")
   if list == 5:
       print("5 is the last number and I found it as well.")
   else:
       print("Better luck next time")

# after the condition is met, then it stops running the system

# Example using dictionaries

student_1 = {
    "Name" : "Afshana",
#   "Key"  : "Value"
    "Stream" : "Cyber Security",
    "Completed_Lessons" : 3,
    "Complete_Lessons" : ["Variables", "Operators", "Data_Collections"] # List
}

for data in student_1.values():
    if data == "Cyber Security":
        break
    print(data)

# While Loops
------------------------------------------------------------------------------------------------------------------------
# The while loop is used to iterate over a block of code as long as the test expression (condition) is true
# We generally use this loop when we don't know the number of times to iterate beforehand

user_prompt = True
while user_prompt:
    age = input("Please enter your age: ")
    if age.isdigit():
        user_prompt = False # gives output
    else:
        print("Please provide your answer in digits: ")
print(f"Your age is {age}")

# The process continues to keep going if until the the condition evaluates to false then at this point, it will provide you with your output.

# practice example

user_prompt = True
while user_prompt:
    age = input("Please enter your age: ")
    if age.isdigit():
        name = input("Please enter your name: ") # gives output
        user_prompt = False
    else:
        print("Please provide your answer in digits: ")
print(f"Your age is {age} and your name is {name}.")
