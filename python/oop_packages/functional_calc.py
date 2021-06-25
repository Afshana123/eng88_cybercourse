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


