# Example using pygame-zero actor object
# pull the ball back as if it is a sling shot
# with the pgz animation function

BACK_COLOR_DAY = (200, 225, 255)
BACK_COLOR_NIGHT = (50, 50, 128)
HEIGHT = 300
WIDTH = 1000
BACKGROUND0 = 'background_mountains0_1000x200'
BACKGROUND1 = 'background_mountains1_1000x200'
BACKGOUND_TIME = 10.0

back0 = Actor(BACKGROUND0, (500, 200))
back1 = Actor(BACKGROUND1, (1500, 200))
g_backgrounds = [back0, back1]

def draw():
    if not keyboard.space:
        screen.fill(BACK_COLOR_DAY)
    else:
        screen.fill(BACK_COLOR_NIGHT)
    b0, b1 = g_backgrounds
    b0.draw()
    b1.draw()

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

scroll_backgrounds(g_backgrounds)
