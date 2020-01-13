#!/usr/bin/python3
#python script


import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    a = sys.argv[1]
    b = parse.urlencode({"email": sys.argv[2]}).encode('utf8')
    with request.urlopen(a, b) as response:
        print(response.read().decode('utf-8')
