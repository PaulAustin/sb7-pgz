# Ported from JavaSript version to Python and Pygame Zero
# Designed to work well with mu-editor environment.
#
# The original Javascript version wasdonw by Ben Eater
# at https://github.com/beneater/boids (MIT License)
# No endorsement implied.
#
# Complex numbers are are used as vectors to integrate x and y positions and velocities
# MIT licesense (details in parent directory)

import random
import time

HEIGHT = 500                # window height
WIDTH = 900                 # window width
MARGIN = 150                # disstance to start avoid edge

NUM_BOIDS = 75
VISUAL_RANGE = 70           # radius of influence for most algoriths
SPEED_LIMIT_UPPER = 13      # boids canonly fly so fast.
SPEED_LIMIT_LOWER = 3       # boid will fall if flying too slow
SPEED_INIT = 20             # range for random velocity

MIN_DISTANCE = 10           # the distance to stay away from other boids
AVOID_FACTOR = 0.05         # % location change if too close
CENTERING_FACTOR = 0.050    # % location change to pull to center
MATCHING_FACTOR = 0.015     # % velocity change if close
MARGIN_FACTOR = 0.25+0.0j   # rate of turning away from edge

HISTORY_LENGTH = 30

BACK_COLOR = (0, 0, 90)
BOID_COLOR = (255, 128, 128)
BOID_SIZE = 8
TRAIL_COLOR = (255, 255, 64)

g_boids = []

class Boid:
    def __init__(boid) :
        boid.loc = complex(
            (random.randint(0, WIDTH)),
            (random.randint(0, HEIGHT)))
        boid.vel = complex(
            (random.randint(-SPEED_INIT, SPEED_INIT)),
            (random.randint(-SPEED_INIT, SPEED_INIT)))
        boid.history = []

    def keep_within_bounds(boid) :
        # Constrain a boid to within the window. If it gets too close to an edge,
        # nudge it back in and reverse its direction.

        if (boid.loc.real < MARGIN):
            boid.vel += MARGIN_FACTOR * 1.0
        if (boid.loc.real > WIDTH - MARGIN) :
            boid.vel += MARGIN_FACTOR * -1.0
        if (boid.loc.imag < MARGIN) :
            boid.vel += MARGIN_FACTOR * 1.0j
        if (boid.loc.imag > HEIGHT - MARGIN) :
            boid.vel += MARGIN_FACTOR * -1.0j

    def fly_towards_center(boid):
        # Find the center of mass of the other boids and
        # adjust velocity slightly to point towards the
        # center of mass.
        center = 0+0j
        num_neighbors = 0

        for other_boid in g_boids :
            if abs(boid.loc - other_boid.loc) < VISUAL_RANGE :
                center += other_boid.loc
                num_neighbors += 1

        if num_neighbors > 0 :
            center = center / num_neighbors

        boid.loc += (center - boid.loc) * CENTERING_FACTOR

    def avoid_others(boid):
        # Move away from other boids that are too close to avoid colliding
        move = 0+0j
        for other_boid in g_boids :
            if not (other_boid is boid) :
                if abs(boid.loc - other_boid.loc) < MIN_DISTANCE :
                    move += boid.loc - other_boid.loc

        boid.vel += move * AVOID_FACTOR

    def match_velocity(boid):
        # Find the average velocity (speed and direction)
        # of the other boids and adjust velocity slightly to match.

        avg_vel = 0+0j
        num_neighbors = 0

        for otherBoid in g_boids:
            if abs(boid.loc - otherBoid.loc) < VISUAL_RANGE :
                avg_vel += otherBoid.vel
                num_neighbors += 1

        if num_neighbors > 0:
            avg_vel /= num_neighbors

        boid.vel += (avg_vel - boid.vel) * MATCHING_FACTOR

    def limit_speed(boid):
        # Speed will naturally vary in flocking behavior,
        # but real animals can't go arbitrarily fast (or slow)
        speed = abs(boid.vel)
        if (speed > SPEED_LIMIT_UPPER) :
            boid.vel = boid.vel / speed * SPEED_LIMIT_UPPER
        if (speed < SPEED_LIMIT_LOWER) :
            boid.vel = boid.vel / speed * SPEED_LIMIT_LOWER
        return

    def draw(boid):
        screen.draw.filled_circle((boid.loc.real, boid.loc.imag), BOID_SIZE, BOID_COLOR)
        tail = boid.loc + boid.vel * -1.8
        screen.draw.line(
            (boid.loc.real, boid.loc.imag),
            (tail.real, tail.imag),
            BOID_COLOR)

    def draw_trail(boid):
        pt_from = (boid.loc.real, boid.loc.imag)
        for p in boid.history:
            pt_to = (p.real, p.imag)
            screen.draw.line(pt_from, pt_to, TRAIL_COLOR)
            pt_from = pt_to

def draw():
    screen.fill(BACK_COLOR)
    if keyboard.space:
        for boid in g_boids:
            boid.draw_trail()
    for boid in g_boids:
        boid.draw()
    screen.draw.text("space:tails  r:restart", (20, 20))

def update():
    for boid in g_boids:
        # Apply rules
        boid.fly_towards_center()
        boid.avoid_others()
        boid.match_velocity()
        boid.limit_speed()
        boid.keep_within_bounds()

        # Update the position based on the current velocity
        boid.loc += boid.vel
        boid.history.insert(0, boid.loc)
        boid.history = boid.history[:HISTORY_LENGTH]

def init():
    global g_boids
    g_boids = [Boid() for _ in range(NUM_BOIDS)]

def on_key_down(key, mod, unicode):
    if (key == keys.R):
        init()

init()
