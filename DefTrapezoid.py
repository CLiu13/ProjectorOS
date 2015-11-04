import turtle

def trapezoid(base1, base2, height, angle):
    turtle.forward(base1)
    turtle.left(angle)
    turtle.forward(height)
    turtle.setheading(0)
    turtle.left(180)
    turtle.forward(base2)
    turtle.goto(0,0)

trapezoid(250, 500, 250, 60) #This is just an example
