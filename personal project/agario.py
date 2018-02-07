import turtle
import math
import random
import time
from ball import Ball


turtle.tracer(0)
turtle.hideturtle()
RUNNING = True
SLEEP = 0.05
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(0,0,0,0,30,"green")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 35
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = []


#PART 0
for i in range(NUMBER_OF_BALLS):
    X = random.randint(round(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS),round(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
    Y = random.randint(round(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS),round(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
    DX = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX )
    DY = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DX)
    while DX == 0 or DY == 0:
        DX = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX )#how can we make  sure that the dx and dy are not 0
        DY = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY )
    RADIUS = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
    COLOR = (random.random(), random.random() , random.random())
    new_ball = Ball(X,Y,DX,DY,RADIUS,COLOR)
    BALLS.append(new_ball)

# PART 1 

def move_balls():
    for ball in BALLS:
        ball.move(SCREEN_WIDTH , SCREEN_HEIGHT)


#PART 2

def collide(ball_a,ball_b):
    if ball_a==ball_b:
        return False
    d = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2)+math.pow(ball_a.ycor()-ball_b.ycor(),2))
    if d +10 <= ball_a.r + ball_b.r:
        return True 
    else:
         return False




        

def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            if ball_a.collide(ball_a,ball_b)== True:
                A_radius =  ball_a.RADIUS 
                B_radius = ball_b.RADIUS
                
                X_COORDINATE= random.randint(-SCREEN_WIDTH + ball_a.RADIUS , SCREEN_WIDTH - a.RADIUS)
                Y_COORDINATE= random.randint(-SCREEN_HEIGHT + ball_a.RADIUS , SCREEN_HEIGHT - a.RADIUS)
                X_AXISSPEED = 0
                Y_AXISSPEED = 0
                while X_AXISSPEED == 0  or Y_AXISSPEED == 0:
                    X_AXISSPEED = random.randinit( MINIMUM_BALL_DX , MAXIMUM_BALL_DX)               
                    Y_AXISSPEED = random.randinit(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
                Radius =random.randinit(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
                r = random.randint(0,256)
                b = random.randint(0,256)
                g = random.randint(0,256)
                Color = random.randint(r,g,b) 
                if ball_a.r > ball_b.r:
                    balL_b.goto(X_COORDINATE, Y_COORDINATE)
                    ball_b.r = Radius
                    ball_b.dx = X_AXISSPEED
                    ball_b.dy = Y_AXISSPEED
                    ball_b.color = Color
                    ball_a.r = ball_a.r + 1
                    ball_a.shapesize(ball_a.r/10)
                    ball_b.shapesize(ball_b.r/10)
                else:
                    balL_a.goto(X_COORDINATE, Y_COORDINATE)
                    ball_a.r = Radius
                    ball_a.dx = X_AXISSPEED
                    ball_a.dy = Y_AXISSPEED
                    ball_a.color = Color
                    ball_b.r = ball_a.r + 1
                    ball_a.shapesize(ball_a.r/10)
                    ball_b.shapesize(ball_b.r/10)

# part 4


def check_myball_collision():
    for ball in BALLS:
        if collide(MY_BALL,ball) == True:

            X_COORDINATE= random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
            Y_COORDINATE= random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
            X_AXISSPEED = 0
            Y_AXISSPEED = 0
            while X_AXISSPEED == 0  or Y_AXISSPEED == 0:
                X_AXISSPEED = random.randint( MINIMUM_BALL_DX , MAXIMUM_BALL_DX)               
                Y_AXISSPEED = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
            Radius =random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
            r = random.random()
            b = random.random()
            g = random.random()
            Color = (r,g,b) 
            
            ball_r4 = ball.r
            my_ball_r4 = MY_BALL.r
            if my_ball_r4 < ball_r4:
                return False
            else:
                MY_BALL.r += 1
                MY_BALL.shapesize(MY_BALL.r/10)
                ball.r = Radius
                ball.x = X_COORDINATE
                ball.y = Y_COORDINATE
                ball.dx = X_AXISSPEED
                ball.dy = Y_AXISSPEED
                ball.color = Color
                ball.shapesize(ball.r/10)
                ball.goto(ball.x, ball.y)
    return True 
            
            
            



## part_5:


def movearound(event):
    XX = event.x - round(SCREEN_WIDTH)
    YY = round(SCREEN_HEIGHT) - event.y
    MY_BALL.goto(XX,YY)

##Part_5.1:
turtle.getcanvas().bind("<Motion>", movearound)
turtle.getscreen().listen()
## fffffffffffffffiiiiiiiiiiiiiiiiiinaaaaaaaaaaaaal paaaaaaaaaaart

while (RUNNING):
    if(SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2):
        SCREEN_WIDTH =  turtle.getcanvas().winfo_width()/2
    if(SCREEN_HEIGHT == turtle.getcanvas().winfo_height()/2):
         SCREEN_HEIGHT == turtle.getcanvas().winfo_height()/2
    for ball in BALLS:
        ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)
        
    RUNNING = check_myball_collision()
    time.sleep(SLEEP)
    turtle.getscreen().update()
        
turtle.mainloop()
