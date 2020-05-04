#!/usr/bin/env python38

def myFunc1():
    x = 0
    for x in range(1,11):

        if x == 6:
            print("Passing")
            pass
        if x == 7:
            print("continue")
            continue
        if x == 9:
            break
        print(x)

def myfunc2():
    for x in range(1,11):
        break 

myFunc1()