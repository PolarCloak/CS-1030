"""
CS10300-20766
ID#700714467
David Guest
Classwork
Due Date: N/A

Making a face with turtle
"""

import turtle

turtle.showturtle()

# outline the face
turtle.penup()
turtle.goto(0, -70)
turtle.pendown()
turtle.circle(70)

# left eye
turtle.penup()
turtle.goto(-30, 20)
turtle.pendown()
turtle.color("blue")
turtle.circle(10)

# right eye
turtle.penup()
turtle.goto(30, 20)
turtle.pendown()
turtle.color("red")
turtle.circle(10)

# mouth
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.color("purple")
turtle.circle(30)

turtle.hideturtle()
turtle.done()
