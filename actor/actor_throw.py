# Example using pygame-zero actor object
# move the ball to where the mouse is clicked
# with the pgz animation function

BACK_COLOR = (200, 225, 255)
HEIGHT = 200
WIDTH = 400
BALL = 'ball_100x100'

ball = Actor(BALL, (100, 100))

def draw():
    screen.fill(BACK_COLOR)
    ball.draw()

def reset_ball():
    ball.pos = (100, 100)

def animation_done():
    sounds.pop.play()

def on_mouse_down(pos, button):
    # base animation time on distance
    # 1000 pixels per second
    d = ball.distance_to(pos)
    if d != 0:
        animate(ball,
            tween= 'decelerate',
            duration= d / 500,
            on_finished= animation_done,
            pos= pos)

# TRY IT YOURSELF - change the duration to a constant,
# and see how the program feels.
