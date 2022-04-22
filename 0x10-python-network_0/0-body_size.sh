#!/bin/bash
# How to get a body size
curl -s --head "$1" | grep "Content-Lenght" | cut -d ' ' -f 2