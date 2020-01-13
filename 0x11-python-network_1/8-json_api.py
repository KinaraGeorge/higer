#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request"""

import requests
from sys import argv

if __name__ == "__main__":

    letter = ""
    if len(argv) == 2:
        letter = argv[1]

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
        j = r.json()

        if j:
            print('[{}] {}'.format(j.get('id'), j.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
