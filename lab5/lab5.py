#Q1:
from turtle import Turtle
class square(Turtle):
    def __init__(self,size):
        Turtle.__init__(self)
        self.shapesize(size)
        self.shape("square")
        #extra1:

#Q2:
import turtle
from turtle import *
class Hexagon(Turtle):
    def __init__(self,size,color,speed):
        Turtle.__init__(self)
        self.home()
        self.color(color)
        self.speed(speed)
        self.begin_poly()
        self.left(30)
        self.fd(size)
        self.left(60)
        self.fd(size)
        self.left(60)
        self.fd(size)
        self.left(60)
        self.fd(size)
        self.left(60)
        self.fd(size)
        self.left(60)
        self.fd(size)
        self.left(60)
        self.end_poly()
        Hexagon = self.get_poly()
        register_shape("forat", Hexagon)
        self.shape("forat")
    def forward(self):
        self.fd(200)
