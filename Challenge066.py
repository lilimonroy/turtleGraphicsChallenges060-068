# ----------* CHALLENGE 66 *----------
# Draw an octagon that uses a different colour (randomly selected from a list of six possible colours) for each line.

import turtle
import random

colour = random.choice(["red","blue","yellow","green","pink","orange"])

turtle.pensize(4)

for i in range (0,8):
    turtle.color(colour)
    turtle.forward(50)
    turtle.left(45)

turtle.exitonclick()