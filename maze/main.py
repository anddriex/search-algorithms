# Help the turtle navigate through the maze by using the 
# forward, left, and right commands.  After navigating 
# through the green, blue, and red sections the turtle 
# should exit the maze at the top.

# Modified from www.101computing.net/turtle-maze

import turtle
import maze

fred = turtle.Turtle()
fred.shape("turtle")
fred.color("magenta")
fred.width(2)

fred.penup()
fred.goto(-177, 177)
fred.right(90)
fred.forward(84)
fred.left(90)
fred.forward(28)
fred.right(90)
fred.forward(28)
# fred.left(180)
#fred.pendown()

# Start of maze
# fred.forward(40)

# Add your code here
