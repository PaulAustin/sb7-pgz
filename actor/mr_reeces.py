# Example using pygame-zero actor object
# pull the ball back as if it is a sling shot
# with the pgz animation function

import random

BACK_COLOR_DAY = (200, 225, 255)
BACK_COLOR_NIGHT = (50, 50, 128)
HEIGHT = 300
WIDTH = 1000

GROUND_X = WIDTH / 2
GROUND_Y = HEIGHT - 50
JUMP_Y = 200

BACKGROUND0 = 'background_mountains0_1000x200'
BACKGROUND1 = 'background_mountains1_1000x200'
VIRUS_C = 'cvc_50x50.png'
VIRUS_R = 'cvr_50x50.png'
VIRUS_Y = 'cvy_50x50.png'
DOG_HAPPY = 'dog2_100x100'

TARGET_NAMES = [VIRUS_C, VIRUS_R, VIRUS_Y]

BACKGOUND_TIME = 10.0


back0 = Actor(BACKGROUND0, (500, 200))
back1 = Actor(BACKGROUND1, (1500, 200))
g_backgrounds = [back0, back1]

dog = Actor(DOG_HAPPY, (GROUND_X, GROUND_Y))

g_targets = []

def draw():
    if not keyboard.space:
        screen.fill(BACK_COLOR_DAY)
    else:
        screen.fill(BACK_COLOR_NIGHT)
    b0, b1 = g_backgrounds
    b0.draw()
    b1.draw()

    for t in g_targets:
        t.draw()

    dog.draw()

    screen.draw.text("SCORE 505, Life 78%", (20, 20))


def background_repeat():
    b0 = g_backgrounds.pop(0)
    g_backgrounds.append(b0)
    scroll_backgrounds(g_backgrounds)
    return


def scroll_backgrounds(backs):
    left = 500
    bottom = 200
    b0, b1 = backs

    b0.pos = (left, bottom)
    animate(b0,
        tween= 'linear',
        duration= BACKGOUND_TIME,
        on_finished= background_repeat,
        pos= (left - 1000, bottom))

    b1.pos = (left + 1000, bottom)
    animate(g_backgrounds[1],
        tween= 'linear',
        duration= BACKGOUND_TIME,
        on_finished= None,
        pos= (left, bottom))

def update():
    test_jump()

    if keyboard.V or len(g_targets) == 0:
        spread_targets(25, 15)

    for t in g_targets:
        if dog.distance_to(t) < 45 :
            sounds.pop.play()
            g_targets.remove(t)
        else:
            tx, ty = t.pos
            vx, vy = t.velocity
            t.pos = (tx + vx, ty + vy)
            tx, ty = t.pos
            if tx > WIDTH or tx < 0 : vx *= -1
            if ty > HEIGHT or ty < 0 : vy *= -1
            t.velocity = (vx, vy)

g_jumping = False
flip_direction = 1

JUMP_T = 0.8
def test_jump():
    global g_jumping, flip_direction
    if keyboard.space and not g_jumping:
        # Start the jump by moving up
        # slowing as it gets to the peak
        g_jumping = True
        animate(dog,
            tween='decelerate',
            duration=JUMP_T / 2,
            on_finished=on_jump_done,
            pos=(GROUND_X, GROUND_Y - JUMP_Y))

        # A second animation does a flip
        # This one is set to be twice as long
        # The the jump is split into two parts
        animate(dog,
            tween='linear',
            duration=JUMP_T,
            on_finished=None,
            angle=360 * flip_direction)
        sounds.bark.play()
        flip_direction *= -1

def on_jump_done():
    global g_jumping
    if g_jumping:
        # Finish the jump by moving down
        # starting slowing the speeding up
        animate(dog,
            tween='accelerate',
            duration=JUMP_T / 2,
            on_finished=on_jump_done,
            pos=(GROUND_X, GROUND_Y))
        g_jumping = False
    else:
        # Reset the angle so next fil will work
        dog.angle = 0
        sounds.pop.play()

def spread_targets(count, max_speed):
    g_targets.clear()
    for i in range(count):
        name = random.choice(TARGET_NAMES)
        loc = (random.randint(300, WIDTH-50), GROUND_Y)
        target = Actor(name, loc)
        vx =  random.randint(-max_speed, max_speed)
        vy =  random.randint(-max_speed, max_speed)
        target.velocity = (vx, vy)
        g_targets.append(target)

scroll_backgrounds(g_backgrounds)
spread_targets(15, 7)


