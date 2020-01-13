#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response (decoded in utf-8)"""

import urllib.request as reque
import urllib.parse as parse
from sys import argv

if __name__ == "__main__":

    value = {'email': argv[2]}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = reque.Request(argv[1], data)
    with reque.urlopen(req) as response:
        print(str(response.read(), 'utf-8'))
