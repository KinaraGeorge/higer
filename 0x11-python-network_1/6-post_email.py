#!/usr/bin/python3
"""
send data to a site using requests
"""

import requests
import sys

if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    posted = response.text

    print(posted)
