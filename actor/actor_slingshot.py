# Example using pygame-zero actor object
# working on the sling shot
# with the pgz animation function

import time

BACK_COLOR = (200, 225, 255)
HEIGHT = 400
WIDTH = 800
BALL = 'ball_100x100'
DOG2 = 'dog2_100x100'

GRAVITY = -9.81   # meters / seconds^2
SCALE   = 100.0   # 100px  / meter
DRAG    = 1.0
TARGET_T_DELTA = 0.01

INITIAL_VELOCITY = (0.0,0.0)     # in m/s - clean drop for starters
ball = Actor(BALL, (100, 100))
ball.posm = (1.0, 1.0)           # position in meters
ball.velocity = (0.0, 0.0)
ball.accel = (0.0, GRAVITY)
t_last = 0
t_drop = 0
g_clock = None

def sim_motion():
    global t_last, g_clock

    keep_going = True
    # Object roughly has location and velocity
    # they cant both be percise the this is an rougth
    # 100 Hz simuation

    # use the monotonic timer to measure the real delta time
    t_now = time.monotonic()
    t_delta = t_now - t_last
    t_last = t_now

    x, y   = ball.posm
    vx, vy = ball.velocity
    ax, ay = ball.accel

    if (vy < 0 and y < 0.40):
        # bounce and dampen
        vy = -vy * 0.70
        # print ("time till bounce", t_now - t_drop)
        if (abs(vy) * t_delta < 1.0 / SCALE):
            keep_going = False
            vy = 0

    vx *= DRAG
    vy *= DRAG
    ball.posm = (x + (vx * t_delta), y + (vy * t_delta))
    ball.velocity = (vx + (ax * t_delta), vy + (ay * t_delta))

    # Translate meter values to pixel locations
    ball.pos = (ball.posm[0] * SCALE), (HEIGHT - ball.posm[1] * SCALE)

    if (keep_going):
        g_clock = clock.schedule(sim_motion, TARGET_T_DELTA)

    return

def draw():
    screen.fill(BACK_COLOR)
    ball.draw()
    # screen.draw.filled_circle((150,150), 20, (0,200,0))
    # screen.draw.line((150,150),ball.pos,(0,255,0))

def on_mouse_down(pos,button):
    on_mouse_move(pos, (0,0), {button})

def on_mouse_up(pos):
    global t_last, t_drop
    ball.pos = pos
    ball.posm = ball.pos[0]/SCALE, (HEIGHT - ball.pos[1]) / SCALE
    ball.velocity = INITIAL_VELOCITY
    ball.accel = (0.0, GRAVITY)
    print("dropped from", ball.posm)
    t_last = t_drop = time.monotonic()
    g_clock = clock.schedule(sim_motion, TARGET_T_DELTA)

def on_mouse_move(pos, rel, buttons):
    if (mouse.LEFT in buttons) :
        ball.pos = pos

