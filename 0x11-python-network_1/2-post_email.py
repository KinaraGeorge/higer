#!/usr/bin/python3
#python script


import urllib.request as reque
import urllib.parse as parse
import sys

if __name__ == "__main__":
    value = sys.argv[1]
    dat = parse.urlencode({'email': sys.argv[2]}).encode('utf8')

    with reque.urlopen(url=value, data=dat) as response:
        posted = response.read()

    print(posted.decode('utf-8'))
