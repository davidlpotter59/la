#!/usr/bin/env python3.8

# ages = {'Keith': 30, 'Levi': 25, 'John': 20}
# age = ages['Kevin']
# print(ages * 2)

# val = 1 or '2'
# val *= 3
# print(val)

# names = ['Alice', 'Bob', 'Lance', 'Mike']
# names[:3]

# ages = {'Keith': 30, 'Levi': 25, 'John': 20}
# del ages['Keith']

# print(ages)

# for num in range(10):
#     print(num)
#     if num % 2 == 0:
#         continue
#     else:
#         break

# def add_five(num1, num2=5):
#     num1 + num2
# print(add_five(1, 2))

# num = 5
# message = 'Hello'
# print(message, num)

# num = 12
# num2 = num
# num = num + 1
# num2 = num2 / 2
# print(num2)

# names = ['Alice', 'Lance', 'Bob', 'Mike']
# all_names = names
# names.append('Brock')
# print(sorted(all_names))

# for num in range(1, 10, 2):
#     if num % 3:
#         print(num)

# def double_values(list1):
#     doubles = []
#     for num in list1:
#         doubles.append(str(num * 2))
#     return doubles

# first_list = [1, 2, 3, 4]
# print(" ".join(double_values(first_list)))

# num = 10
# if num > 20 or num >= 10:
#     print("First")
# elif num <= 10:
#     print("Second")
# else:
#     print("Third")

# def add_five(num1, num2=5):
#     return num1 + 5
# print(add_five(1, 2))

# names = ['Alice', 'Bob', 'Lance', 'Mike']
# names.del('Bob')
# This one names.remove('Bob')
# This one names[1:2] = []
# print(names)

# def fizz(num):
#     if num % 3 == 0 and num % 5 == 0:
#       return 'FizzBuzz'
#     elif num % 3 == 0:
#       return 'Fizz'
#     elif num % 5 == 0:
#       return 'Buzz'
#     else:
#       return num

# fizz(14)

# print("1600 Pennsylvania Ave NW", "Washington", "DC", sep=', ')

# num = 10
# if num > 20 or num > 10:
#     print("First")
# elif num < 10:
#     print("Second")
# else:
#     print("Third")

# names = ['Alice', 'Bob', 'Lance', 'Mike']
# # names.insert(2, 'Jimmy')
# names[2] = 'Jimmy'
# print(names)

# num = 1
# while num <= 6:
#     if num % 3 == 0:
#         print(num)
#     num = num + 1

# w = "la"
# print(w * 4)

# letter = 'a'
# if letter < 'b':
#     print("First")
# if letter == 'b' or letter > 'c':
#     print("Second")
# elif letter <= 'a':
#     print("Third")
# else:
#     print("Fourth")

# def hello(name, salutation):
#     print(salutation, name, sep=", ")

# hello(salutation="Howdy", name="Oscar")

# num = input("Enter a float value: ")
# new_num = num // 100
# print(new_num)

# values = ['Kevin Bacon', 60, '555-555-5555', False]
# val = not values[-1]
# print(val)

# names = ['Alice', 'Bob', 'Lance', 'Mike']
# print(names[:3])

# num = 1
# while num <= 6:
#     if num % 3 == 0:
#         print(num)

# num1 = 15
# num2 = num1
# num1 *= 2
# print(num2)

# def fib(n):
#     a, b = 0, 1
#     for _ in range(1, n):
#         a, b = b, a + b
#         yield a
# fib_gen = fib()
# print(fib_gen)

# pair1 = ('a', 'b', 'c')
# pair2 = ('d', 'e', 'f')
# index = 0

# while index < len(pair1):
#     for item in pair2:
#         print(pair2[index], item)
#     index += 1

# values = ['Kevin Bacon', 60, '555-555-5555', False]
# val = not values[1]
# print(val)

# num = 15.1
# num2 = num / 4
# num2 //= 2
# num2 + 1
# print(num2)

# def fizz(num):
#     if num % 3 == 0 and num % 5 == 0:
#       return 'FizzBuzz'
#     elif num % 3 == 0:
#       return 'Fizz'
#     elif num % 5 == 0:
#       return 'Buzz'
#     else:
#       return num

# fizz(14)

# def fib(n):
#     a, b = 0, 1
#     for _ in range(1, n):
#         a, b = b, a + b
#         yield a
# fib_gen = fib(4)
# print(fib_gen)

# num = 10
# if num > 20 or num >= 10:
#     print("First")
# elif num <= 10:
#     print("Second")
# else:
#     print("Third")

# names = ['Alice', 'Bob', 'Lance', 'Mike']
# names = names[::-1]
# print(names)

# letter = 'a'
# if letter < 'b':
#     print("First")
# if letter == 'b' or letter > 'c':
#     print("Second")
# elif letter <= 'a':
#     print("Third")
# else:
#     print("Fourth")

# def add_five(num1, num2=5):
#     return num1 + 5
# print(add_five(1, 2))

# letter = 'c'
# if letter < 'e':
#     print("First")
# if letter == 'b' or letter >= 'c':
#     print("Second")
# if letter < 'a':
#     print("Third")
# else:
#     print("Fourth")

# names = ['Alice', 'Bob', 'Lance', 'Mike']
# # names.del('Bob') syntax error
# # names.remove('Bob')
# names[1:2] = []
# print(names)

# print("1600 Pennsylvania Ave NW", "Washington", "DC", sep=', ')
# print("1600 Pennsylvania Ave NW", "Washington", "DC", sep=',')

print()
try:
    num = input("Enter a float value: ")
    new_num = float(num) // 100 * 1.0
    print(new_num)
except Exception as e:
    print()
    print(f'Error in input : {e}')
# myNum = input("Enter a value ")
print('''asdasdada
sadasdwr
dytryituyur''')
