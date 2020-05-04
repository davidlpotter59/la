# print(6 // 3)
# print(6 // 3.)
# print(6. // 3)
# print(6. // 3.)

# print(6 // 4)
# print(6. // 4)
# print(6 % 4)

# print(-6 // 4)
# print(6. // -4)

# print(2 + 3 * 5)

# print(9 % 6 % 2)

# print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

# a = 2 * 13
# b = (25 % 13) + 100
# c = b / a
# d = c // 2
# e = 5 * d
# print(e)

# print(2 * 3 % 5)
# a = 2 * 3
# b = a % 5
# print(b)

# print(15 - 1 * (5 * (1 + 2)))

# print((2 ** 4), (2 * 4.), (2 * 4))

# print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

# var1 = 1.0
# print(id(var1))
# var1 = var1 + 1
# print(id(var1))

# anything = int(input("Enter a number: "))
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# print("hello" * 0)
# a = float(input("Enter first value"))
# b = float(input("Enter second value"))

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print("\nThat's all, folks!")

# x = int(input())
# y = int(input())
# x = x //y
# x = y // x
# # y = y % x
# print(y)
# print(0)

# x = 1 / 2 + 3 // 3 + 4 ** 2
# print(x)

# x = int(input())
# y = int(input())

# n = int(input("Enter your number "))
# print(n < 100)
# print(n >= 100)

# myplant = input("What plant? ")
# plant = "Spathiphyllum"

# if myplant == plant.upper():
#     print("Yes - Spathiphyllum is the best plan ever")
# elif myplant == plant:
#     print("No, I want a big Spathiphyllum")
# else:
#     print("Spathiphyllum not {0}".format(myplant))

# step 1
# beatles =[]
# print("Step 1:", beatles)

# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")

# # step 2
# print("Step 2:", beatles)

# for _ in range(2):
#     newName = input("Enter New name: ")
#     beatles.append(newName)

# print(beatles)
# del beatles[3]
# del beatles[3]

# print(beatles)

# beatles.insert(0, "Ringo")
# print(beatles)

# myList = [8, 10, 6, 2, 4] # list to sort

# for i in range(len(myList) - 1): # we need (5 - 1) comparisons
#     if myList[i] > myList[i + 1]: # compare adjacent elements
#         myList[i], myList[i + 1] = myList[i + 1], myList[i] # if we end up here it means that we have to swap the elements

# myList = [8, 10, 6, 2, 4] # list to sort
# swapped = True # it's a little fake - we need it to enter the while loop

# while swapped:
#     swapped = False # no swaps so far
#     for i in range(len(myList) - 1):
#         if myList[i] > myList[i + 1]:
#             swapped = True # swap occured!
#             myList[i], myList[i + 1] = myList[i + 1], myList[i]

# print(myList)

# myList = [8, 10, 6, 2, 4]
# myList.sort()
# print(myList)
# print(sorted(myList))

# list1 = ["Howdy"]
# list2 = list1
# list1[0]="Goog-bye"
# print(list2)

# myList = [10, 8, 6, 4, 2]
# newList = myList[1:-1]
# print(newList)

# myList = [10, 8, 6, 4, 2]
# newList = myList[:]
# print(newList)

# for i in range(-1, 1):
#     print("#")

# z = 10
# y = 0
# x = z > y or z == y
# print(x)

# lst = [3, 1, -1]
# lst[-1] =lst[-2]
# print(lst)

# vals = [0, 1, 2]
# vals[0], vals[1] = vals[1], vals[2]
# print(vals)

# nums = []
# vals = nums[:]
# print(vals.append(1))

# print(len(nums))
# print(len(vals))

# lst = [0, 1, 2, 3]

# x = 1
# for elem in lst:
#     x *= elem
# print(x)

# lst = [1 for i in range(-1, 2)]
# print(lst)

# for i in range(1):
#     print("#")
# else:
#     print("#")

# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
# print(c + d + e)

# i = 1
# while i <=3:
#     i +=2
#     print("*")

# vals = [0, 1, 2]
# vals.insert(0, 1)
# del vals[1]
# print(vals)

# lst = [3, 1, -2]
# print(lst[lst[-1]])

# lst = [1,2,3]
# for v in range(len(lst)):
#     lst.insert(1, lst[v])

# print(lst)

# i = 0
# while i <=5:
#     if i % 2 == 0:
#         break
#     print("*")

# z = 10
# y = 0

# x = y and z > y or z and 2 < y
# print(x)

# vals = [0, 1, 2]
# vals[0], vals[2] = vals[2], vals[0]
# print(vals)

# lst = [[0, 1, 2, 3] for i in range(2)]
# print(lst[2][0])

# nums = [1, 2, 3]
# vals = nums[-1:-2]
# print(vals, nums)

# nums = [1, 2, 3]
# vals = nums
# del vals[1:2]
# print(vals)

# var = 1
# while var < 10:
#     print("#")
#     var = var << 1

# lst1 = [1, 2, 3]
# lst2 = []

# for v in lst1:
#     lst2.insert(0,v)
# print(lst2)

# t = [[ 3 - i for i in range (3) for j in range (3)]]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)

# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0;
      
# # print("Enter a value: ")
# a = int(input())

# print("Enter a value: ")
# b = int(input())

# print("Enter a value: ")
# c = int(input())

# def message():
#     print("Enter a Value: ")
#     myVal = int(input())
#     return myVal
    
# a = message()
# b = message()
# c = message()

# print(a, b, c)


# def message(number):
#     print("Enter a number:", number)

# message(1)

# def factorialFun(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * factorialFun(n - 1)

# a = factorialFun(8)
# print(a)

# myTuple = (1, 10, 100, 1000)

# print(myTuple[0])
# print(myTuple[-1])
# print(myTuple[1:])
# print(myTuple[:-2])

# for elem in myTuple:
#     print(elem)

# myTuple = (1, 10, 100)

# t1 = myTuple + (1000, 10000)
# t2 = myTuple * 3

# print(len(t2))
# print(t1)
# print(t2)
# print(10 in myTuple)
# print(-10 not in myTuple)

# from list1 import myDict


# dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
# phoneNumbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
# emptyDictionary = {}


# for x,y in dict.items():
#     print(x,y)

# for x in dict.keys():
#     print(x)

# for x in sorted(dict.keys()):
#     print("sorted value of the dict is {}".format(x))


# for x in dict.values():
#     print(x)

# print(len(dict))
# print(len(phoneNumbers))

# words = ['cat', 'lion', 'horse']

# for word in words:
#     if word in dict:
#         print(word, "->", dict[word])
#     else:
#         print(word, "is not in dictionary")

# myDict = {}
# myDict.update(dict)
# myDict.update(phoneNumbers)
# print(myDict)
# myDict.popitem()
# print(myDict)
# print(myDict['cat'])

# schoolClass = {}

# while True:
#     name = input("Enter the student's name (or type exit to stop): ")
#     if name == 'exit':
#         break
    
#     score = int(input("Enter the student's score (0-10): "))
    
#     if name in schoolClass:
#         schoolClass[name] += (score,)
#     else:
#         schoolClass[name] = (score,)
        
# for name in sorted(schoolClass.keys()):
#     sum = 0
#     counter = 0
#     for score in schoolClass[name]:
#         sum += score
#         counter += 1
#     print(name, ":", sum / counter)

# myTup = (1, 2, 3)
# print(myTup[2])

# tup = 1, 2, 3
# a, b, c = tup

# print(a * b * c)

# l = ["car", "Ford", "flower", "Tulip"]

# t = tuple(l) # your code
# print(t)

# colors = (("green", "#008000"), ("blue", "#0000FF"))

# colDict = dict(colors)

# print(colDict)

myDict = {"A":1, "B":2}
copyMyDict = myDict.copy()
myDict.clear()

print(copyMyDict)

print()