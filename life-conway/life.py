import random

ROWS = 50
COLS = 80
CELL_SIZE = 10
BACK_COLOR = 255, 255, 255
CELL_COLOR = 0, 200, 0

HEIGHT = (ROWS * CELL_SIZE)
WIDTH = (COLS * CELL_SIZE)

def init_lives(rows, cols):
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            # Build the columns by appending cells to each row
            row.append(random.randint(0, 7) == 0)

        # Build the world one row at a time.
        grid.append(row)
    return grid

def draw_cell(r, c):
    cx = CELL_SIZE * c
    cy = CELL_SIZE * r
    cell_rect = Rect((cx, cy), (CELL_SIZE, CELL_SIZE))
    screen.draw.filled_rect(cell_rect, CELL_COLOR)
    return;

def draw():
    screen.clear()
    for r in range(ROWS):
        for c in range(COLS):
            if world[r][c]:
                draw_cell(r, c)

def count_neighbors(w, r, c):
    # count the 3x3 grid, subtrct the middle
    # trims off the edges if next to the edge of the world
    sum = 0
    for nr in range(max(r-1,0), min(r+1,ROWS-1) + 1):
        for nc in range(max(c-1,0), min(c+1,COLS-1) + 1):
            if w[nr][nc]:
                sum += 1
    if w[r][c]:
        sum -= 1
    return sum

def update():
    global worldNext, world

    # Calculate the next state
    for r in range(ROWS):
        for c in range(COLS):
            n = count_neighbors(world, r, c)
            if world[r][c]:
                worldNext[r][c] = (n == 2 or n == 3)
            else:
                worldNext[r][c] = (n == 3)

    # Move the next state back to the main grid
    for r in range(ROWS):
        for c in range(COLS):
            world[r][c] = worldNext[r][c]


def on_mouse_down(pos, button):
    print (" on mouse down")

world = init_lives(ROWS, COLS)
worldNext = init_lives(ROWS, COLS)



