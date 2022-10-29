import turtle
from random import randint, choice

from numpy import random

exclude_list_x = []
exclude_list_y = []


def create_blue_team():
    distance = [[0 for i in range(3)] for j in range(3)]
    blue_team = [turtle.Turtle() for i in range(4)]
    turtle.register_shape('assets/blue_player.gif')
    for player in blue_team:
        player.shape('assets/blue_player.gif')
        turtle.update()
    agent = blue_team[3]
    striker = blue_team[2]
    right_wing = blue_team[1]
    left_wing = blue_team[0]
    agent_x = random.randint(-60, 60)
    agent_y = random.randint(-60, 60)
    print(agent_x)
    print(agent_y)
    agent.goto(agent_x, agent_y)
    exclude_list_x.append(agent_x)
    exclude_list_y.append(agent_y)
    striker_x = random_exclude(-455, -400, exclude_list_x)
    striker_y = random_exclude(-100, 100, exclude_list_y)
    print(striker_x)
    print(striker_y)
    striker.goto(striker_x, striker_y)
    exclude_list_x.append(striker_x)
    exclude_list_y.append(striker_y)
    right_wing_x = random_exclude(-500, 0, exclude_list_x)
    right_wing_y = random_exclude(0, 250, exclude_list_y)
    exclude_list_x.append(right_wing_x)
    exclude_list_y.append(right_wing_y)
    right_wing.goto(right_wing_x, right_wing_y)
    left_wing_x = random_exclude(-500, 0, exclude_list_x)
    left_wing_y = random_exclude(-250, 0, exclude_list_y)
    left_wing.goto(left_wing_x, left_wing_y)
    exclude_list_x.append(left_wing_x)
    exclude_list_y.append(left_wing_y)
    turtle.update()
    return blue_team, distance


def create_red_team():
    turtle.register_shape('assets/red_player.gif')
    red_team = [turtle.Turtle() for i in range(3)]
    goalkeeper = red_team[2]
    for player in red_team:
        player.shape('assets/red_player.gif')
        player_x = random_exclude(-500, -50, exclude_list_x)
        player_y = random_exclude(-50, 100, exclude_list_y)
        player.goto(player_x, player_y)
        exclude_list_x.append(player_x)
        exclude_list_y.append(player_y)
    goalkeeper_y = random_exclude(-10, 10, exclude_list_y)
    goalkeeper.goto(-450, goalkeeper_y)
    goalkeeper.color('dark red')
    turtle.update()
    return red_team


def random_exclude(start_range, end_range, exclude_this):
    the_int = random.randint(start_range, end_range)
    while the_int in exclude_this:
        the_int = random.randint(start_range, end_range)
    return the_int
