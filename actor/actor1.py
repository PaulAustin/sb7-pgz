# Example using pygame-zero actor object

BACK_COLOR = (200, 220, 255)
BACK_COLOR_CLOSE = (170, 170, 255)
HEIGHT = 200
WIDTH = 400

DOG1 = 'dog1_100x100'
DOG2 = 'dog2_100x100'
BALL = 'ball_100x100'

dog = Actor(DOG2, (200,100))
ball = Actor(BALL, (200,100))
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
        dog.x -= 2
    elif keyboard.right:
        dog.x += 2
