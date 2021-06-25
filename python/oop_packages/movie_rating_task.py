# Create a class called Movie Rating and functions for each block of code movie rate

class Movie_ratings:

    def ratings_checker(self):
        pg = "Movie A"
        twelve_plus = "Movie B"
        fifteen_plus = "Movie C"
        eighteen_plus = "Movie D"
        universal = "Movie E"

        age = int(input("Welcome! Please enter your age: "))
        if (age >= 18):
            print("No one younger than 18 may see an 18 film in a cinema.")
            print(str(input(
                "The following movies are available: " + pg + ", " + twelve_plus + ", " + fifteen_plus + ", " + eighteen_plus + ", " + universal + ", " + " Please type in which movie you would like to watch: ")))
        elif (age >= 15 and age < 18):
            print("No one younger than 15 may see a 15 film in a cinema.")
            print(str(input(
                "The following movies are available: " + pg + ", " + twelve_plus + ", " + fifteen_plus + " " + universal + ", " + " Please type in which movie you would like to watch: ")))
        elif (age >= 12 and age < 15):
            print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
            print(str(input(
                "The following movies are available: " + pg + ", " + twelve_plus + ", " + universal + ", " + " Please type in which movie you would like to watch: ")))
        elif (age >= 10 and age < 12):
            print("General viewing, but some scenes may be unsuitable for young children")
            print(str(input(
                "The following movies are available: " + pg + ", " + universal + ", " + " Please type in which movie you would like to watch: ")))
        else:
            print("Please try again: ")

        print(str(input("Your ticket has been printed. Please take your ticket to the counter to pay. Thank you. ")))


user_input_movie = Movie_ratings()
user_input_movie.ratings_checker()
