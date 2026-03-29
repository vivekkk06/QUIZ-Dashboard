import turtle
import random

n=turtle.Turtle()
m=turtle.Screen()
m.bgcolor("black")
n.color("white","red")
n.pensize(2)
n.speed(7)
for j in range(5):
    for i in range(8):
        n.teleport(-500+ i*100,250- j*125)
        n.begin_fill()
        n.circle(random.randint(10,80))
        n.end_fill()
turtle.done()
