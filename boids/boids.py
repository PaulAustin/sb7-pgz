# Ported from JavaSript version to Python and Pygame Zero
# Designed to work well with mu-editor environment.
#
# Original by Ben Eater at https://github.com/beneater/boids (MIT License)
# No endorsement implied.

import random

HEIGHT = 600                # window height
WIDTH = 700                 # window width
MARGIN = 150                # disstance to start avoid edge

NUM_BOIDS = 100
VISUAL_RANGE = 70           # range of influence for most algoriths
SPEED_LIMIT_UPPER = 15      # boids canonly fly so fast.
SPEED_LIMIT_LOWER = 3       # boid will fall if flying too slow
SPEED_INIT = 12             # range for random velocity

MIN_DISTANCE = 10           # the distance to stay away from other boids
AVOID_FACTOR = 0.05         # % location change if too close
CENTERING_FACTOR = 0.005    # % location change to pull to center
MATCHING_FACTOR = 0.015     # % velocity change if close

g_boids = []

class Boid:
    pass

def init_boids():
    boids = []
    for i in range(NUM_BOIDS):
        boid = Boid()
        boid.loc = complex(
            (random.randint(0, WIDTH)),
            (random.randint(0, HEIGHT)))
        boid.vel = complex(
            (random.randint(0, SPEED_INIT)),
            (random.randint(0, SPEED_INIT)))
        boid.history = []
        boids.append(boid)
    return boids

def keep_within_bounds(boid) :
    # Constrain a boid to within the window. If it gets too close to an edge,
    # nudge it back in and reverse its direction.

    if (boid.loc.real < MARGIN):
        boid.vel += 0.4+0j
    if (boid.loc.real > WIDTH - MARGIN) :
        boid.vel += -0.4+0j
    if (boid.loc.imag < MARGIN) :
        boid.vel += 0+0.4j
    if (boid.loc.imag > HEIGHT - MARGIN) :
        boid.vel += 0-0.4j
    return

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
    # Find the average velocity (speed and direction) of the other boids and
    # adjust velocity slightly to match.
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

def draw_boid(boid):
    screen.draw.filled_circle((boid.loc.real, boid.loc.imag), 5, (0, 255, 0))
    tail = boid.loc + boid.vel * 1.8
    screen.draw.line(
        (boid.loc.real, boid.loc.imag),
        (tail.real, tail.imag),
        (0, 255, 0))

    # angle = math.atan2(boid.vel.real, boid.vel.imag)
    return

def draw():
    screen.fill((0, 0, 0))
    for boid in g_boids:
        draw_boid(boid)

def update():
    for boid in g_boids:
        # Apply rules
        fly_towards_center(boid)
        avoid_others(boid)
        match_velocity(boid)
        limit_speed(boid)
        keep_within_bounds(boid)

        # Update the position based on the current velocity
        boid.loc += boid.vel
        # boid.history.append(boid.loc)
        # boid.history = boid.history.slice(-50);

g_boids = init_boids()
