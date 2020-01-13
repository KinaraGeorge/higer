#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})

    try:
        j = r.json()

        if not j:
            print("No result")
        else:
            print("[{}] {}".format(j['id'], j['name']))
    except:
        print('Not a valid JSON')
