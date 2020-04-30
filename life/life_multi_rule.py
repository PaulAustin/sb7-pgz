# Conway's game of life
# uses pygamezero frame work
#
# See key event at end for commands
#

import random

ROWS = 80
COLS = 150
CELL_SIZE = 5
HEIGHT = (ROWS * CELL_SIZE)
WIDTH = (COLS * CELL_SIZE)

BACK_COLOR = (0, 0, 127)
CELL_COLOR = (0, 200, 0)

def Rule(rule):
    return [(b != '_') for b in rule]

g_rules = [
    [
        Rule('__X_X_X_X'),      # Wake up 0 Wild stuff
        Rule('_X_X_X_X_')       # Stay up
    ],[
#   This is the standard set of rules
#   How many neighboring cells
#             012345678
        Rule('___X_____'),      # Wake up 1  Standard game
        Rule('__XX_____')       # Stay up
    ],[
        Rule('___X_____'),      # Wake up 2
        Rule('__XXX____')       # Stay up
    ],[
        Rule('___X_____'),      # Wake up 3  Wiggle Bats
        Rule('___XX____')       # Stay up
    ],[
        Rule('___X_____'),      # Wake up 4  Growing Blobs
        Rule('___XXX___')       # Stay up
    ],[
        Rule('___XX____'),      # Wake up 5  Spreading Fire
        Rule('___XXX___')       # Stay up
    ],[
        Rule('___X_____'),      # Wake up 6
        Rule('__XXXX___')       # Stay up
    ],[
        Rule('__XX_____'),      # Wake up 7
        Rule('__XXXX___')       # Stay up
    ],[
        Rule('_XXX_____'),      # Wake up 8
        Rule('__XXXX___')       # Stay up
    ],[
        Rule('__X______'),      # Wake up 9  Single cycle life
        Rule('___X_____')       # Stay up
    ]]

g_rule_num = 1
g_rule = g_rules[g_rule_num]

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
    apply(grid, lambda r, c : False)

def cell_draw(r, c):
    cx = CELL_SIZE * c
    cy = CELL_SIZE * r
    cell_rect = Rect((cx, cy), (CELL_SIZE, CELL_SIZE))
    screen.draw.filled_rect(cell_rect, CELL_COLOR)
    return True

def draw():
    screen.fill(BACK_COLOR)
    apply(world, lambda r, c : (cell_draw(r, c) if world[r][c] else False))

    message = "Rule #"+ str(g_rule_num)
    message += "  (paused)" if g_step or (not g_running) else ""
    screen.draw.text(message, (20, 20))

def count_neighbors(w, r, c):
    # Count the 3x3 grid, subtract the middle and
    # trim off the edges if next to the edge of the world
    sum = 0
    for nr in range(max(r-1, 0), min(r+1, ROWS-1) + 1):
        for nc in range(max(c-1, 0), min(c+1, COLS-1) + 1):
            if w[nr][nc]:
                sum += 1
    # Loop above added the center cell, subtract it back out.
    if w[r][c]:
        sum -= 1
    return sum

def next_cell(current_world, r, c):
    n = count_neighbors(current_world, r, c)
    up = current_world[r][c]
    wakeup = g_rule[0]
    stayup = g_rule[1]
    return ((not up and wakeup[n]) or (up and stayup[n]))

def update():
    global g_running, g_step
    if not g_running:
        return
    if g_step:
        g_running = False

    # Calculate the next state, then copy back
    apply(worldNext, lambda r, c : next_cell(world, r, c))
    apply(world, lambda r, c : worldNext[r][c])

def on_mouse_down(pos, button):
    r = pos[1] // CELL_SIZE
    c = pos[0] // CELL_SIZE
    world[r][c] = not world[r][c]

def on_key_down(key, mod, unicode):
    global g_running, g_step, g_rule_num, g_rule
    if (key == keys.SPACE):
        # Freeze / thaw the clock of life
        g_running = not g_running
        g_step = False
    elif (key == keys.C):
        # Clear the world
        grid_clear(world)
    elif (key == keys.R):
        # Seed world wiht random values
        grid_random(world)
    elif (key == keys.S):
        # Make a a single generaion step
        g_running = True
        g_step = True
    elif (key >= keys.K_0 and key <= keys.K_9):
        g_rule_num = key - keys.K_0
        g_rule = g_rules[g_rule_num]


world = grid_build(ROWS, COLS)
grid_random(world)
worldNext = grid_build(ROWS, COLS)

