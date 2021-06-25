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
