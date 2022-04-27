#!/usr/bin/python3
""" Post email with request """
from sys import argv
import requests


if __name__ == '__main__':
    response = requests.post(argv[1], data={'email': argv[2]})
    output = response.content.decode('utf8')
    print(output)
