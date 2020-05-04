print(chr(8482))
print(ord('™'))

# for x in range(0,256):
#     print(f'This is the output for this char {x}  ---- {chr(x)}')

print(ord('½'))
d="dave"
print("Today's specials are {0} off.  Today only!".format(chr(189)))

# string methods
print(d.lower())
print(d.upper())
print(d.title())
print(d.capitalize())
#
# .is
# print(d.isascii())
print(d.isupper())

print(d.istitle())
print(d.title().istitle())

# isdecimal
# isnumeric

x = "1"
y="1word1"
z="word"
s="def"

print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())

print(x.isalpha())
print(y.isidentifier()) # y cannot start with a number
print(z.isidentifier())

print(d.isprintable())

# working with collections

phrase = "This is a simple phrase"
words = phrase.split()
print(words)

url = "https://www.google.com/jimmy"

url2 = url.split("/")
print(url2[-1])

# or

print(url.split('/')[-1])

#  join

print(",".join(words))
lines = ["First Line", "Second Line", "Third Line"]
output = "\n".join(lines)
print(output, "\n")

# format
print(f'1. This is the output {output}') # python 3.X only
print('2. This is the output {0}'.format(output)) # python 2.X and 3.X

template = "Hello, my name is {}, and I really enjoy {}.  Have a nice day"
print(template.format('David', 'Python'))

myStr = """This is a multiline string
I hope this actually works.
this is the last line"""

myStr2 = "This is a String.  I did it myself"
print(myStr)

for x in range(len(myStr2)):
    print("myStr2[x] = {0} -- {1} ".format(myStr2[x],ord(myStr2[x])))

# methods on strings
print("String Methods")
print(myStr2.find('I'))
print(myStr2.find('T'))
print(myStr2.upper())
print(myStr2.lower())
print(myStr2.title())
print(myStr2.swapcase())

myStr3 = "This is a \"quote\" inside of a string"
print(myStr3)

myBool = None

if myBool:
    print("True")
else:
    print("False")


# myVar = 6
# print(myVar // 2)
# print(myVar % 2)

# print(myVar.numerator)
# print(myVar.denominator)

# name = input("What is your name? ")
# if len(name) >= 6:
#    print("Your name is long.")
# elif len(name) == 5:
#    print("Your name is 5 characters.")
# elif len(name) >= 4:
#    print("Your name is 4 or more characters.")
# elif len(name) == 1:
#     print("Really, only 1 letter for a name?")
# else:
#    print("Your name is short.")

# print(name.upper())
# print(name.upper()[::-1])

colors = ['red', 'blue', 'orange', 'green', 'yellow']
warm_colors = [color for color in colors if color in ['red', 'orange', 'yellow']]
print(warm_colors)