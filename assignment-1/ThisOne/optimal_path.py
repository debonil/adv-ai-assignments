import turtle

from numpy import random


def find_minimum_dist(agent, striker, right_wing, left_wing):
    dist1 = agent.distance(striker)
    dist2 = agent.distance(right_wing)
    dist3 = agent.distance(left_wing)
    dist4 = dist1 + striker.distance((-501, 0))
    dist5 = dist2 + right_wing.distance((-501, 0))
    dist6 = dist3 + left_wing.distance((-501, 0))
    lowest = min(dist4, dist5, dist6)
    turtle.write(f"\n\n\nBest Path {lowest}", font=("Another", 16, "bold"))
    turtle.update()
    print(f"\n{lowest}")
