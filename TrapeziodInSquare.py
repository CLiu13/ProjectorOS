import turtle
#Screensize#
turtle.screensize(1200,1200)
"""This sets the screensize to 1200 pixels long and 1200 pixels wide."""
#Square#
turtle.forward(500) #Turtle moves 500 pixels eastward
turtle.right(90)    #Turtle turns 90 degrees clockwise
turtle.forward(500) #Turtle moves 500 pixels south (because of change in direction
turtle.right(90)    #Turtle turns 90 degrees clockwise again
turtle.forward(500) #Turtle moves 500 pixels west becuase of change in direction
turtle.right(90)    #Turtle turns 90 degrees clockwise
turtle.forward(500) #Turtle moves 500 pixels north becuase of change in direction
turtle.right(90)    #Turtle turns 90 degrees clockwise
#Trapezoid#
turtle.setpos(0,0)
#This sets the turtle's position back to the origin (where it started).
#Note that this draws a line connecting the two points as well.
turtle.goto(125,-500)
#Moves the turtle to the point (125, -500) while drawing a line connecting the two
turtle.setheading(0)
"""This resets the direction the turtle points. So when used, this sets the
turtle's direction to face eastwards again."""
turtle.forward(250)
#Makes the turtle move forward 250 pixels
turtle.goto(500,0)
#Moves the turtle to the point (500,0) drawing a line simultaneously

