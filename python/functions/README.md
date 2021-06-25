# Dictionaries
# ----------------------------------------------------------------------------------------------------------------------
# They are structured as KEY : VALUE
# VALUE could be string, int, list
# Syntax {}

student_1 = {
    "Name" : "Afshana",
#   "Key"  : "Value"
    "Stream" : "Cyber Security",
    "Completed_Lessons" : 3,
    "Complete_Lessons" : ["Variables", "Operators", "Data_Collections"] # List
}

print(student_1)

# We can fetch the values with the keys
print(student_1["Name"])
print(student_1["Stream"])
print(student_1["Complete_Lessons"])

# Display only 'Operators' from the list inside the dictionary
print(student_1["Complete_Lessons"][1]) # name of the dictionary followed by the key then the index of the value you want to retrieve

# You can print all the keys as follows
print(student_1.keys())

# You can print all the values as follows
print(student_1.values())

# Sets
# ----------------------------------------------------------------------------------------------------------------------
# Sets are part of data collections but the difference is that they are unordered
# Syntax {}
# You can use sets if you are not worried about the organisation or order of how it is stored

car_parts = {"Wheels", "Doors", "Engine"}

print(car_parts) # the output is that they elements are printed in a random order everytime it is run. It won't be necessarily in the order you have assigned them.


# To add an element
car_parts.add("Windows")
print(car_parts)

# To remove an element
car_parts.discard(("Doors"))
print(car_parts)

# Frozen sets are like Tuples (immutable)
frozen_set = ([1,2,3,4])
print(frozen_set)
