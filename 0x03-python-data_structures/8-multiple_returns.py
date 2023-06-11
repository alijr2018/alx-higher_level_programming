#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    i = sentence
    if length <= 0:
        return (None)
    else:
        return (length, i)
