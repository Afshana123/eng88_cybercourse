# Application Programming Interface (API)
_API with python_

## What is API?
An API (Application Programming Interface) is a set of functions that allows applications to access data and interact with external software components, operating systems, or microservices. To simplify, an API delivers a user response to a system and sends the system's response back to a user

## Code Along Exercise
```python
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
```

## Exercise: 
```python
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
```
