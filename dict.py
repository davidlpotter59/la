weights = dict(kevin=160, bob=240, kayla=135)
weights2 = {"kevin": 160, "bob": 240, "kayla": 135}

colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla','red')])

print(colors)
print(weights)
print(weights2)

# to add to a dictionary
colors['davep'] = "orange"

print(colors)

weights2['davep'] = 200
weights['davep'] = 220 

print(weights2)

# reassign
weights['kevin']=190

print(weights)

# delete entry
del weights['davep']

print(weights)

print('davep' in weights)
print('davep' in weights2)

#  dictionary methods

# age = {'kevein': 61, 'bob': 79}
# print(age.keys())
# print(list(age.keys()))
# print(age.values())
# print(list(age.values()))
# print(age.items())

myDict={"David": 55, "Hailey": 46, "Bob": 99, "Frank": 40,}
question = input("Enter your name to see if it is in the dictionary: ")

try:
    myDict[question]
except Exception as e:
    if e:
        print("Name {0} not found".format(question))
    else:
        print("Error found was {0}".format(e))
finally:
        print("Your try is over")