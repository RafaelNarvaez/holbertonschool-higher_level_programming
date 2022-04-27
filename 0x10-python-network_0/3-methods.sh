#!/bin/bash
# Dsplay http methods
curl -i -sX OPTIONS -L "$1" | grep 'Allow' | cut -c8-
