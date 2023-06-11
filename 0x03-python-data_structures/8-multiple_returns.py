#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if length <= 0:
        i = None
    else:
        i = sentence[0]
    return (length, i)
