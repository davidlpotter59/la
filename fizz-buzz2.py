#!/usr/bin/env python38


# try:
#     loops = int(input("Please enter and integer to check "))
# except Exception as e:
#     loops = 1
#     print("Whoops, something went wrong.  \n\nYour error was: {0}.  \n\nPlease try again!".format(e))

# for counter in range(1, loops + 1):
#     if counter % 3 == 0 and  counter %5 == 0:
#         print("Fizz Buzz ", end = "")
#     elif counter % 3 == 0:
#         print("Fizz ", end = "")
#     elif counter % 5 == 0:
#         print("Buzz ", end = "")

#     print(counter)

myDict = {'david': '55', 'john': 70, 'bob': 53}
print(myDict)

for x,y in myDict.items():
    print(x,y)

myTuple = tuple(myDict.items())
print(myTuple)

for x,y  in myTuple:
    print('My name is {0} and I am {1} years old'.format(x,y))