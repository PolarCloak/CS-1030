"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A


"""
# imports
import PySimpleGUI as sg
import os

# static variables

# global variables
row1 = [[sg.Image(key="-IMAGE1-")], [sg.Image(key="-IMAGE2-")], [sg.Image(key="-IMAGE3-")]]
row2 = [[sg.Image(key="-IMAGE4-")], [sg.Image(key="-IMAGE5-")], [sg.Image(key="-IMAGE6-")]]
row3 = [[sg.Image(key="-IMAGE7-")], [sg.Image(key="-IMAGE8-")], [sg.Image(key="-IMAGE9-")]]
layout = [
    [sg.Column(row1)],
    [sg.Column(row2)],
    [sg.Column(row3)]
]
window = sg.Window("Tic Tac Toe", layout)
gameRunning = True


# complete some tasks before the game starts
def pregame():

    return


# game loop
def gameLoop():
    global gameRunning
    while gameRunning:
        # read the window for events
        window.finalize()
        window["-IMAGE1-"].update(filename="images/x.png")
        window["-IMAGE2-"].update(filename="images/o.png")
        window["-IMAGE3-"].update(filename="images/x.png")
        window["-IMAGE4-"].update(filename="images/x.png")
        window["-IMAGE5-"].update(filename="images/x.png")
        window["-IMAGE6-"].update(filename="images/x.png")
        window["-IMAGE7-"].update(filename="images/x.png")
        window["-IMAGE8-"].update(filename="images/x.png")
        window["-IMAGE9-"].update(filename="images/x.png")
        event, values = window.read()
        # if a close window event is made, close the game.
        if event == sg.WIN_CLOSED:
            gameRunning = False
            break
        # otherwise we continue with our game.


    return


# run code starting from here
def main():
    pregame()
    gameLoop()
    return


main()
