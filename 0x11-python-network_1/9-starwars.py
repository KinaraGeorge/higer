#!/usr/bin/python3
"""
takes in a string and sends a search request to the Star Wars API
"""

import requests as web
from sys import argv

if __name__ == "__main__":
    r = web.get('https://swapi.co/api/people/?search={}'.format(argv[1]))
    j = r.json()
    print("Number of results: {}".format(j['count']))
    for name in j['results']:
        print(name['name'])
