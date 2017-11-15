#Problem 1:
i = 1
for i in range(100):
    print("forat")
    i = i + 1
#Problem 2:
    #Part 1
number1 = 5
print(number1)
    #part2
number2 = number1 * 0.5
print(number2)
#Problem 3:
    #Part 1:
list1 = [5,8,9]
i = 0
for i in range(3):
    print(list1[i])
    i = i + 1
    #Part 2:
for i in range(3):
    print((list1[i])*2)
    i = i + 1
    #Part 3:
x = 0
for i in range(3):
    x= x + list1[i]
    i = i + 1
print(x)
#Problem 4:
#import turtle
#turtle.goto(100,100)
#turtle.mainloop()
    #extra:
import turtle
turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(45)
turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(45)
turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(45)
turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(45)
turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(45)
turtle.done()

