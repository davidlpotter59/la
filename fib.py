# Recursion
def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n - 2) + fib(n - 1)

item_to_calculate = int(input("Enter your number please "))

print(fib(item_to_calculate))