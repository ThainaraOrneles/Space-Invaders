import turtle
import tkinter
import os
import sys
wn = turtle.Screen()
wn.bgcolor("blue")
wn.bgpic("Background.gif")
# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()
def drawMenu():
    # Draw border 
    #import DrawBorder 
    FONTSIZE = 100
    FONT = ("Game Over", FONTSIZE, "bold")
    turtle.hideturtle()
    turtle.color("blue")
    turtle.penup()
    turtle.setpos(0, FONTSIZE*2)
    turtle.write("SPACE INVADERS", align="center", font=FONT)

    FONT = ("Game Over", FONTSIZE-30, "bold")

    turtle.setpos(0, 0)
    turtle.write("START", align="center", font=FONT)
    turtle.setpos(0, -50)
    turtle.write("EXIT", align="center", font=FONT)
    turtle.setpos(0, -100)
    turtle.write("CREDITS", align="center", font=FONT)
    
def MainMenu():    
    s = turtle.Screen()
    def menu(x, y):
        turtle.clearscreen()
        if y >= 10 and y < 40 and x > -60 and x < 60:
            import Game
        elif y <= -20 and y > -40 and x > -40 and x < 35:
            quit() 
        elif y < -70 and y > -90 and x > -80 and x < 80:
            import Creditos
    turtle.listen()        
    turtle.onscreenclick(menu,1,True)
    turtle.done()
drawMenu()
MainMenu()
wn.mainloop()
