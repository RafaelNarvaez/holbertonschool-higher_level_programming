#!/usr/bin/python3
"""Module for Fetch URL's with URLlib"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: ', end='')
        print(type(html))
        print('    - content: ', end='')
        print(html)
        print('\t- utf8 content: ', end='')
        print(html.decode('utf-8'))
