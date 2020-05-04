# names = ['Alice', 'Lance', 'Bob', 'Mike']
# all_names = names
# names.append('Brock')
# print(sorted(all_names))

# num1 = 15
# num2 = num1
# num1 *= 2
# print(num2)

# val = 1 or '2'
# val *= 3
# print(val)

# def add_five(num1, num2=5):
#     return num1 + 5
# print(add_five(1, 2))

# for num in range(1, 10, 2):
#     if num % 3:
#         print(num)

# print(3 ** 3)

# names = ['Alice', 'Bob', 'Lance', 'Mike']
# print(names[:3])

# print("1600 Pennsylvania Ave NW", "Washington", "DC", sep=',')

# num = 12
# if num <= 15:
#     print("Less than 15")
# elif num >= 15:
#     print("Greater than 15")
# else:
#     print("Less than 15")

# num1 = 30
# num2 = 15
# num1 // 2
# print(num1 // 2)
# print(num2 == num1)

# values = ['Kevin Bacon', 60, '555-555-5555', False]
# # Code goes here
# print(val)

# def fib(n):
#     a, b = 0, 1
#     for _ in range(1, n):
#         a, b = b, a + b
#         yield a
# fib_gen = fib()
# print(fib_gen)

# for num in range(10):
#     print(num)
#     if num % 2 == 0:
#         continue
#     else:
#         break

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

# num = input("Enter a float value: ")
# new_num = float(num) // 100 * 1.0
# print(new_num)

# w = "la"
# print(w * 4)

# def fib(n):
#     a, b = 0, 1
#     for _ in range(1, n):
#         a, b = b, a + b
#         yield a
# fib_gen = fib(4)
# print(fib_gen)

# num = 1
# while num <= 6:
#     if num % 3 == 0:
#         print(num)

# ages = {'Keith': 30, 'Levi': 25, 'John': 20}
# output = [str(value) for value in ages.values()]
# print(output)

# names = ['Alice', 'Lance', 'Bob', 'Mike']
# all_names = names
# names.append('Brock')
# print(sorted(all_names))
# print(all_names)

# num = 10
# if num > 20 or num > 10:
#     print("First")
# elif num < 10:
#     print("Second")
# else:
#     print("Third")

# def fizz(num):
#     if num % 3 == 0 and num % 5 == 0:
#       return 'FizzBuzz'
#     elif num % 3 == 0:
#       return 'Fizz'
#     elif num % 5 == 0:
#       return 'Buzz'
#     else:
#       return num

# print(fizz(14))

# def fib(n):
#     a, b = 0, 1
#     for _ in range(1, n):
#         a, b = b, a + b
#         yield a
# fib_gen = fib(4)
# print(fib_gen)

# pair1 = ('a', 'b', 'c')
# pair2 = ('d', 'e', 'f')
# index = 0

# while index < len(pair1):
#     for item in pair2:
#         print(pair2[index], item)
#     index += 1

# val = 1 or '2'
# val *= 3
# print(val)

# values = ['Kevin Bacon', 60, '555-555-5555', False]
# val = not values[1]
# print(val)

# ages = {'Keith': 30, 'Levi': 25, 'John': 20}
# age = ages.get('Kevin')
# print(age)

# names = ['Alice', 'Bob', 'Lance', 'Mike']
# names.remove('Bob')
# print(names)
# names = ['Alice', 'Bob', 'Lance', 'Mike']
# all_names = names
# names.remove('Bob')
# all_names + ['Kevin']
# print(all_names)

# names = ['Alice', 'Bob', 'Lance', 'Mike']
# # names[2] = 'Jimmy'
# # names.insert(2, 'Jimmy')
# names.set(2, 'Jimmy')
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

# def double_values(list1):
#     doubles = []
#     for num in list1:
#         doubles.append(str(num * 2))
#     return doubles

# first_list = [1, 2, 3, 4]
# print(" ".join(double_values(first_list)))

colors =['red', 'blue', 'green', 'yellow', 'orange']

uppercase_colors = [color.upper() for color in colors]
print(uppercase_colors)

warm_colors=[]
for color in colors:
    if color in ['red', 'orange', 'yellow']:
        warm_colors.append(color)

# list comprehension way

warm_colors = [color for color in colors if color in ['red', 'orange', 'yellow']]
print(warm_colors)

title_colors = [color.title() for color in colors]
print(title_colors)

myDict={"David": 55, "Hailey": 46, "Bob": 99, "Frank": 40,}
myDict_out = [age for age in myDict.values()]
print(myDict_out)

myDict_out = [name for name in myDict.keys()]
print(myDict_out)

myDict_out = [list(myValues) for myValues in myDict.items()]
print(myDict_out)
print(len(myDict_out))
print(myDict_out[3][0])

for x in range(len(myDict_out)):
    print(myDict_out[x][0])
    print(myDict_out[x][1])