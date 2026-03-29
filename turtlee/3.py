import turtle
import random

n=turtle.Turtle()
m=turtle.Screen()

m.bgcolor("black")
n.color("white")
print(n.position())
n.pensize(2)
n.speed(5)

n.begin_fill()
for i in range(20):
    n.goto(random.randint(-200,200),random.randint(-200,200))
    print(n.position())
n.goto(0,0)
n.end_fill()

n.teleport(-300,300)
print(n.position())
n.begin_fill()
for i in range(20):
    n.goto(random.randint(-500,-100),random.randint(100,500))
    print(n.position())
n.goto(-300,300)
n.end_fill()

n.teleport(300,300)
print(n.position())
n.begin_fill()
for i in range(20):
    n.goto(random.randint(100,500),random.randint(100,500))
    print(n.position())
n.goto(300,300)
n.end_fill()

n.teleport(300,-300)
print(n.position())
n.begin_fill()
for i in range(20):
    n.goto(random.randint(100,500),random.randint(-500,-100))
    print(n.position())
n.goto(300,-300)
n.end_fill()

n.teleport(-300,-300)
print(n.position())
n.begin_fill()
for i in range(20):
    n.goto(random.randint(-500,-100),random.randint(-500,-100))
    print(n.position())
n.goto(-300,-300)
n.end_fill()
turtle.done()