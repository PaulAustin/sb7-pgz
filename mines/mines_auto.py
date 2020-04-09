def computer_move(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            num_ones = 0
            for n in list_of_neighbors(grid, r, c) :
                if grid[r][c] == '1':
                    numones +=1
            if num_ones == 8:
                set_flag(r,c)
    return

