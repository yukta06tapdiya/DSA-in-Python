import turtle 
import math
screen=turtle.Screen()
screen.bgcolor("black")

t=turtle.Turtle()
t.speed()
t.hideturtle()
t.penup()
t.color("#ffb6c1")

for scle in range(11,12):
    for i in range(120):
        angle=i*(math.pi*2)/120

        x=16*(math.sin(angle)**3)*scle
        y=(13*math.cos(angle)-5*math.cos(2*angle)-2*math.cos(3*angle)-math.cos(4*angle))*scle
        t.goto(x,y)
        t.write("Hi",align="center",font=("Arial", 8, "bold"))
turtle.done()

