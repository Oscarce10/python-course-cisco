#!/usr/bin/env python3

""" module.py - an example of Python module"""

__counter = 0

def suml(list):
    global __counter
    __counter += 1
    sum = 0
    for e in list:
        sum += e
    return sum

def prodl(list):
    global __counter
    __counter += 1
    prod = 1
    for e in list:
        prod *= e

    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you")
    l = [i + 1 for i in range(5)]
    print(suml(l) == 15)
    print(prodl(l) == 120)
else:
    print("I am currently the module!")