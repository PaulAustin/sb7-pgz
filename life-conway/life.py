import random
import copy

ROWS = 50
COLS = 100
CELL_SIZE = 10
BACK_COLOR = 255, 255, 255
CELL_COLOR = 0, 200, 0

HEIGHT = ((ROWS+5) * CELL_SIZE)
WIDTH = ((COLS+5) * CELL_SIZE)

world = list()

def init_lives(rows, cols):
    for r in range(rows):
        row = []
        for c in range(cols):
            # Build the columns by appending cells to each row
            row.append(random.randint(0, 7) == 0)

        # Build the world one row at a time.
        world.append(row)

def draw_cell(r, c):
    cx = CELL_SIZE * c
    cy = CELL_SIZE * r
    cell_rect = Rect((cx, cy), (CELL_SIZE, CELL_SIZE))
    screen.draw.filled_rect(cell_rect, CELL_COLOR)
    return;

def draw():
    for r in range(ROWS):
        for c in range(COLS):
            if world[r][c]:
                draw_cell(r, c)

def count_neighbors(r, c):
    # count the 3x3 grid, subtrct the middle
    # trims off the edges if next to the edge of the world
    sum = 0
    for i in range(max(r-1,0), min(r+1,ROWS-1)+1):
        for j in range(max(c-1,0), min(c+1,COLS-1)+1):
            if world[i][j]:
                sum += 1
    if world[r][c]:
        sum -= 1
    return sum

def update():
    global world
    screen.clear()
    newlife = copy.deepcopy(world) # make a copy of life
    for r in range(ROWS):
        for c in range(COLS):
            k = count_neighbors(r, c)
            if k < 2 or k > 3:
                newlife[r][c] = False
            elif k == 3:
                newlife[r][c] = True
    world = copy.deepcopy(newlife) # copy back to life

def on_mouse_down(pos, button):
    print (" on mouse down")

init_lives(ROWS, COLS)
