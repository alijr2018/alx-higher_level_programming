#!/usr/bin/python3
"""a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response."""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Create the payload with the email
    payload = {'email': email}

    # Send a POST request with the payload
    response = requests.post(url, data=payload)

    # Print the email from the response
    print("Your email is:", email)
