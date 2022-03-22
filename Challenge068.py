# ----------* CHALLENGE 68 *----------
# Draw a pattern that will change each time the
# program is run. Use the random function to pick
# the number of lines, the length of each line and
# the angle of each turn.

import turtle
import random

lines = random.randint(0,12)
lenght = random.randint(30,100)
angle = random.randint(45,270)

turtle.pensize(3)
for i in range(0,lines):
    turtle.right(angle)
    for j in range(0,8):
        turtle.forward(lenght)
        turtle.left(45)
    
turtle.exitonclick()