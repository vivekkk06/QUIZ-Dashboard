import turtle

n=turtle.Turtle()
n.speed(5)
n.begin_fill()
for i in range(8):
    n.goto(-160 + i*40,-160 + i*40)
    for i in range(8):
        n.fd(50)
        n.lt(80)

    for i in range(8):
        n.undo()
n.goto(-160,-160)
n.end_fill()
turtle.done()