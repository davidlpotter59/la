from functools import reduce

domain = [1, 2, 3, 4, 5,]

# f(x) = x * 2

# map
our_range = map(lambda num: num * 2, domain)
print(list(our_range))

# filter
evens = filter(lambda num: num % 2 == 0, domain)
print(list(evens))

# reduce - this example sums all of the items in the list (domain)
# the 0 at the end is the starting point - kind of the default
the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(the_sum)

words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'Dog', 'dave', 'dig']
print(sorted(words))

print(sorted(words, key=lambda s: s.lower(), reverse=True))

# not using lambdas and using methods - this is the same as the above line
print("Sorting with a method")
words.sort(key=str.lower, reverse=True)
print(words)