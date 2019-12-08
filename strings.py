print(chr(8482))
print(ord('™'))

for x in range(0,256):
    print(f'This is the output for this char {x}  ---- {chr(x)}')

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
print(d.isascii())
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

