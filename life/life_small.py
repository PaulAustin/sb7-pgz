# Conway's game of life (no frills version)

import random

ROWS = 50
COLS = 70
CELL_SIZE = 10
HEIGHT = (ROWS * CELL_SIZE)
WIDTH = (COLS * CELL_SIZE)
BACK_COLOR = (0, 0, 127)
CELL_COLOR = (0, 200, 0)

def Rule(rule): return [(b != '_') for b in rule]
WAKEUP = Rule('___X_____')
KEEPUP = Rule('__XX_____')

def grid_build(rows, cols):
    return [[False for c in range(cols)] for r in range(rows)]

def apply(grid, func):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] = func(r, c)

def grid_random(grid):
    apply(grid, lambda r, c : (random.randint(0, 7) == 0))

def cell_draw(r, c):
    xy = (CELL_SIZE * c, CELL_SIZE * r)
    cell_rect = Rect(xy, (CELL_SIZE, CELL_SIZE))
    screen.draw.filled_rect(cell_rect, CELL_COLOR)
    return True

def draw():
    screen.fill(BACK_COLOR)
    apply(world, lambda r, c : (cell_draw(r, c) if world[r][c] else False))

def count_neighbors(w, r, c):
    sum = -1 if w[r][c] else 0
    for nr in range(max(r-1, 0), min(r+1, ROWS-1) + 1):
        for nc in range(max(c-1, 0), min(c+1, COLS-1) + 1):
            if w[nr][nc]:
                sum += 1
    return sum

def next_cell(current_world, r, c):
    n = count_neighbors(current_world, r, c)
    up = current_world[r][c]
    return ((not up and WAKEUP[n]) or (up and KEEPUP[n]))

def update():
    apply(worldNext, lambda r, c : next_cell(world, r, c))
    apply(world, lambda r, c : worldNext[r][c])

world = grid_build(ROWS, COLS)
grid_random(world)
worldNext = grid_build(ROWS, COLS)
