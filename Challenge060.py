#----------* CHALLENGE 60 *----------
#Draw a square.

import turtle

scr = turtle.Screen()
scr = turtle.bgcolor("black")

turtle.shape("turtle")

for i in range(0,4):
    turtle.forward(90)
    turtle.right(90)
turtle.exitonclick()