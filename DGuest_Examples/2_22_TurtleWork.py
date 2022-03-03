"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A

Playing with turtle
"""
import turtle as t

running = True

pastPos = []


def up():
    t.seth(90)


def right():
    t.seth(0)


def down():
    t.seth(270)


def left():
    t.seth(180)

def quit():
    global running
    running = False
    print("Quitting")


def turtleLoop():
    while running:
        t.forward(1.5)

    for x in range(len(pastPos)):
        if t.pos() == pastPos[x]:
            quit(0)
    pastPos.append(t.pos())


def main():
    t.showturtle()
    t.listen()
    t.speed(10)
    t.onkeypress(left, "a")
    t.onkeypress(up, "w")
    t.onkeypress(right, "d")
    t.onkeypress(down, "s")
    t.onkeypress(quit, "esc")
    turtleLoop()

    t.done()


main()
