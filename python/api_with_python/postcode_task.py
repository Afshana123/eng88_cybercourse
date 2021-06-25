# Create a function and return the location/postcode if status code is 200
# Get the user to input the postcode
# Validate the post code before making the API call
import requests
import json

class Validate_postcode:

    def promp_user_for_postcode(self):
        user_postcode = input("Please enter your postcode:")
        post_api_response = requests.get("https://api.postcodes.io/postcodes/" + user_postcode)
        if post_api_response.status_code == 200:
            print("Your postcode is valid.")
            print(post_api_response.headers)
            data_headers = post_api_response.headers
            for date_in in data_headers:
                print(date_in)
        else:
            print("Sorry, the postcode is incorrect. Please enter the correct postcode.")

call_postcode = Validate_postcode()
call_postcode.promp_user_for_postcode()
