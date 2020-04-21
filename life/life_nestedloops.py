# Conway's game of life
# uses pygamezero frame work
#
# See key event handler at end for commands
#

import random

# Game setup
ROWS = 100
COLS = 140
CELL_SIZE = 5
BACK_COLOR = (0, 0, 127)
CELL_COLOR = (0, 255, 0)

# The globals HEIGHT & WIDTH are used by pygamezero
HEIGHT = (ROWS * CELL_SIZE)
WIDTH = (COLS * CELL_SIZE)

g_changed = False
g_running = True
g_step = False

def grid_build(rows, cols):
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(False)
        grid.append(row)
    return grid

def grid_clear(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = False

def grid_random(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = random.randint(0, 7) == 0

def cell_draw(r, c):
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

    screen.fill(BACK_COLOR)
    for r in range(len(g_world)):
        for c in range(len(g_world[0])):
            if g_world[r][c]:
                cell_draw(r, c)

def count_neighbors(w, r, c):
    # count the 3x3 grid, subtract the middle
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
    # Look at globals that control the speed
    global g_running, g_changed, g_step
    if not g_running:
        return
    if g_step:
        g_running = False
    g_changed = True

    # Calculate the next state
    for r in range(ROWS):
        for c in range(COLS):
            n = count_neighbors(g_world, r, c)
            if g_world[r][c]:
                # Live cell stays alive if not lonely or crowded
                g_worldNext[r][c] = (n >= 2 and  n <= 3)
            else:
                # Open cell springs to life if three nearby
                g_worldNext[r][c] = (n == 3)

    # Move the next state back to the main grid
    for r in range(ROWS):
        for c in range(COLS):
            g_world[r][c] = g_worldNext[r][c]

def on_mouse_down(pos, button):
    global g_changed
    r = pos[1] // CELL_SIZE
    c = pos[0] // CELL_SIZE
    g_world[r][c] = not g_world[r][c]
    g_changed = True

def on_key_down(key, mod, unicode):
    global g_running, g_step, g_changed
    if (key == keys.SPACE):
        # Freeze / thaw the clock of life
        g_running = not g_running
        g_step = False
    if (key == keys.C):
        # Clear the world
        grid_clear(g_world)
        g_changed = True
    if (key == keys.R):
        # Seed world with random values
        grid_random(g_world)
        g_changed = True
    if (key == keys.S):
        # Make a a single generaion step
        g_running = True
        g_step = True

# Initialize the game then let pygamezero run the program
g_world = grid_build(ROWS, COLS)
grid_random(g_world)
g_worldNext = grid_build(ROWS, COLS)
