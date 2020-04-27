# Example using pygame-zero actor object
# To jump use 'decelerate' to move up
# then 'accelerate' for down

BACK_COLOR = (200, 225, 255)
HEIGHT = 200
WIDTH = 400

DOG1 = 'dog1_100x100'
DOG2 = 'dog2_100x100'
BALL = 'ball_64x64'

GROUND_Y = 150
JUMP_T   = 0.4
JUMP_Y   = 100

class Game:
    def __init__(self):
        self.dog = Actor(DOG2, (200, GROUND_Y))
        self.ani_obj = None
        self.jumping = False
        self.flip_direction = 1

    def on_update(self):
        if keyboard.space and self.ani_obj == None:
            # Start the jump by moving up
            # slowing as it gets to the peak
            self.jumping = True
            self.ani_obj = animate(self.dog,
                tween='decelerate',
                duration = JUMP_T,
                on_finished = animation_done,
                pos = (200, GROUND_Y - JUMP_Y))

            # A second animation does a flip
            # This one is set to be twice as long
            # The the jump is split into two parts
            animate(self.dog,
                tween='linear',
                duration = JUMP_T * 2,
                on_finished = None,
                angle = 360 * self.flip_direction)
            sounds.bark.play()
            self.flip_direction *= -1

    def on_draw(self):
        screen.fill(BACK_COLOR)
        screen.draw.text("Angle = " + str(int(self.dog.angle)),(20,20))
        screen.draw.text("Pos = " + str(int(self.dog.pos[1])),(20,40))
        self.dog.draw()

    def on_ani_done(self):
        self.ani_obj = None
        if self.jumping:
            # Finish the jump by moving down
            # starting slowing the speeding up
            self.ani_obj = animate(self.dog,
                tween='accelerate',
                duration = JUMP_T,
                on_finished = animation_done,
                pos = (200, GROUND_Y))
            self.jumping = False
        else:
            # Reset the angle so next fil will work
            self.dog.angle = 0
            sounds.pop.play()


game = Game()

def draw(): game.on_draw()

def update(): game.on_update()

def animation_done(): game.on_ani_done()

