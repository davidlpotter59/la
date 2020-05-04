my_list = [1,2,3,4,5]
print(my_list)
print(my_list[::2])

my_list[0]= "David"
my_list.insert(0, "Louis")
print(my_list)

for x in my_list:
    print(x)

my_list.append("Louis")
print(my_list)

my_list.insert(0,"Katharina")
print(my_list)

print("Mukki" in my_list)  # returns False

print("David" in my_list)  # returns True

print("David" not in my_list) # returns False

my_list = [1,5,3,6,2,0,7,8,9]
newList = sorted(my_list)
print(newList)
print(list(reversed(sorted(my_list))))
# Functions and methods available
# += or .append(value)
# insert
#    .insert(index, value)
# .index(3) -- 4 item in the list
# 'david' in myList True or False
# 'david' not in myList  True or False
# 
# sorted(myList)

# matrix

myMatrix =[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

print(myMatrix)
print(len(myMatrix))

print(myMatrix[1][2])

myMatrix =[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,25,16],
]
print(myMatrix[2][3])

myMatrix =[
    [1,2,3,4],
    [5,6,7,8,[99,105,210]],
    [9,10,11,12],
    [13,14,25,16],
]

print(myMatrix)
print(f'Length of myMareix is {len(myMatrix)}')

print(myMatrix[1][4][1])

point = (2,0, 3.0)
print(point)
print(len(point))
point_3d = point + (4.0, 5.0, 7.0)
print(point)
print(len(point_3d))
x, b, c, d, e, f  = point_3d
print(x, b, c, d, e, f)

david = "David"
potter = "Potter"
my_tuple = (david, potter) + point_3d
print(my_tuple)
point_3d = point + (4.4, 5.5, 7.7)
print(my_tuple)

myDict = {'kevin': 61, 'alice' : 29, 'bob' : 80}
print('doug' in myDict)
print("alice" in myDict)