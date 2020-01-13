#!/usr/bin/python3
# Python script that fetches a url
import urllib.request as web

if __name__ == "__main__":

    with web.urlopen('https://intranet.hbtn.io/status') as URL:

        html = URL.read()

    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(html), html))
    print('\t- utf8 content: {}'.format(html.decode('utf-8')))