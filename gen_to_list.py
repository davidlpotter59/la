#!/usr/bin/env python3.8

def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step

generator = gen_range(10)

# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(list(generator))

def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

fib = gen_fib()
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

print([next(fib) for _ in range(50)][-1])

a = 1.0 - 0.001
print(a)