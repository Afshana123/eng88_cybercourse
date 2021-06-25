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

