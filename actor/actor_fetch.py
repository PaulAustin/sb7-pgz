# Example using pygame-zero actor object
# move the ball to where the mouse is clicked
# with the pgz animation function

BACK_COLOR = (200, 225, 255)
HEIGHT = 300
WIDTH = 500
BALL = 'ball_64x64'
DOG2 = 'dog2_100x100'

ball = Actor(BALL, (100, 100))
dog = Actor(DOG2, (100, 100))

def draw():
    screen.fill(BACK_COLOR)
    dog.draw()
    ball.draw()

def on_mouse_down(pos, button):
    # base animation time on distance
    # 1000 pixels per second
    d = ball.distance_to(pos)

    if d != 0:
        dog.angle = dog.angle_to(pos) + 90

        # Throw the ball
        animate(ball,
            tween= 'decelerate',
            duration= d / 5000,
            on_finished= (lambda: sounds.pop.play()),
            pos= pos)

        # Start dog running at 1/4 the speed
        animate(dog,
            tween= 'decelerate',
            duration= d / 100,
            on_finished= (lambda: sounds.bark.play()),
            pos= pos)
