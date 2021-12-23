#!/usr/bin/python3
for idx in range(ord('z'), ord('a')-1, -1):
    print('{:c}'.format(idx) if idx % 2 == 0 else chr(idx-32), end='')
