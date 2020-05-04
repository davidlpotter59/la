myStr="David L. Potter"
myName  = myStr.split(maxsplit=-1)
name1 = {}
counter = int(0)

for name in myName:
    if "." not in name:
	    print(name, end=" ")
	    if counter == 0:
		    name1("first", name)
	    else:
		    name1("last", name)
    counter =+ 1

print(f'\n{name1}')