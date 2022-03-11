import turtle
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
    FONTSIZE = 100
    FONT = ("Game Over", FONTSIZE, "bold")
    turtle.hideturtle()
    turtle.color("blue")
    turtle.penup()
    turtle.setpos(0, FONTSIZE*2)
    turtle.write("SPACE INVADERS", align="center", font=FONT)

    turtle.setpos(0, 120)
    FONT = ("Game Over", FONTSIZE-60, "bold")
    turtle.write("Criador por:", align="center", font=FONT)

    turtle.setpos(0, 95)
    turtle.write("Mahesh Sawant", align="center", font=FONT)

    turtle.setpos(0, 40)
    turtle.write("Adaptado por:", align="center", font=FONT)

    turtle.setpos(0, 15)
    turtle.write("Thainara Orneles e Ygor Takashi", align="center", font=FONT)

    turtle.setpos(0, -40)
    turtle.write("Professora:", align="center", font=FONT)

    turtle.setpos(0, -65)
    turtle.write("Yorah Bosse", align="center", font=FONT)

    turtle.setpos(0, -120)
    turtle.write("Instituiçao:", align="center", font=FONT)

    turtle.setpos(0, -145)
    turtle.write("UFMS", align="center", font=FONT)

    turtle.setpos(0, -200)
    turtle.write("Música:", align="center", font=FONT)

    turtle.setpos(0, -225)
    turtle.write("Lays Gabrielle", align="center", font=FONT)

    turtle.setpos(-240, -300)
    turtle.write("VOLTAR", align="center", font=FONT)

def mainmenu():
    s = turtle.Screen()
    def backmenu(x,y):
        turtle.clearscreen()
        if y <= -270 and y > -295 and x <= -220 and x > -390:
            import menu
    turtle.listen()       
    turtle.onscreenclick(backmenu,1,True)
    s.done()
drawMenu()
mainmenu()
wn.mainloop()
