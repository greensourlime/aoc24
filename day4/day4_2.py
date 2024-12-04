f = open('input.txt', 'r')

def check_corners(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for row in range(1, rows - 1): # ignore the edges
        for col in range(1, cols - 1):
            if grid[row][col] == 'A':
                one = [grid[row - 1][col - 1], grid[row + 1][col + 1]]
                two = [grid[row - 1][col + 1], grid[row + 1][col - 1]]
                
                if 'M' in one and 'S' in one and 'M' in two and 'S' in two:
                    count += 1

    return count

grid = []
for l in f.readlines():
    grid.append(list(l.strip()))

print(check_corners(grid))
