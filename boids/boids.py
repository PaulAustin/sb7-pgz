# Ported from JavaSript version to Python and Pygame Zero
# Designed to work well with mu-editor environment.
#
# Original by Ben Eater at https://github.com/beneater/boids (MIT License)

import math
import random

HEIGHT = 500
WIDTH = 500
MARGIN = 150

NUM_BOIDS = 100
VISUAL_RANGE = 75
SPEED_LIMIT = 18

g_boids = []

class Boid:
    pass

def init_boids():
    boids = []
    for i in range(NUM_BOIDS):
        boid = Boid()
        boid.loc = complex((random.randint(0, WIDTH)), (random.randint(0, HEIGHT)))
        boid.vel = complex((random.randint(-10, 10)), (random.randint(-10, 10)))
        boid.history = []
        boids.append(boid)
    return boids

def distance(boid1, boid2):
    return abs(boid1.loc - boid2.loc)

def n_closest_boids(boids, n):
    # make copy of array
    # sort
    # slice
    return

def fly_to_center(boid):
    return

def avoid_others(boid):
    return

def match_velocity(boid):
    return

# Constrain a boid to within the window. If it gets too close to an edge,
# nudge it back in and reverse its direction.
def keep_within_bounds(boid) :
    if (boid.loc.real < MARGIN) :
        boid.vel += 1+0j
    if (boid.loc.real >  WIDTH - MARGIN) :
        boid.vel += -1+0j
    if (boid.loc.imag < MARGIN) :
        boid.vel += 0+1j
    if (boid.loc.imag >  HEIGHT - MARGIN) :
        boid.vel += 0-1j
    return

"""
// Find the center of mass of the other boids and adjust velocity slightly to
// point towards the center of mass.
function flyTowardsCenter(boid) {
  const centeringFactor = 0.005; // adjust velocity by this %

  let centerX = 0;
  let centerY = 0;
  let numNeighbors = 0;

  for (let otherBoid of boids) {
    if (distance(boid, otherBoid) < visualRange) {
      centerX += otherBoid.x;
      centerY += otherBoid.y;
      numNeighbors += 1;
    }
  }

  if (numNeighbors) {
    centerX = centerX / numNeighbors;
    centerY = centerY / numNeighbors;

    boid.dx += (centerX - boid.x) * centeringFactor;
    boid.dy += (centerY - boid.y) * centeringFactor;
  }
}

// Move away from other boids that are too close to avoid colliding
function avoidOthers(boid) {
  const minDistance = 20; // The distance to stay away from other boids
  const avoidFactor = 0.05; // Adjust velocity by this %
  let moveX = 0;
  let moveY = 0;
  for (let otherBoid of boids) {
    if (otherBoid !== boid) {
      if (distance(boid, otherBoid) < minDistance) {
        moveX += boid.x - otherBoid.x;
        moveY += boid.y - otherBoid.y;
      }
    }
  }

  boid.dx += moveX * avoidFactor;
  boid.dy += moveY * avoidFactor;
}

// Find the average velocity (speed and direction) of the other boids and
// adjust velocity slightly to match.
function matchVelocity(boid) {
  const matchingFactor = 0.05; // Adjust by this % of average velocity

  let avgDX = 0;
  let avgDY = 0;
  let numNeighbors = 0;

  for (let otherBoid of boids) {
    if (distance(boid, otherBoid) < visualRange) {
      avgDX += otherBoid.dx;
      avgDY += otherBoid.dy;
      numNeighbors += 1;
    }
  }

  if (numNeighbors) {
    avgDX = avgDX / numNeighbors;
    avgDY = avgDY / numNeighbors;

    boid.dx += (avgDX - boid.dx) * matchingFactor;
    boid.dy += (avgDY - boid.dy) * matchingFactor;
  }
}

"""
# Speed will naturally vary in flocking behavior,
# but real animals can't go arbitrarily fast.
def limit_speed(boid) :
    speed = abs(boid.vel)
    if (speed > SPEED_LIMIT) :
        boid.vel = boid.vel / speed * SPEED_LIMIT
    return

def draw_boid(boid):
  # could make actor image
  # screen.draw.circle(100, 100, 5)
  screen.draw.circle((boid.loc.real, boid.loc.imag), 4, (255, 0, 0))
  angle = math.atan2(boid.vel.real, boid.vel.imag)
  # draw tail
  return

def draw():
    screen.fill((0,0,0))
    for boid in g_boids:
        draw_boid(boid)

def update():
  for boid in g_boids:
    # Apply rules
    fly_to_center(boid)
    avoid_others(boid)
    match_velocity(boid)
    limit_speed(boid)
    keep_within_bounds(boid)

    # Update the position based on the current velocity
    boid.loc += boid.vel
    # boid.history.append(boid.loc)
    # boid.history = boid.history.slice(-50);

g_boids = init_boids()
