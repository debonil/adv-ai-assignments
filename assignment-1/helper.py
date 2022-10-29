import turtle


turtle.register_shape('images\\football.gif')
turtle.register_shape('images\\blue_player0.gif')
turtle.register_shape('images\\blue_player1.gif')
turtle.register_shape('images\\blue_player2.gif')
turtle.register_shape('images\\blue_player3.gif')
# turtle.register_shape('images\\images.png')
turtle.register_shape('images\\red_player.gif')


def drawField():
    turtle.setup(1224, 700)
    turtle.speed(100)
    turtle.bgcolor('green')
    turtle.color('white')
    turtle.pensize(4)
    turtle.tracer(0, 0)
    # Draw the outer boundary Dimension of my football ground (500,250)(-500,250)(500,-250)(-500,-250)
    turtle.penup()
    turtle.goto(500, -250)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(500)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(1000)
    turtle.setheading(270)
    turtle.forward(500)
    turtle.setheading(360)
    turtle.forward(1000)

    # draw the left side
    turtle.fillcolor("blue")
    turtle.penup()
    turtle.goto(-500, 100)
    turtle.pendown()
    turtle.forward(100)
    turtle.setheading(270)
    turtle.forward(200)
    turtle.setheading(180)
    turtle.forward(100)
    # left goal post
    turtle.fillcolor("red")
    turtle.setheading(90)
    turtle.penup()
    turtle.begin_fill()
    turtle.forward(40)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(35)
    turtle.setheading(90)
    turtle.forward(120)
    turtle.setheading(360)
    turtle.forward(35)
    turtle.end_fill()
    # draw the right side
    turtle.penup()
    turtle.goto(500, 100)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(100)
    turtle.setheading(270)
    turtle.forward(200)
    turtle.setheading(360)
    turtle.forward(100)
    # right goal post
    turtle.fillcolor("blue")
    turtle.setheading(90)
    turtle.penup()
    turtle.begin_fill()
    turtle.forward(40)
    turtle.pendown()
    turtle.setheading(360)
    turtle.forward(35)
    turtle.setheading(90)
    turtle.forward(120)
    turtle.setheading(180)
    turtle.forward(35)
    turtle.end_fill()

    # draw center
    turtle.penup()
    turtle.goto(0, 250)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(500)
    turtle.penup()

    turtle.goto(80, 0)
    turtle.setheading(90)
    turtle.pendown()
    turtle.circle(80)
    turtle.hideturtle()
    ##### Field Design Complete#####


def createFootball():

    # ball design
    ball = turtle.Turtle()
    ball.hideturtle()
    ball.right(0)
    ball.penup()
    ball.forward(0)
    ball.showturtle()
    ball.shape('circle')
    ball.color('light green')
    ball.shapesize(2)
    ball.left(0)
    ball.speed(5)
    #ball.dx = 2
    #ball.dy = -2
    ball.shape('images\\football.gif')
    return ball


def writeText(distance, tpen: turtle.Turtle):
    tpen.clear()
    tpen.penup()
    tpen.setpos((100, 200))
    tpen.write(f"Path and Distances:\n", False, font=("Another", 16, "bold"))
    Lowest = [100000]
    for i, dist in enumerate(distance):
        tpen.setpos((100, 180-i*20))
        tpen.write(f"Agent to Goal via {dist[1]}:\t {dist[0]:.2f}\n", False, font=(
            "Another", 12, "bold"))
        if dist[0] < Lowest[0]:
            Lowest = dist
    tpen.setpos((100, 180-len(distance)*20))
    tpen.write(f"\nLowest Distance:\t{Lowest[0]:.2f} via {Lowest[1]}", False, font=(
        "Another", 12, "bold"))
    tpen.setpos((100, 180-len(distance)*20-20))
    tpen.write(f"(Click on the Screen to generate new player arrangement )",
               False, font=("Another", 9, ""))
    tpen.hideturtle()


epsilon = 0.5
class Point:
    x:float
    y:float
    def __init__(self, point:turtle.Vec2D):
        self.x=point[0]
        self.y=point[1]

def isBetween(a:Point, b:Point, c:Point):
    crossproduct = (c.y - a.y) * (b.x - a.x) - (c.x - a.x) * (b.y - a.y)

    # compare versus epsilon for floating point values, or != 0 if using integers
    if abs(crossproduct) > epsilon:
        return False

    dotproduct = (c.x - a.x) * (b.x - a.x) + (c.y - a.y)*(b.y - a.y)
    if dotproduct < 0:
        return False

    squaredlengthba = (b.x - a.x)*(b.x - a.x) + (b.y - a.y)*(b.y - a.y)
    if dotproduct > squaredlengthba:
        return False

    return True
def isBlocked(kicker:turtle.Turtle, GoalPoint:tuple, intermediates:list[turtle.Turtle]):
    return False
    is_blocked = False
    for via in intermediates:
        a=Point(kicker.pos())
        b=Point(GoalPoint[0])
        c=Point(via.pos())
        is_blocked= is_blocked or isBetween(a,b,c)
    return is_blocked