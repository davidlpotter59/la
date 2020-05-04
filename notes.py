# Strings

# to repeat a string X # of times

"HA " * 5

# string methods

"my_string".capitalize()

# converting a number into binary
# 
#  convert 15 into binary
# 
#  15 / 2 = 7 - remainder 1
#   7 / 2 = 3 - remaninder 1
#   3 / 2 = 1 - remainder 1
#   1 / 2 =0     remainder 1

# 15 decimal = 1111 binary
print("ob1111")

True == False

a = 0b1001
b = 0b1100

# one has to be True (AND)
bin(a | b)
# 0b1101 results

# both has to be True (OR)
bin(a & b)
#  0b1000 results

# only one can be True (XOR)
print(bin(a ^ b))
#  0b0101 results 