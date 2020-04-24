# Example using pygame-zero actor object
# pull the ball back as if it is a sling shot
# with the pgz animation function

BACK_COLOR = (200, 225, 255)
HEIGHT = 300
WIDTH = 1000
BACKGROUND1 = 'background_mountains1_1000_200'
BACKGROUND2 = 'background_mountains2_1000_200'
BACKGOUND_TIME = 8.0
DOG2 = 'dog2_100x100'

back1 = Actor(BACKGROUND1, (500, 200))
back2 = Actor(BACKGROUND2, (1500, 200))

def draw():
    screen.fill(BACK_COLOR)
    back1.draw()
    back2.draw()

def background_repeat():
    back1.pos = (500,200)
    back2.pos = (1500,200)
    scroll_backgrounds()
    return

def scroll_backgrounds():
    animate(back1,
        tween= 'linear',
        duration= BACKGOUND_TIME,
        on_finished= background_repeat,
        pos= (-500, 200))

    animate(back2,
        tween= 'linear',
        duration= BACKGOUND_TIME,
        on_finished= None,
        pos= (500, 200))

scroll_backgrounds()
