my_list = [1,2,3,4,5]
print(my_list)
print(my_list[::2])

my_list[0]= "David"
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