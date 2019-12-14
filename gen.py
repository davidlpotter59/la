def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step

def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

generator = gen_range(10)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))  # this triggers the error StopIteration

# converting a generator to a list
# print(list(generator))

fib=gen_fib()
# print(next(fib))
# print(next(fib))
# print(next(fib))

print([next(fib) for _ in range(50)][-1])

# lab
def char_range(start, stop, step=1):
    start_code = ord(start)
    stop_code  = ord(stop)
    for value in range(start_code, stop_code + 1, step):
        yield chr(value)

from inspect import isgeneratorfunction

assert isgeneratorfunction(
    char_range
), f"Expected char_range to be a generator but was not"