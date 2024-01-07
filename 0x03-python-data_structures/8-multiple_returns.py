#!/usr/bin/python3

# convert string to list
# get length of list
# join

def multiple_returns(sentence):
    items = list(sentence)
    length = len(items)

    if sentence == " ":
        fail = (0, None)
        return (fail)
    else:
        success = (length, items[0])
        return (success)
