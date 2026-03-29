import turtle

n=turtle.Turtle()
m=turtle.Screen()
n.speed(7)
n.color("pink", "yellow")
m.bgcolor("blue")
n.begin_fill()
for i in range(50):
    n.forward(10*i)
    n.left(170)
    n.forward(10*i)
n.end_fill()
turtle.done()