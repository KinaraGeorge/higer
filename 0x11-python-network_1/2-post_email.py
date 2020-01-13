#!/usr/bin/python3
#python script


import urllib.request as reque
import urllib.parse as parse
from sys import argv

if __name__ == "__main__":
    value = argv[1]
    data = parse.urlencode({'email':argv[2]}).encode('utf8')

    with reque.urlopen(value, data) as response:
        posted = response.read()
    print(posted.decode('utf-8'))
