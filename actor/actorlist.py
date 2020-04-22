# Example using pygame zero actor

import math
import time

BACK_COLOR = (200, 220, 255)
CELL_COLOR = (0, 200, 0)
HEIGHT = 200
WIDTH = 600

DOG1  = 'dog1_100x100'
DOG2  = 'dog2_100x100'
BALL = 'ball_100x100'
COUNT = 10

balls = [Actor(DOG2,(i*(WIDTH/COUNT), 100)) for i in range(COUNT)]

def draw():
    screen.fill(BACK_COLOR)
    for b in balls:
        b.draw()

    # screen.draw.text("Angle = " + str(int(dog.angle)),(20,20))
    # screen.draw.text("Distance = " + str(int(dog.distance_to(ball))),(20,40))

def update():
    seconds = time.monotonic()
    for b in balls:
        b.angle = seconds * -6
