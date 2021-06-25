# Let's use python to make an API call using a package called requests
# Dependencies are pip

# pip is the package manager

import requests
import json

post_api_response = requests.get("https://api.postcodes.io/postcodes/se120nb")
if post_api_response.status_code == 200: # A HTTP status code means success. It indicates that the request has been processed successfully on the server.
    print("Thank you for your request " + str(post_api_response.status_code))
else:
    print("Sorry, the postcode is incorrect. Please enter the correct postcode.")

#if status code was 404, then this would tell a web user that a requested page was 'not found'. This means that the page you were trying to reach on the website couldn't be found on their server.

# Allows user to input their post code and gives back their response if it is live
user_postcode = input("Please enter your postcode:")
post_api_response = requests.get("https://api.postcodes.io/postcodes/" + user_postcode)
print(post_api_response)
















response_bbc = requests.get("https://www.bbc.co.uk/")

# print(response_bbc)
# print(response_bbc.status_code)

# print(response_bbc.headers)
# data_headers = response_bbc.headers
# for date_in in data_headers:
#     print(date_in)
