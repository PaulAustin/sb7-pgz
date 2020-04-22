# Example using pygame zero actor

BACK_COLOR = (200, 220, 255)
CELL_COLOR = (0, 200, 0)
HEIGHT = 200
WIDTH = 400

DOG  = 'dog2_100x100'
BALL = 'ball_100x100'

dog = Actor(BALL, (200,100))
ball = Actor(DOG, (200,100))

def draw():
    screen.fill(BACK_COLOR)
    ball.draw()
    dog.draw()
    screen.draw.text("Angle = " + str(int(dog.angle)),(20,20))
    screen.draw.text("Distance = " + str(int(dog.distance_to(ball))),(20,40))

def update():
    if keyboard.left:
        ball.x -= 1
    elif keyboard.right:
        ball.x += 1
    elif keyboard.up:
        ball.angle -= 1
    elif keyboard.down:
        ball.angle += 1

def on_mouse_move(pos):
    dog.angle = dog.angle_to(pos) + 90
    ball.pos = pos
