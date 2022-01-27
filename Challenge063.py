#----------* CHALLENGE 62 *----------
#Draw three squares in a row with a gap between each. Fill them using three different colours.

import turtle

#Screen
scr = turtle.Screen()

#First Square
turtle.color("blue", "blue")
turtle.begin_fill()
for i in range (0,4):
    turtle.forward(90)
    turtle.right(90)
    #turtle.color("blue", "red")
turtle.end_fill()

#Gap
turtle.penup()
turtle.forward(-100)
turtle.pendown()

#Second Square
turtle.color("red", "red")
turtle.begin_fill()
for i in range (0,4):
    turtle.forward(90)
    turtle.right(90)
    #turtle.color("blue", "red")
turtle.end_fill()

#Gap
turtle.penup()
turtle.forward(-100)
turtle.pendown()

#Third Square
turtle.color("purple", "purple")
turtle.begin_fill()
for i in range (0,4):
    turtle.forward(90)
    turtle.right(90)
    #turtle.color("blue", "red")
turtle.end_fill()

turtle.exitonclick()