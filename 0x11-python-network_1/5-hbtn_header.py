#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    rs = requests.get(url)
    rs_id = response.header.get('X-Request-Id')
    print(rs_id)
