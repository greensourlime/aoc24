f = open('input.txt', 'r')

def search_directions(grid):
    rows = len(grid)
    cols = len(grid[0])

    count = 0
    # horizontal
    for row in range(rows):
        churro = "".join(grid[row][col] for col in range(cols))        
        count += churro.count("XMAS")
        count += churro[::-1].count("XMAS") 

    # vertical
    for col in range(cols):
        churro = "".join(grid[row][col] for row in range(rows))
        count += churro.count("XMAS")
        count += churro[::-1].count("XMAS") 

    # diagonal \
    for row in range(rows):
        churro = "".join(grid[row + col][col] for col in range(min(cols, rows-row)))
        count += churro.count("XMAS")
        count += churro[::-1].count("XMAS") 
    for col in range (1, cols):
        churro = "".join(grid[row][col + row] for row in range(min(rows, cols-col)))
        count += churro.count("XMAS")
        count += churro[::-1].count("XMAS") 

    # diagonal /
    for row in range(rows):
        churro = "".join(grid[row - col][col] for col in range(min(cols, row+1)))
        count += churro.count("XMAS")
        count += churro[::-1].count("XMAS") 
    for col in range(1, cols):
        churro = "".join(grid[rows -1 -row][col+row] for row in range(min(rows, cols-col)))
        count += churro.count("XMAS")
        count += churro[::-1].count("XMAS") 

    return count   

grid = []
for l in f.readlines():
    grid.append(list(l.strip()))

print(search_directions(grid))
