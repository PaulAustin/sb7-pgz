import random

ROWS = 50
COLS = 80
CELL_SIZE = 10
HEIGHT = (ROWS * CELL_SIZE)
WIDTH = (COLS * CELL_SIZE)

BACK_COLOR = 255, 255, 255
CELL_COLOR = (0, 200, 0)

g_changed = False
g_delay = 0
g_tics  = 0
g_paused = False

def grid_clear(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = False

def grid_random(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = random.randint(0, 7) == 0

def grid_build(rows, cols):
    return [[False for c in range(cols)] for r in range(rows)]

def draw_cell(r, c):
    cx = CELL_SIZE * c
    cy = CELL_SIZE * r
    cell_rect = Rect((cx, cy), (CELL_SIZE, CELL_SIZE))
    screen.draw.filled_rect(cell_rect, CELL_COLOR)
    return;

def draw():
    global g_changed
    if not g_changed:
        return
    g_changed = False

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
    # Loop above added the center cell, subtract it back out.
    if w[r][c]:
        sum -= 1
    return sum

def update():
    global g_changed
    if g_paused:
        return
    g_changed = True

    # Calculate the next state
    for r in range(ROWS):
        for c in range(COLS):
            n = count_neighbors(world, r, c)
            if world[r][c]:
                # Live cell stays alive if not lonely or crowded
                worldNext[r][c] = (n >= 2 and  n <= 3)
            else:
                # Open cell springs to life if three nearby
                worldNext[r][c] = (n == 3)

    # Move the next state back to the main grid
    for r in range(ROWS):
        for c in range(COLS):
            world[r][c] = worldNext[r][c]

def on_mouse_down(pos, button):
    global g_changed
    r = pos[1] // CELL_SIZE
    c = pos[0] // CELL_SIZE
    world[r][c] = not world[r][c]
    g_changed = True

def on_key_down(key,mod,unicode):
    global g_paused
    if (key == keys.SPACE):
        g_paused = not g_paused
    if (key == keys.C):
        grid_clear(world)
    if (key == keys.R):
        grid_random(world)

world = grid_build(ROWS, COLS)
grid_random(world)
worldNext = grid_build(ROWS, COLS)



