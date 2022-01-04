#!/usr/bin/python3
def multiple_returns(sentence):
    idx = len(sentence)
    first = sentence[0] if idx > 0 else None

    return(idx, first)
