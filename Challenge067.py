# ----------* CHALLENGE 67 *----------
# Create the following pattern:

import turtle

for i in range(0,10):
    turtle.right(36)
    for j in range(0,8):
        turtle.forward(50)
        turtle.left(45)
    
turtle.exitonclick()