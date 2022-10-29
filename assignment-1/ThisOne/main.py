import turtle
from football import create_football
from ground import create_field
from optimal_path import find_minimum_dist
from teams import create_blue_team, create_red_team

create_field()
create_football()
blue_team, distance = create_blue_team()
agent = blue_team[3]
striker = blue_team[2]
right_wing = blue_team[1]
left_wing = blue_team[0]
red_team = create_red_team()
find_minimum_dist(agent, striker, right_wing, left_wing)
turtle.done()
