#!/usr/bin/python3
""" login into github using API """
from sys import argv
import requests


if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(user, passwd))
    print(response.json().get('id'))
