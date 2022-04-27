#!/bin/bash
# Example of email send to argument URL
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
