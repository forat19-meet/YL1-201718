#Q1:
from turtle import Turtle
class square(Turtle):
    def __init__(self,size):
        Turtle.__init__(self)
        self.shapesize(size)
        self.shape("square")

#Q2:
from turtle import Turtle
class Hexagon(Turtle):
    def __init__(self,size):
        Turtle.__init__(self)
        self.shapesize(size)
        self.shape("hexagon")
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
