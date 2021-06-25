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


