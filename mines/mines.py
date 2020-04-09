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

# Basic game parameters
ROWS = 15
COLS = 15
MINES = 10

# Build a list of lists
def build_grid(rows, cols, filler):
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(filler)
        grid.append(row)
    return grid

# Add mines at random locations
def place_mines(grid, mines):
    # Attempt to place n mines, if one already placed
    # try again, but only so many attempts
    # loop will alwasy exit.
    max_tries = len(grid) * len(grid[0]) * 2
    while mines > 0 and max_tries > 0 :
        r = random.randint(0, len(grid) - 1)
        c = random.randint(0, len(grid[0]) - 1)
        if grid[r][c] != 'M' :
            grid[r][c] = 'M'
            mines -= 1
        else:
            max_tries -= 1
            continue

    # return True if all placed.
    return mines == 0


# Build a list neighbors omitting ones off the edge
def list_of_neighbors(grid, r, c):
    neighbors = []
    for rn in range(max(0,r-1), min(r+2,len(grid))):
        for cn in range(max(0,c-1), min(c+2,len(grid[0]))):
            if rn != r or cn != c :
                # Ignore the center, append all others
                neighbors.append((rn,cn))
    return neighbors

# For each cell if it is not a mine count how many mines are nearby
def count_mines(grid):
    # For each cell that has a mine, increment the cells around it.
    # so long as they are not mines them selves.
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'M':
                inc_neighbors(grid, r, c)
    return

# Increment all mine neighbors
def inc_neighbors(grid, r, c):
    # Inc all cells next to the mine
    for r, c in list_of_neighbors(grid, r, c) :
        if grid[r][c] != 'M':
            grid[r][c] += 1
    return

# Update the board.
def draw():
    offset = -CELL_SIZE/2
    xpos, ypos = offset, offset
    for row in range(len(top_grid)):
        ypos += CELL_SIZE
        xpos = offset
        for col in range(len(top_grid[0])):
            xpos += CELL_SIZE
            if top_grid[row][col] == 1:
                # Its still hidden
                cover.pos = xpos, ypos
                cover.draw()
            elif top_grid[row][col] == 'F':
                # Its a flag
                flag.pos = xpos, ypos
                flag.draw()
            else:
                # top is gone, show the base layer
                gridpos = base_grid[row][col]
                tiles[gridpos].pos = xpos, ypos
                tiles[gridpos].draw()
    return

def on_mouse_down(pos, button):

    # map x y pixel location to row/col in grid
    r = math.floor(pos[1]/CELL_SIZE)
    c = math.floor(pos[0]/CELL_SIZE)

    if button == mouse.LEFT:
        # Left click tests cell
        if top_grid[r][c] != 'F':
            top_grid[r][c] = 0
            if base_grid[r][c] == 0:
                flood_fill(base_grid, (r, c))
            elif base_grid[r][c] == 'M' :
                print("sunk your battleship")
                # PLay a sound of a sin skip
    else:
        # Right/Center click adds flag
        if top_grid[r][c] == 1:
            top_grid[r][c] = 'F'
        elif top_grid[r][c] == 'F':
            top_grid[r][c] = 1

def flood_fill(grid, seedpos):
    # Make a queue of cleared cells to look at begining with
    # the seed point, visit neighbors and add to the queue
    zcells = [seedpos]
    for r, c in zcells:
        neighbors = list_of_neighbors(grid, r, c)
        for nr, nc in neighbors:
            if grid[nr][nc] == 0 and top_grid[nr][nc] == 1 :
                # If this cell has no near mines and
                # and it is still hidden, then..
                if top_grid[nr][nc] != 'F':
                    # Not a flag, reove cover
                    top_grid[nr][nc] = 0

                if (nr, nc) not in zcells:
                    zcells.append((nr, nc))

            elif top_grid[nr][nc] != 'F':
                # Show the count on the edge the area cleared
                top_grid[nr][nc] = 0
    return

# Pygamezero will set the the screen based on the globals WIDTH and HEIGHT
HEIGHT = ((ROWS * CELL_SIZE) + 1)
WIDTH = ((COLS * CELL_SIZE) + 1)

# top_grid holds blanks or flags
top_grid  = build_grid(ROWS, COLS, 1)

# base_grid holds mines/numeber of adjacent/or blanks
# it is buil in three steps.
base_grid = build_grid(ROWS, COLS, 0)
place_mines(base_grid, MINES)
count_mines(base_grid)