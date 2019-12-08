prompt = int(input("What how many values should we process? "))

for x in range(1, prompt + 1):
    if x % 3 == 0 and x % 5 == 0:
        print("{0} Fizz Buzz".format(x))
    elif x % 3 == 0:
        print("{0} Fizz".format(x))
    elif x % 5 == 0:
        print("{0} Buzz".format(x))
    else:
        print("{0} else".format(x))