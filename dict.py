weights = dict(kevin=160, bob=240, kayla=135)
weights2 = {"kevin": 160, "bob": 240, "kayla": 135}

colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla','red')])

print(colors)
print(weights)
print(weights2)

# to add to a dictionary
colors['davep'] = "orange"

print(colors)

weights2['davep'] = 220
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

age = {'kevein': 61, 'bob': 79}
print(age.keys())
print(list(age.keys()))
print(age.values())
print(list(age.values()))
print(age.items())