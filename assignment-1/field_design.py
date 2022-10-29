import random
import turtle

from helper import createFootball, drawField, isBlocked, writeText

# window configuration
win = turtle.Screen()
win.bgcolor('dark green')
win.title(
    'Adv Artificial Intelligence Assignment: By Debonil Ghosh [M21AIE225]')
win.tracer(0)

drawField()
football = createFootball()
# Creating Blue FCB team

Y = 3
X = 3
# distance=[],[]
# print(distance)
blueTeam = [turtle.Turtle() for i in range(4)]
kicker = blueTeam[0]
blue_player3 = blueTeam[3]
blue_player2 = blueTeam[2]
blue_player1 = blueTeam[1]

for i, player in enumerate(blueTeam):
    player.penup()
    player.speed(0)
    player.color('dark blue')
    player.shape(f'images\\blue_player{i}.gif')
    player.goto(-100, 200 - i*100) if i > 0 else player.goto(30, 30)
    player.turtlesize(1)


# Creating Red CSK team
redteam = [turtle.Turtle() for i in range(3)]
Goalkeeper = redteam[2]
for i, player in enumerate(redteam):
    player.penup()
    player.speed(0)
    player.color('dark red')
    player.shape('images\\red_player.gif')
    player.turtlesize(1)
    player.goto(-250, 100 - i*200)
Goalkeeper.goto(-450, 5)
Goalkeeper.color('dark red')

GoalPoint = (-501, 0)

textTurtle = turtle.Turtle()
textTurtle.penup()
textTurtle.setpos((-150, -300))
textTurtle.write(f"(Click on the Screen to generate new player arrangement )",
                 False, font=("Another", 12, ""))
textTurtle.hideturtle()


def calculateDistance():

    distance = [[] for i in range(7)]
    distance[2] = [kicker.distance(
        blue_player1) + blue_player1.distance(GoalPoint), ['P1'], isBlocked(kicker, GoalPoint, [blue_player1])]
    distance[1] = [kicker.distance(
        blue_player2) + blue_player2.distance(GoalPoint), ['P2']]
    distance[0] = [kicker.distance(
        blue_player3) + blue_player3.distance(GoalPoint), ['P3']]
    distance[3] = [kicker.distance(blue_player1) + blue_player1.distance(
        blue_player3) + blue_player3.distance(GoalPoint), ['P1', 'P3']]
    distance[4] = [kicker.distance(blue_player2) + blue_player2.distance(
        blue_player3) + blue_player3.distance(GoalPoint), ['P2', 'P3']]
    distance[5] = [kicker.distance(blue_player1) + blue_player1.distance(blue_player2) +
                   blue_player2.distance(blue_player3) + blue_player3.distance(GoalPoint), ['P1', 'P2', 'P3']]
    distance[6] = [kicker.distance(blue_player2) + blue_player2.distance(blue_player1) +
                   blue_player1.distance(blue_player3) + blue_player3.distance(GoalPoint), ['P2', 'P1', 'P3']]
    ########finding shortest distance######
    writeText(distance, textTurtle)


def arrangePlayers(x=None, y=None):
    for player in redteam:
        player.goto(random.randint(-499, -50), random.randint(-50, 100))
    Goalkeeper.goto(-450, random.randint(-10, 10))
    kicker.goto(random.randint(-60, 60), random.randint(-60, 60))
    kicker_pos = kicker.pos()
    football.goto((kicker_pos[0]-30, kicker_pos[1]-30))

    blue_player3.goto(random.randint(-455, -400), random.randint(-100, 100))
    blue_player2.goto(random.randint(-500, 0), random.randint(0, 250))
    blue_player1.goto(random.randint(-500, 0), random.randint(-250, 0))
    calculateDistance()
    turtle.update()


turtle.update()


# key bindings
win.listen()
win.onkeypress(arrangePlayers, 'Return')
win.onscreenclick(arrangePlayers)


turtle.done()
