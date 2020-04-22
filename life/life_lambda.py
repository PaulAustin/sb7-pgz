# Conway's game of life
# uses pygamezero frame work
#
# See key event at end for commands
#

import random

ROWS = 50
COLS = 70
CELL_SIZE = 10
HEIGHT = (ROWS * CELL_SIZE)
WIDTH = (COLS * CELL_SIZE)

BACK_COLOR = (0, 0, 127)
CELL_COLOR = (0, 200, 0)

g_changed = False
g_running = True
g_step = False

def grid_build(rows, cols):
    return [[False for c in range(cols)] for r in range(rows)]

def apply(grid, func):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] = func(r, c)

def grid_random(grid):
    apply(grid, lambda r, c : (random.randint(0, 7) == 0))

def grid_clear(grid):
    apply(grid, lambda : False)

def cell_draw(r, c):
    cx = CELL_SIZE * c
    cy = CELL_SIZE * r
    cell_rect = Rect((cx, cy), (CELL_SIZE, CELL_SIZE))
    screen.draw.filled_rect(cell_rect, CELL_COLOR)
    return True

def draw():
    global g_changed
    if not g_changed:
        return
    g_changed = False

    screen.fill(BACK_COLOR)
    apply(world, lambda r, c : (cell_draw(r, c) if world[r][c] else False))

def count_neighbors(w, r, c):
    # count the 3x3 grid, subtrct the middle
    # trims off the edges if next to the edge of the world
    sum = -1 if w[r][c] else 0
    for nr in range(max(r-1, 0), min(r+1, ROWS-1) + 1):
        for nc in range(max(c-1, 0), min(c+1, COLS-1) + 1):
            if w[nr][nc]:
                sum += 1
    # Loop above added the center cell, subtract it back out.
    return sum

def next_cell(current_world, r, c):
    n = count_neighbors(current_world, r, c)
    if current_world[r][c]:
        # Live cell stays alive if not lonely or crowded
        return (n >= 2 and n <= 3)
    else:
        # Open cell springs to life if three nearby
        return (n == 3)

def update():
    # Look at globals that control the speed
    global g_running, g_changed, g_step
    if not g_running:
        return
    if g_step:
        g_running = False
    g_changed = True

    # Calculate the next state, then copy back
    apply(worldNext, lambda r, c : next_cell(world, r, c))
    apply(world, lambda r, c : worldNext[r][c])

def on_mouse_down(pos, button):
    global g_changed
    r = pos[1] // CELL_SIZE
    c = pos[0] // CELL_SIZE
    world[r][c] = not world[r][c]
    g_changed = True

def on_key_down(key, mod, unicode):
    global g_running, g_step, g_changed
    if (key == keys.SPACE):
        # Freeze / thaw the clock of life
        g_running = not g_running
        g_step = False
    if (key == keys.C):
        # Clear the world
        grid_clear(world)
        g_changed = True
    if (key == keys.R):
        # Seed world wiht random values
        grid_random(world)
        g_changed = True
    if (key == keys.S):
        # Make a a single generaion step
        g_running = True
        g_step = True

world = grid_build(ROWS, COLS)
grid_random(world)
worldNext = grid_build(ROWS, COLS)

