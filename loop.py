#!/usr/bin/env python3.8

def myFunc():

    counter = 1

    while counter <= 100:
        print("Counter is {0}".format(counter))
        counter += 1

    return counter

def myFunc2(num=10):
    for x in range(1,num + 1):
        print("Num is now {0}".format(x))
    return x

def varArgs(*args):
    for x in args:
        print(x, sep=", ", end=" ")

    return x

def fizzBuzz(num=60):

    for x in range(1,num + 1):
        if x % 3 == 0 and x % 5 == 0:
            print("X is {0} and the mod is {1} & {2} - FizzBuzz".format(x, x % 3, x % 5))
        elif x % 3 == 0:
            print("X is {0} and the mod is {1} - Fizz".format(x, x % 3))
        elif x % 5 == 0:
            print("X is {0} and the mod is {1} - Buzz".format(x, x % 5))
        else:
            print("X is {0} and the mod 3 is {1} and the mod 5 is {2}".format(x, x % 3, x % 5))

a = fizzBuzz(100)
# a = myFunc()
print(a)
# a = myFunc2(50)
# print(a)

# a = varArgs('david','louis','potter','Katharina','Mukki')
# print()
# print(a)

