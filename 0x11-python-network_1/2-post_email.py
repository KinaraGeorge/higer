#!/usr/bin/python3
#python script


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    post_url = sys.argv[1]
    post_data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf8')

    with urllib.request.urlopen(url=post_url, data=post_data) as response:
        posted = response.read()

    print(posted.decode('utf8'))
