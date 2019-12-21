y = 5

def set_x(y):
    print(f"Inner Y {y}")
    x = y
    y = x
    global a 
    a = x + y
    

set_x(10)

print(f'Outer Y {y}')
print(f'a is {a}')