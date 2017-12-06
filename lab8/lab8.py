from turtle import *
import random

class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)
ball1 = Ball(10, "red", 3)
ball2 = Ball(50, "green", 4)
ball1.penup()
def check_coloision(ball1,ball2):
    import math
    x1 = ball1.xcor()
    x2 = ball2.xcor()
    y1 = ball1.ycor()
    y2 = ball2.ycor()
    if ((ball1.radius) + (ball2.radius)) >= (math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))):
        print("collide")
    else:
        print("not collide")
