#!/usr/bin/env python3.8
# name = input("What is your name? ")
# color = input("What is your favorite color? ")
# age = int(input("How old are you today? "))

# print(name)
# print("is " + str(age) + " years old")
# print("and loves the color " + color + ".")

# fahrenheit to celsius  
# (°F - 32) x .5556
# 
# try:
#     myTemp = float(input("Enter the Temperature in Fahrenheit: "))
#     myCelsius = (myTemp - 32) * .5556
#     print(f'The current temp in celsius is {round(myCelsius,2)}')
# except Exception as e:
#     print(f"You have an error in your input which is \"{e}\"")

# if 1 == 2:
#     print('one = one')
# else:
#     print('1 <> 2')

# colors = ['blue', 'green', 'red', 'purple']
# for color in colors:
#     if 'blue' in color:
#         print(color)

def myFunc(num=10):
    for x in range(1,num + 1):
        yield x

# a = list(myFunc(50))
a = myFunc(50)
print(a)