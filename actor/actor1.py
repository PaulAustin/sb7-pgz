# Example using pygame-zero actor object
import pgzero
print(pgzero.__version__)

BACK_COLOR = (200, 220, 255)
BACK_COLOR_CLOSE = (170, 170, 255)
CELL_COLOR = (0, 200, 0)
HEIGHT = 200
WIDTH = 400

DOG  = 'dog2_100x100'
BALL = 'ball_100x100'

dog = Actor(BALL, (200,100))
ball = Actor(DOG, (200,100))
close = False

def on_mouse_move(pos):
    global close
    dog.angle = dog.angle_to(pos) + 90
    ball.pos = pos
    close = dog.distance_to(ball) < 50

def on_mouse_down(pos):
    if close:
        sounds.pop.play()
    else:
        sounds.bark.play()

def draw():
    bcolor = BACK_COLOR_CLOSE if close else BACK_COLOR
    screen.fill(bcolor)

    ball.draw()
    dog.draw()
    screen.draw.text("Angle = " + str(int(dog.angle)),(20,20))
    screen.draw.text("Distance = " + str(int(dog.distance_to(ball))), (20,40))
    screen.draw.line(dog.pos, ball.pos, (0,255,0))

def update():
    if keyboard.left:
        ball.x -= 1
    elif keyboard.right:
        ball.x += 1
    elif keyboard.up:
        ball.angle -= 1
    elif keyboard.down:
        ball.angle += 1

