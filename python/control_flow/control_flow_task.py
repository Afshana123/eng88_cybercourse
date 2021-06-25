# Create a programme to check the age according to movie rating and sell the ticket if the age meets the correct criteria

# If false, then display the message to re-enter the correct format or decline the ticket

# Enter user input for the age

pg = "Movie A"
twelve_plus = "Movie B"
fifteen_plus = "Movie C"
eighteen_plus = "Movie D"
universal = "Movie E"

age = int(input("Welcome! Please enter your age: "))
if (age >= 18):
    print(str(input("The following movies are available: " + pg + ", " + twelve_plus + ", " + fifteen_plus + ", " + eighteen_plus + ", " + universal + ", " + " Please type in which movie you would like to watch: ")))
elif (age >= 15 and age < 18 ):
    print(str(input("The following movies are available: " + pg + ", " + twelve_plus + ", " + fifteen_plus + " " + universal + ", " + " Please type in which movie you would like to watch: ")))
elif (age >= 12 and age < 15):
    print(str(input("The following movies are available: " + pg + ", " + twelve_plus + ", " + universal + ", " + " Please type in which movie you would like to watch: ")))
elif (age >= 10 and age < 12):
    print(str(input("The following movies are available: " + pg + ", " + universal + ", " + " Please type in which movie you would like to watch: ")))
elif (age < 10 ):
   print(str(input("The following movies are available: " + pg + ", " + universal + ", " + " Please type in which movie you would like to watch: ")))


print(str(input("Thank you, please type 'exit' to exit the terminal: ")))

