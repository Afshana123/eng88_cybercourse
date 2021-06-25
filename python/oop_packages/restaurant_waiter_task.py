# Create a program that helps a waiter with their menu and orders

class Restaurant_order:

    def __init__(self): # self refers to this class
         self.orders = True

    def menu_created(self):
        menu_list = {
            "1" : "Margherita Pizza",
            "2" : "Vegetarian Pizza",
            "3" : "BBQ Chicken Pizza",
            "4" : "Calzone",
            "5" : "Lasagna",
            "6" : "Pasta",
            "7" : "Cookie Dough",
            "8" : "Cake"
        }
        for menu in menu_list.items():
            print(menu)

    def introduction(self):
        user_prompt = True
        while user_prompt:
            print("Welcome! Let's begin ordering your items. Type 'exit' at any time you would like to leave the service. ")
            first_order = input("Please type in the number from the list according to what you would like to order: ")
            break

    def next_order(self):
        ask_the_user = input("Thank you. Would you like to add another item? Y/N: ")
        if ask_the_user == "N":
            print("Here is a summary of your order")
        elif ask_the_user == "Y":
            second_order = input("What would you like to order next? ")


    def ask_order(self):
        ask_the_user = input("Thank you. Would you like to add another item? Y/N: ")
        return print_menu.next_order()\\\\\\\\\\\

    def summary_order(self):



print_menu = Restaurant_order()
print_menu.menu_created()
print_menu.next_order()
print_menu.ask_order()
print_menu.summary_order()



