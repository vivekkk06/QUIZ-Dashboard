import turtle
import random
n= turtle.Turtle()
i=turtle.Turtle()
m= turtle.Screen()

m.bgcolor("green")
n.shape("triangle")
n.pensize(5)
n.color("blue")
i.write("Find me if you can!", align="center", font=("Arial", 24, "bold"))

def up():
    n.setheading(90)
    n.forward(50)
def left():
    n.setheading(180)
    n.fd(50)
def right():
    n.setheading(0)
    n.fd(50)
def down():
    n.setheading(270)
    n.fd(50)
def x():
    print(n.distance(i))

i.teleport(random.randint(-500,500), random.randint(-500,500))
i.dot(20, "red")
m.onkeypress(right, "d")
m.onkeypress(up, "w")
m.onkeypress(left, "a")
m.onkeypress(down, "s")
m.onkeypress(x, "space")
m.listen()
if n.distance(i) < 40:
    i.clearscreen()
    i.write("You found me!", align="center", font=("Arial", 24, "bold"))
turtle.done()

