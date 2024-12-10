f = open('input.txt', 'r')

def nines(grid, pos, all_nines):
    if height(grid, pos) == 9:
        all_nines.append(pos)
        return

    for m in moves(grid, pos):
        if height(grid, m) == height(grid, pos) +1:
            nines(grid, m, all_nines)

def moves(grid, pos):
    all = []
    if pos[0] - 1 >= 0:
        all.append((pos[0]-1, pos[1]))
    if pos[0] + 1 < len(grid):
        all.append((pos[0]+1, pos[1]))
    if pos[1] - 1 >= 0:
        all.append((pos[0],pos[1]-1))
    if pos[1] + 1 < len(grid[0]):
        all.append((pos[0],pos[1]+1))
    return all

def height(grid, pos):
    return grid[pos[0]][pos[1]]

grid = []
for l in f.readlines():
    grid.append(list(map(int, list(l.strip()))))

score = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 0:
            peaks = []
            nines(grid, (r, c), peaks)
            score += len(peaks)

print(score)