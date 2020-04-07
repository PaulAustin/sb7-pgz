# To run this game type the command pgzrun mines.py into the terminal whilst in this directory

import random
import math

# Create the top tiles
cover = Actor('cover')
flag  = Actor('flag')

# Create a dictionary that stores all the possible bottom tile types
tiles = {0: Actor('blank'),
         1: Actor('one'),
         2: Actor('two'),
         3: Actor('three'),
         4: Actor('four'),
         5: Actor('five'),
         6: Actor('six'),
         7: Actor('seven'),
         8: Actor('eight'),
         'M': Actor('mine'),}

# Game Setup
CELL_SIZE = 30

# Functions
def build_grid(rows, cols, filler):
    grid = []
    for ir in range(rows):
        row = []
        for ic in range(cols):
            row.append(filler)
        grid.append(row)
    return grid

# Add mines at random locations
def place_mines(grid, rows, cols, mines):
    for mine in range(mines):
        ir = random.randint(0, rows - 1)
        ic = random.randint(0, cols - 1)
        # TODO: if too many mines this loop will never end.
        while grid[ir][ic] == 'M':
            ir = random.randint(0, rows - 1)
            ic = random.randint(0, cols - 1)
        grid[ir][ic] = 'M'
    return grid

# For each cell if it is not a mine count how many mines are near by
def count_mines(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != 'M':
                neighbors = [(x - 1, y - 1), (x    , y - 1), (x + 1, y - 1),
                             (x - 1, y    ),                 (x + 1, y    ),
                             (x - 1, y + 1), (x    , y + 1), (x + 1, y + 1)]
                for nx, ny in neighbors:
                    try:
                        if ny >= 0 and nx >= 0 and grid[ny][nx] == 'M':
                            grid[y][x] += 1
                    except:
                        pass
    return grid

# Update the board.
def draw():
    offset = -CELL_SIZE/2
    xpos, ypos = offset, offset
    for row in range(len(base_grid)):
        ypos += CELL_SIZE
        xpos = offset
        for col in range(len(base_grid[0])):
            xpos += CELL_SIZE
            gridpos = base_grid[row][col]
            tiles[gridpos].pos = xpos, ypos
            tiles[gridpos].draw()

    xpos, ypos = offset, offset
    for row in range(len(top_grid)):
        ypos += CELL_SIZE
        xpos = offset
        for col in range(len(top_grid[0])):
            xpos += CELL_SIZE
            if top_grid[row][col] == 1:
                cover.pos = xpos, ypos
                cover.draw()
            elif top_grid[row][col] == 'F':
                flag.pos = xpos, ypos
                flag.draw()


def on_mouse_down(pos, button):
    col = math.floor(pos[0]/CELL_SIZE)
    row = math.floor(pos[1]/CELL_SIZE)
    if button == mouse.LEFT:
        # Left click tests cell
        if top_grid[row][col] != 'F':
            top_grid[row][col] = 0
            if base_grid[row][col] == 0:
                edge_detection((col, row), base_grid)
    else:
        # Right/Center click adds flag
        if top_grid[row][col] == 1:
            top_grid[row][col] = 'F'
        elif top_grid[row][col] == 'F':
            top_grid[row][col] = 1

def edge_detection(gridpos, grid):
    zeros = [gridpos]
    past_zeros = []
    for zero in zeros:
        top_grid[zero[1]][zero[0]] = 0
        x, y = zero
        neighbors = [(x - 1, y - 1), (x    , y - 1), (x + 1, y - 1),
                     (x - 1, y    ),                 (x + 1, y    ),
                     (x - 1, y + 1), (x    , y + 1), (x + 1, y + 1)]
        for nx, ny in neighbors:
            try:
                if ny >= 0 and nx >= 0:
                    if grid[ny][nx] == 0 and top_grid[ny][nx] == 1:
                        if top_grid[ny][nx] != 'F':
                            top_grid[ny][nx] = 0
                        if (nx, ny) not in zeros:
                            zeros.append((nx, ny))
                    else:
                        if top_grid[ny][nx] != 'F':
                            top_grid[ny][nx] = 0

            except:
                pass
    return top_grid

# Basic game parameters
ROWS = 10
COLS = 10
MINES = 10

# Pygamezero will set the the screen based on the globals WIDTH and HEIGHT
HEIGHT = ((ROWS * CELL_SIZE) + 1)
WIDTH = ((COLS * CELL_SIZE) + 1)

# top_grid holds blanks or flags
top_grid  = build_grid(ROWS, COLS, 1)

# base_grid holds mines/numeber of adjacent/or blanks
# it is buil in three steps.
base_grid = build_grid(ROWS, COLS, 0)
base_grid = place_mines(base_grid, ROWS, COLS, MINES)
base_grid = count_mines(base_grid)