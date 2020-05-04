import turtle


def mySquare(num1, num2):
    turtle.forward(num1)
    turtle.right(num2)

def mySquare2(num1, num2):
    turtle.right(num1)
    turtle.forward(num2)

my_box = [
    [100, 90], 
    [100, 90],
    [100, 90],
    [100, 0],
]

for x,y in my_box:
    mySquare(x,y)

mySquare2(300,300)