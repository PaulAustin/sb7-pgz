# Example using pygame-zero actor object
# pull the ball back as if it is a sling shot
# with the pgz animation function

BACK_COLOR = (200, 225, 255)
HEIGHT = 300
WIDTH = 500
BALL = 'ball_100x100'
DOG2 = 'dog2_100x100'

ball = Actor(BALL, (100, 100))

def draw():
    screen.fill(BACK_COLOR)
    ball.draw()
    screen.draw.filled_circle((150,150), 20, (0,200,0))
    screen.draw.line((150,150),ball.pos,(0,255,0))

def on_mouse_down(pos,button):
    on_mouse_move(pos, (0,0), {button})

def on_mouse_move(pos, rel, buttons):
    # base animation time on distance
    # 1000 pixels per second
    d = ball.distance_to(pos)
    if d != 0 and mouse.LEFT in buttons:
        # Throw the ball
        animate(ball,
            tween= 'decelerate',
            duration= d / 5000,
            on_finished= None,
            pos= pos)

