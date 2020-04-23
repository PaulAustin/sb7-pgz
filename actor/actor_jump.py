# Example using pygame-zero actor object
# To jump use 'decelerate' to move up
# then 'accelerate' for down

BACK_COLOR = (200, 225, 255)
HEIGHT = 200
WIDTH = 400

DOG1 = 'dog1_100x100'
DOG2 = 'dog2_100x100'
BALL = 'ball_100x100'

GROUND_Y = 150
JUMP_T   = 0.4
JUMP_Y   = 100

class Game:
    def __init__(self):
        self.dog = Actor(DOG2, (200, GROUND_Y))
        self.ani_obj = None
        self.tween = "jump"
        self.jumping = False

    def on_update(self):
        if keyboard.space and self.ani_obj == None:
            self.jumping = True
            self.ani_obj = animate(self.dog,
                tween='decelerate',
                duration = JUMP_T,
                on_finished = animation_done,
                pos = (200, GROUND_Y - JUMP_Y))
            sounds.bark.play()

    def on_draw(self):
        screen.fill(BACK_COLOR)
        self.dog.draw()

    def on_ani_done(self):
        self.ani_obj = None
        if self.jumping:
            self.ani_obj = animate(self.dog,
                tween='accelerate',
                duration = JUMP_T,
                on_finished = animation_done,
                pos = (200, GROUND_Y))
            self.jumping = False
        else:
            sounds.pop.play()


game = Game()

def draw(): game.on_draw()

def update(): game.on_update()

def animation_done(): game.on_ani_done()

