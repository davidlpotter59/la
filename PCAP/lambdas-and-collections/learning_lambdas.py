def square(num):
    return num * num

print(square(2))

square_lambda = lambda num: num * num 
print(f'square_lamba(4) = {square_lambda(4)}')

assert square(4) == square_lambda(4)

# when are they useful
