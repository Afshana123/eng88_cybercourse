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


