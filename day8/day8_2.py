from math import gcd
f = open('input.txt', 'r')

def locate_antennas(grid):
    antennas = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            c = grid[row][col]
            if c != ".":
                if c in antennas.keys():
                    antennas[c].append((row, col))
                else:
                    antennas[c] = [(row, col)]
    return antennas

def find_antinodes():
    antinodes = set()
    for ant_type in antennas.keys():
        for antenna_1 in antennas[ant_type]:
            for antenna_2 in antennas[ant_type]:
                if antenna_1 != antenna_2:
                    alignment = (antenna_1[0]-antenna_2[0], antenna_1[1]-antenna_2[1]) 
                    divisor = gcd(abs(alignment[0]), abs(alignment[1]))
                    step = (alignment[0]//divisor, alignment[1]//divisor)
                    steps = 0
                    while True:
                        point = (antenna_1[0] + steps * step[0], antenna_1[1] + steps * step[1])
                        if 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0]):
                            antinodes.add(point)
                        else: 
                            break
                        steps += 1
                    steps = 1
                    while True:
                        point = (antenna_1[0] - steps * step[0], antenna_1[1] - steps * step[1])
                        if 0 <= point[0] < len(grid) and 0 <= point[1] < len(grid[0]):
                            antinodes.add(point)
                        else:
                            break
                        steps += 1     
    return antinodes

grid = []
for l in f.readlines():
    grid.append(list(l.strip()))
antennas = locate_antennas(grid)

antinodes = find_antinodes()

print(len(antinodes))