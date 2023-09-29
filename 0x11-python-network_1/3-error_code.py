#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8)."""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('ascii')
            print(content)
    except urllib.error.HTTPError as e:
        print("Erro code:", e.code)
