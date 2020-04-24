# Example using pygame-zero actor object
# pull the ball back as if it is a sling shot
# with the pgz animation function

BACK_COLOR = (200, 225, 255)
HEIGHT = 300
WIDTH = 1000
BACKGROUND1 = 'background_mountains1_1000_200'
BACKGROUND2 = 'background_mountains2_1000_200'
BACKGOUND_TIME = 20.0

back1 = Actor(BACKGROUND1, (500, 200))
back2 = Actor(BACKGROUND2, (1500, 200))
g_backgrounds = [back1, back2]

def draw():
    screen.fill(BACK_COLOR)
    back1.draw()
    back2.draw()

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
