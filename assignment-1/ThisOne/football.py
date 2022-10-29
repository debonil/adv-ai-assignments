import turtle


def create_football():
    football = turtle.Turtle()
    turtle.register_shape('assets/football.gif')
    football.shape('assets/football.gif')
    football.hideturtle()
    football.right(0)
    football.penup()
    football.forward(0)
    football.showturtle()
    football.color('lightblue')
    football.shapesize(1)
    football.left(0)
    football.speed(2)
    football.dx = 1
    football.dy = -1
    turtle.update()
