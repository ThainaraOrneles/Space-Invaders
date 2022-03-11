# Space Invader by Mahesh Sawant
import turtle
import winsound
import os
import math
import random
import pygame
import time
import DrawBorder
# Set up the screen
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Space Invaders by Mahesh Sawant adapted by Thainara and Ygor")
wn.bgpic("background.gif")

pygame.mixer.init()
pygame.mixer.music.load("music2.mp3")
pygame.mixer.music.play(-1)
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
# Register the shape
turtle.register_shape("Invaders.gif")
turtle.register_shape("BOSS.gif")
turtle.register_shape("BOSS_RED.gif")
turtle.register_shape("Spacecraft.gif")

# Draw border
#import DrawBorder

# Set the score to 0
score = 0

# Draw the pen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
#player.color("blue")
player.shape("Spacecraft.gif")
player.penup()
player.speed(0)
player.setposition(-250,0)
player.setheading(180)

playerspeed = 30

# Choose a number of enemies
number_of_enemies = 4
# Creat an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # create the enemy
    enemies.append(turtle.Turtle())
   
for enemy in enemies:
    if score > 100:
        enemy.color("Red")
    enemy.shape("Invaders.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(200, 250)
    y = random.randint(-250, 250)
    enemy.setposition(x, y)

    
enemyspeed = 4.5

# Create Boss
number_of_boss = 1
# Creat an empty list of boss
bossList = []

# Add boss to the list
for i in range(number_of_boss):
    # create the boss
    bossList.append(turtle.Turtle())
   
for boss in bossList:
    boss.shape("BOSS.gif")
    boss.penup()
    boss.speed(0)
    boss.hideturtle()
    boss.setposition(-300, -400)

  
bossspeed = 6

# Creat the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bullet.right(90)
bulletspeed = 30

# define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"


# Creat the boss's bullet
bossbullet = turtle.Turtle()
bossbullet.color("green")
bossbullet.shape("circle")
bossbullet.penup()
bossbullet.speed(0)
bossbullet.setheading(90)
bossbullet.shapesize(0.8,0.8)
bossbullet.hideturtle()
bossbullet.right(90)
bossbulletspeed = 30

# define boss bullet state
# ready - boss ready to fire
# fire - boss bullet is firing
bossbulletstate = "ready"

# Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def move_up():
    y = player.ycor()
    y += playerspeed
    if y > 280:
        y = 280
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < -280:
        y = -280
    player.sety(y)
    
def fire_bullet():
    # Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move the bullet to the just above the player
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC) #sound for windows
        #os.system("aplay laser.wav&") #sound for linux
        x = player.xcor() + 25
        y = player.ycor() 
        bullet.setposition(x,y)
        bullet.showturtle()
def boss_fire_bullet():
    # Declare bossbulletstate as a global if it needs changed
    global bossbulletstate
    if bossbulletstate == "ready":
        bossbulletstate = "fire"
        # Move the bullet to the just above the player
        #os.system("aplay laser.wav&") #sound for linux
        winsound.PlaySound("boss.wav", winsound.SND_ASYNC) #sound for windows
        x = boss.xcor() - 25
        y = boss.ycor() 
        bossbullet.setposition(x,y)
        bossbullet.showturtle()
# For collision between enemy and bullet
def isCollision_enemy_bullet(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        return True
    else:
        return False

# For collision between enemy and player
def isCollision_enemy_player(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 45:
        return True
    else:
        return False

# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(fire_bullet, "space")

# Main game loop
Game_Over = False
missed_enemies = 0
boss.setx(-300)
while True:
   
    for enemy in enemies:
        x = enemy.xcor()
        x -= enemyspeed
        enemy.setx(x)

        for e in enemies:
            if e.xcor() < -285 and Game_Over == False and score % 100 != 0:
                e.hideturtle()
                x = random.randint(200, 250)
                y = random.randint(-250, 250)
                e.setposition(x, y)
                e.showturtle()
        # check for a collision between the bullet and the enemy
        if isCollision_enemy_bullet(bullet, enemy):
            winsound.PlaySound("explosion-e+b.wav", winsound.SND_ASYNC) #sound for windows
            #os.system("aplay explosion-e+b.wav&")  # sound for linux
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            if score > 100:
                enemy.color("Red")
            x = random.randint(200, 250)
            y = random.randint(-100, 100)
            enemy.setposition(x, y)
            enemyspeed += 0.5
            # update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        isboss = True
        ## BOSS ##
        if score // 100 > 0 and score // 100 <= 10 and score % 100 == 0 and boss.xcor() == -300:
            for r in enemies:
                r.hideturtle()
                r.setposition(-300, -400)
            x = random.randint(200, 250)
            y = random.randint(-250, 250)
            vida = 4
            boss.setposition(x,y)
            boss.showturtle()
            bossbulletstate = "ready"
            boss_fire_bullet()
        #verifica a colisão do tiro no boss
        if isCollision_enemy_bullet(bullet, boss):
            winsound.PlaySound("explosion-e+b.wav", winsound.SND_ASYNC) #sound for windows
            #os.system("aplay explosion-e+b.wav&")  # sound for linux
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            boss.shape("BOSS_RED.gif")
            time.sleep(0.1)
            boss.shape("BOSS.gif")
            vida = vida - 1
            # update the score
            if vida == 0:
                bossbulletstate = "stop"
                bossbullet.hideturtle()
                boss.hideturtle()
                boss.setposition(-300, -400)
                score += 10
                scorestring = "Score: %s" %score
                score_pen.clear()
                score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
                
        # check for a collision between the boss's bullet and the player
        if isCollision_enemy_bullet(bossbullet, player):
            winsound.PlaySound("explosion-e+b.wav", winsound.SND_ASYNC) #sound for windows
            #os.system("aplay explosion-e+b.wav&")  # sound for linux
            # Reset the bullet
            bossbullet.hideturtle()
            bossbulletstate = "ready"
            bossbullet.setposition(0, -400)
            pygame.mixer.music.pause()
            pygame.mixer.music.load("fim.mpeg")
            pygame.mixer.music.play()
            # Reset the enemy
            Game_Over = True
            if Game_Over == True:           
                player.hideturtle()
                bullet.hideturtle()
                boss.hideturtle()
                for e in enemies:
                    e.hideturtle()
                #tela game_over
                import GameOver
            
        # check for a collision between the player and enemy
        for boss in bossList:
            # Move the boss
            y = boss.ycor()
            y += bossspeed
            boss.sety(y)


        # Move the boss back and down
        if boss.ycor() > 270:
            bossspeed *= -1


        if boss.ycor() < -270:
            # Change boss direction
            bossspeed *= -1
            # Move the bullet        
        
        if isCollision_enemy_player(player, enemy):
            #winsound.PlaySound("explosion-e+p.wav", winsound.SND_ASYNC) #sound for windows
            # os.system("aplay explosion-e+p.wav&")  # sound for linux
            pygame.mixer.music.pause()
            pygame.mixer.music.load("fim.mpeg")
            pygame.mixer.music.play()
            Game_Over = True
        if Game_Over == True:           
            player.hideturtle()
            bullet.hideturtle()            
            for e in enemies:
                e.hideturtle()
            #tela game_over
            import GameOver

    # Move the bullet
    if bulletstate == "fire":
        x = bullet.xcor()
        x += bulletspeed
        bullet.setx(x)

    # Check to see if the bullet has gone to the top
    if bullet.xcor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
        
    if bossbulletstate == "fire":
        x = bossbullet.xcor()
        x -= bossbulletspeed
        bossbullet.setx(x)
    # Check to see if the boss's bullet has gone to the top
    if bossbullet.xcor() < -285:
        bossbullet.hideturtle()
        bossbulletstate = "ready"
        boss_fire_bullet()
delay = input("Press enter to finish")
wn.listen()
wn.mainloop()
