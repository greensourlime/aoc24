f = open('input.txt', 'r')

def grow(grid, row, col, already_in):
    for (n_row, n_col) in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
        if (n_row, n_col) not in already_in:                
            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                if grid[n_row][n_col] == grid[row][col]:
                    already_in.append((n_row, n_col))
                    grow(grid, n_row, n_col, already_in)

def perimeter(grid, field):   
    elem = grid[field[0][0]][field[0][1]]
    n = 0
    for tile in field:
        for (t_row, t_col) in [(tile[0]+1, tile[1]), (tile[0]-1, tile[1]), (tile[0], tile[1]+1), (tile[0], tile[1]-1)]:        
            if 0 <= t_row < len(grid) and 0 <= t_col < len(grid[0]):
                if grid[t_row][t_col] != elem:
                    n += 1 # tile exists and is different
            else:
                n += 1 # tile is out of bounds
    return n

def calc_cost(grid):
    cost = 0
    grouped = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in grouped:
                tiles = [(row, col)]
                grow(grid, row, col, tiles)
                grouped += tiles
                cost += len(tiles) * perimeter(grid, tiles)
    return cost

grid = []
for l in f.readlines():
    grid.append(list(l.strip()))

print(calc_cost(grid))