import turtle
import tkinter
import pygame
import os
wn = turtle.Screen()
import DrawBorder
def drawMenu():    
    wn = turtle.Screen()
    wn.bgpic("Game_Over.gif")
    wn.bgcolor("blue")
    FONTSIZE = 80
    FONT = ("Game Over", FONTSIZE, "bold")
    turtle.penup()
    turtle.color("blue")

    turtle.hideturtle()
    turtle.setpos(0, 0)
    turtle.write("PLAY AGAIN", align="center", font=FONT)
    turtle.setpos(0, -50)
    turtle.write("EXIT", align="center", font=FONT)
    turtle.setpos(0, -100)
    turtle.write("MENU", align="center", font=FONT)

def GameOver():
    t = turtle.Turtle()
    s = turtle.Screen()
    def playAgain(x, y):
        turtle.clearscreen()
        if y >= 10 and y < 40 and x > -60 and x < 60:
            import Game
        elif y <= -20 and y > -40 and x > -40 and x < 45:
            quit()
        elif y < -70 and y > -90 and x > -80 and x < 80:
            import menu
    turtle.listen()
    turtle.onscreenclick(playAgain,1,True)
    s.done()
drawMenu()
GameOver()
wn.mainloop()
