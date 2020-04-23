# Example using pygame-zero actor object
# To jump use 'decelerate' to move up
# then 'accelerate' for down

BACK_COLOR = (200, 225, 255)
HEIGHT = 200
WIDTH = 400

BALL = 'ball_100x100'

ANIMATION_OPTIONS = {
    keys.K_0 : 'linear',
    keys.K_1 : 'accelerate',
    keys.K_2 : 'decelerate',
    keys.K_3 : 'accel_decel',
#   elastic mode do note appear to work in pgz bundled in mu 1.10alpha
#   keys.K_4 : 'end_elastic',
#   keys.K_5 : 'start_elastic',
#   keys.K_6 : 'both_elastic',
    keys.K_7 : 'bounce_end',
    keys.K_8 : 'bounce_start',
    keys.K_9 : 'bounce_start_end'
}

ball = Actor(BALL, (100, 100))

def draw():
    screen.fill(BACK_COLOR)
    ball.draw()

def reset_ball():
    ball.pos = (100, 100)

def animation_done():
    clock.schedule(reset_ball, 1.0)

def on_key_down(key, mod):
    tweenx = ANIMATION_OPTIONS.get(key,'')
    if (tweenx != ''):
        print(key, ANIMATION_OPTIONS[key])
        animate(ball,
            tween= tweenx,
            duration= 1.0,
            on_finished= animation_done,
            pos= (300, 100))
