name = input("Enter your name: ").title()
color = input("What is your favorite color? ").title()
age = int(input("What is your age? "))

nameSplit = name.split()
print(nameSplit)

outStr = f'Hello, my name is {name}.',  f'I go by {nameSplit[1]}.',  f'My favorite color is {color}.',  f'I am {age} years old.'
print(f'{outStr}', end="\t")
print(f'Hello, my name is {name}.', f'I go by {nameSplit[1]}.',  f'My favorite color is {color}.',  f'I am {age} years old.', sep="\t")

outStr = f'Hello, my name is {name}.  I go by {nameSplit[0]}. My favorite color is {color}.  I am {age} years old.'
print(outStr)