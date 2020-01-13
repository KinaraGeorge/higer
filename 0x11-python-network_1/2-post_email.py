#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response (decoded in utf-8)
"""

import urllib.request as reque
import urllib.parse as parse
from sys import argv

if __name__ == "__main__":

    value = argv[1]
    data = parse.urlencode({'email':argv[2]}).encode('utf8')

    with reque.urlopen(value, data) as response:
        posted = response.read()
    print(posted.decode('utf-8'))
