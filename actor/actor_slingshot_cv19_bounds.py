# Example using pygame-zero actor object
# working on the sling shot
# with the pgz animation function

import math
import time
import random

BACK_COLOR = (0, 0, 128)
DOT_COLOR = (0, 0, 0)
SLING_COLOR = (0, 255, 0)
HEIGHT = 600
WIDTH = 1200
BALL = 'blueball_75x75'
VIRUS_C = 'cvc_50x50.png'
VIRUS_R = 'cvr_50x50.png'
VIRUS_Y = 'cvy_50x50.png'
DOG2 = 'dog2_100x100'
BOUNCE_DAMPEN = 0.90
AIR_DAMPEN = 0.99
SPRING_FACTOR = 8.0

DOT_POS = (200, 200)

GRAVITY = -9.81   # meters / seconds^2
SCALE   = 100.0   # 100px  / meter
DRAG    = 1.0
TARGET_T_DELTA = 0.01

NUM_VIR = 40
TARGET_NAMES = [VIRUS_C, VIRUS_R, VIRUS_Y]
g_targets = []

ball = Actor(BALL, (100, 100))

g_run_sim = False


def sim_motion():
    global t_last

    # use the monotonic timer to measure the real delta time
    t_now = time.monotonic()
    t_delta = t_now - t_last
    t_last = t_now

    x, y   = ball.posm
    vx, vy = ball.velocity
    ax, ay = ball.accel

    vx *= AIR_DAMPEN
    vy *= AIR_DAMPEN

    if (vy < 0 and y < 50 / SCALE):
        # bounce and dampen
        vy = -vy * BOUNCE_DAMPEN
    if vx > 0 and x > ((WIDTH - 50) / SCALE) :
        vx = -vx * BOUNCE_DAMPEN
    elif vx < 0 and x < 50 / SCALE:
        vx = -vx * BOUNCE_DAMPEN

    vx *= DRAG
    vy *= DRAG
    ball.posm = (x + (vx * t_delta), y + (vy * t_delta))
    ball.velocity = (vx + (ax * t_delta), vy + (ay * t_delta))

    # Translate meter values to pixel locations
    ball.pos = (ball.posm[0] * SCALE), (HEIGHT - ball.posm[1] * SCALE)

    for t in g_targets:
        if ball.distance_to(t) < 40.5 :
            sounds.pop.play()
            g_targets.remove(t)
        else:
            tx, ty = t.pos
            vx, vy = t.velocity
            t.pos = (tx + vx, ty + vy)



    if (abs(vy) < 0.02 and abs(vx) < 0.02):
        # Close to still, stop the sim loop
        reset_sim()
    else:
        clock.schedule(sim_motion, TARGET_T_DELTA)
    return

def spread_targets():
    g_targets.clear()
    for i in range(NUM_VIR):
        name = random.choice(TARGET_NAMES)
        loc = (random.randint(300, WIDTH-50), random.randint(100, HEIGHT-50))
        target = Actor(name, loc)
        target.velocity = (3.0, 5.0)
        g_targets.append(target)

def reset_sim():
    g_run_sim = False
    ball.posm = (1.0, 1.0)           # position in meters
    ball.velocity = (0.0, 0.0)
    ball.accel = (0.0, GRAVITY)
    t_last = 0
    t_drop = 0

def draw():
    screen.fill(BACK_COLOR)
    ball.draw()
    screen.draw.filled_circle(DOT_POS, 10, DOT_COLOR)

    for t in g_targets:
        t.draw()

    if (not g_run_sim):
        screen.draw.line(DOT_POS, ball.pos, SLING_COLOR)

def on_mouse_down(pos,button):
    reset_sim()
    on_mouse_move(pos, (0,0), {button})

def on_mouse_up(pos):
    global t_last, t_drop, g_run_sim

    g_run_sim = True
    ball.pos = pos
    ball.posm = ball.pos[0] / SCALE, (HEIGHT - ball.pos[1]) / SCALE
    ball.accel = (0.0, GRAVITY)

    stretch = ball.distance_to(DOT_POS) / SCALE
    rad = math.radians(ball.angle_to(DOT_POS))
    if (stretch < 0.5):
        ball.velocity = (0, 0)
    else:
        stretch *= SPRING_FACTOR
        ball.velocity = (stretch * math.cos(rad), stretch * math.sin(rad))

    t_last = t_drop = time.monotonic()
    clock.schedule(sim_motion, TARGET_T_DELTA)

def on_mouse_move(pos, rel, buttons):
    if (mouse.LEFT in buttons) :
        ball.pos = pos

def on_key_down(key, mod, unicode):
    if (key == keys.V):
        for i in range(NUM_VIR):
            viru = Actor(VIRUS,
                (random.randint(300, WIDTH-50), random.randint(100, HEIGHT-50)))
        virs.append(viru)


reset_sim()
spread_targets()
