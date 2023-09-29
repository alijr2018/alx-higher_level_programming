#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    rs = requests.get(url)

    print("Body response:")
    print("\t- type:", type(rs.text))
    print("\t- content:", rs.text)
