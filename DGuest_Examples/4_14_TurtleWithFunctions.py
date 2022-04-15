"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A

tortles
"""
# imports
import turtle


# draws a line from (x1,y1) to (x2,y2)
def drawline(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


# write a text at the specified location
def writeText(x, y, message):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(message)


# draw a point at the specified location
def drawPoint(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()


# draw circle with specified radius
def drawCircle(x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)


# draw a rectangle at x,y with specified width and height
def drawRectangle(x, y, width, height):
    turtle.penup()
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)


# start of all of the methods
def main():
    turtle.showturtle()

    drawline(-50, -50, 50, 50)
    drawRectangle(-100, -100, 100, 200)
    writeText(100, 20, "Testing tooortles")
    drawPoint(0, 0, 60, "red")
    drawCircle(200, 50, 30)

    turtle.hideturtle()
    turtle.done()
    return


main()
