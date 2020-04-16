import random
import copy

ROWS = 50
COLS = 50
CELL_SIZE = 10
BACK_COLOR = 255, 255, 255
CELL_COLOR = 0, 200, 0

HEIGHT = ((ROWS * CELL_SIZE) + 1)
WIDTH = ((COLS * CELL_SIZE) + 1)

def draw_grid(rows, cols): # this function draws nxn grid
    turtle.pencolor('gray')
    turtle.pensize(3)
    x = -400
    for i in range(rows):
        draw_line(x,-400,x,400)
        x += 800/n
    y = -400
    for i in range(cols):
        draw_line(-400,y,400,y)
        y += 800/n

life = list() # create an empty list
def init_lives(rows, cols):
    for i in range(rows):
        liferow = [] # a row of lives
        for j in range(cols):
            # 1/7 probability of life
            if random.randint(0, 7) == 0:
                liferow.append(1) # 1 means life
            else:
                liferow.append(0) # 0 means no life
        life.append(liferow) # add a row to the life list -> life is a list of list

def draw_square(x,y,size): # draws a filled square
    lifeturtle.up()
    lifeturtle.goto(x,y)
    lifeturtle.down()
    lifeturtle.seth(0)
    lifeturtle.begin_fill()
    for i in range(4):
        lifeturtle.fd(size)
        lifeturtle.left(90)
    lifeturtle.end_fill()


def draw_cell(x, y): # draws life in (x, y)
    cx = CELL_SIZE * x
    cy = CELL_SIZE * y
    cell_rect = Rect((cx, cy), (CELL_SIZE, CELL_SIZE))
    screen.draw.filled_rect(cell_rect, CELL_COLOR)
    return;

def draw():
    for i in range(ROWS):
        for j in range(COLS):
            if life[i][j] == 1:
                draw_cell(i,j)

def on_mouse_down(pos, button):
    print (" on mouse down")

def update():
    screen.clear()
    update_life()

def num_neighbors(x,y): # computes the number of life neighbours for cell[x,y]
    sum = 0
    for i in range(max(x-1,0), min(x+1,ROWS-1)+1):
        for j in range(max(y-1,0), min(y+1,COLS-1)+1):
            sum += life[i][j]
    return sum - life[x][y]

def update_life(): # update life for each cycle
    global life
    newlife = copy.deepcopy(life) # make a copy of life
    for r in range(ROWS):
        for c in range(COLS):
            k = num_neighbors(r, c)
            if k < 2 or k > 3:
                newlife[r][c] = 0
            elif k == 3:
                newlife[r][c] = 1
    life = copy.deepcopy(newlife) # copy back to life


init_lives(ROWS, COLS)

