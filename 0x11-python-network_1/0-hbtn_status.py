#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status."""

import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/") as response:
    content = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode("utf-8")))
