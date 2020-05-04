Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> ord('\u2122')
8482
>>> chr(8482)
'™'
>>> tm = chr(8482)
>>> tm
'™'
>>> tm = chr(ord(\u2122))
SyntaxError: unexpected character after line continuation character
>>> tm = chr(ord('\u2122'))
>>> tm
'™'
>>> 

>>> print(f'Trade mark looks like {chr(ord('\u2122')}')
SyntaxError: unexpected character after line continuation character
>>> print(f'Trade mark looks like {chr(ord('\u2122'))}')
SyntaxError: unexpected character after line continuation character
>>> print(f'Trade mark looks like {chr(ord('\u2122'))}')
SyntaxError: unexpected character after line continuation character
>>> print(f"Trade mark looks like {chr(ord('\u2122'))}")
SyntaxError: f-string expression part cannot include a backslash
>>> print(f'Trade mark looks like {chr(ord("\u2122"))}')
SyntaxError: f-string expression part cannot include a backslash
>>> print('Trade mark looks like {0}'.format(chr(ord("\u2122")))

	  
KeyboardInterrupt
>>> print('Trade mark looks like {0}'.format(chr(ord('\u2122')))
	  
KeyboardInterrupt
>>> print('Trade mark looks like {0}'.format(tm)
	  
KeyboardInterrupt
>>> print('Trade mark looks like {0}'.format(tm))
	  
Trade mark looks like ™
>>> 
	  
>>> 
	  
>>> myString="This is a string".lower()
	  
>>> mystring
	  
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    mystring
NameError: name 'mystring' is not defined
>>> myString
	  
'this is a string'
>>> myString="This is a string".upper()
	  
>>> myString
	  
'THIS IS A STRING'
>>> myString="This is a string".title()
	  
>>> myString="This is a string".upper()
	  
>>> myString="This is a string".title()
	  
>>> myString
	  
'This Is A String'
>>> myString="This is a string".swapcase()
	  
>>> myString
	  
'tHIS IS A STRING'
>>> myString.isalpha()
	  
False
>>> myString.isascii()
	  
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    myString.isascii()
AttributeError: 'str' object has no attribute 'isascii'
>>> myString.isnumberic()
	  
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    myString.isnumberic()
AttributeError: 'str' object has no attribute 'isnumberic'
>>> myString.isnumberic()
	  
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    myString.isnumberic()
AttributeError: 'str' object has no attribute 'isnumberic'
>>> dir(myString)
	  
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> myString.isupper()
	  
False
>>> myString.islower()
	  
False
>>> myString.istitle()
	  
False
>>> myString.isswapcase()
	  
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    myString.isswapcase()
AttributeError: 'str' object has no attribute 'isswapcase'
>>> myString.isidentifier()
	  
False
>>> " ".isspace()
	  
True
>>> " x x x x".isspace()
	  
False
>>> "1".isnumeric()
	  
True
>>> "1.0".isnumeric()
	  
False
>>> "1.0".isdecimal()
	  
False
>>> "1.0".isdigit()
	  
False
>>> "1".isdigit()
	  
True
>>> "1".startswith('1')
	  
True
>>> " x x x x".isalpha()
	  
False
>>> "xxxx".isalpha()
	  
True
>>> "David Potter".isalpha()
	  
False
>>> "David Potter".isidentifier()
	  
False
>>> myString.isidentifier()
	  
False
>>> "David_Potter".isidentifier()
	  
True
>>> "David_Potter".isprintable()
	  
True
>>> "David_Potter\n".isprintable()
	  
False
>>> 

>>> url = "https://www.google.com/users/davep"
	  
>>> users = url.split('/')[-1]
	  
>>> users
	  
'davep'
>>> 
