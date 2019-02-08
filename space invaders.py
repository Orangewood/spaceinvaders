# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 03:33:36 2018

@author: James
"""

import os
import turtle
import math
import random

#Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic('background.gif')


#register the shapes
turtle.register_shape('enemy2.gif')
turtle.register_shape('spaceship.gif')



#Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range (4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Start score
score = 0


#Draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("red")
player.shape("spaceship.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15


#Number of bad spacemen
number_of_spacemans = 8
#empty list of bad guys in jail
badguys = []

for i in range(number_of_spacemans):
    #Create enemy
    badguys.append(turtle.Turtle())

for enemy in badguys:
    enemy.color("green")
    enemy.shape("enemy2.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

#Firing mah laz0r
raygun = turtle.Turtle()
raygun.color("white")
raygun.shape("square")
raygun.penup()
raygun.speed(0)
raygun.setheading(90)
raygun.shapesize(0.3,0.3)
raygun.hideturtle()

raygunspeed = 20

#Laz0r tiem
#begin - chargin!
#fire - destructo disk
raygunstate = "begin"

#Move the player left and right
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

def firing_mah_laz0rs():
    global raygunstate
    if raygunstate =='begin':
        raygunstate = 'fire'

        x = player.xcor()
        y = player.ycor() +10
        raygun.setposition(x,y)
        raygun.showturtle()


def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2)+ math.pow(t1.ycor() - t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(firing_mah_laz0rs, "space")

#Main game loop
while True:

    for enemy in badguys:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Traverse enemy downward
        if enemy.xcor() > 280:
            #Move all enemies down
            for e in badguys:
                y = e.ycor()
                y -= 40                
                e.sety(y)
            enemyspeed *= -1 

        if enemy.xcor() < -280:
            for e in badguys:
                y = e.ycor()
                y -=40                
                e.sety(y)
            enemyspeed *=-1
            
            #Check for laz0r direct hit!
        if isCollision(raygun,enemy):
            #reset laz0rs!! oh noes!!
            raygun.hideturtle()
            raygunstate = 'begin'
            raygun.setposition(0,-400)
            #reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Cash in score!
            score += 1000
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

    
        if isCollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print('Awesome game, great job!')
            break

    #Make laz0r pew
    if raygunstate == 'fire':
        y = raygun.ycor()
        y += raygunspeed
        raygun.sety(y)

    #Boundry of missile:
    if raygun.ycor() > 275:
        raygun.hideturtle()
        raygunstate = 'begin'




wn.mainloop()