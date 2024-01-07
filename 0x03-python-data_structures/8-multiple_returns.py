#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)

    if length == 0:
        fail = (length, None)
        return (fail)
    else:
        success = (length, sentence[0])

    return (success)
