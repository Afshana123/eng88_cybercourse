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

