#!/usr/bin/python3
"""a Python script that takes your GitHub credentials,
(username and password) and uses the GitHub API to display your id."""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    headers = {
        "Authorization": "token " + token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info.get('id')
        print(user_id)
    else:
        print(None)
