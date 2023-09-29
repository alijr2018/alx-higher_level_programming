#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    rs = requests.get(url)
    resquest_id = rs.headers.get('X-Request-Id')

    print(request_id)
