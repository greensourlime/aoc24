f = open('input.txt', 'r')

dirs = {
    "^": (-1, 0),  # arriba
    ">": (0, 1),   # derecha
    "v": (1, 0),   # abajo
    "<": (0, -1)   # izquierda
}

def next_dir(from_dir):
    if from_dir == "^":
        return ">"
    if from_dir == ">":
        return "v"
    if from_dir == "v":
        return "<"
    if from_dir == "<":
        return "^"

def find_dude():
    for i, row in enumerate(guard_map):
        for j, pos in enumerate(row):
            if pos in "^>v<":
                return i, j, pos
    return -1, -1, -1 # nunca pasa esto

def walk():
    guard_x, guard_y, guard_dir = find_dude()
    if guard_x == -1:
        return 0    
    guard_map[guard_x][guard_y] = "X"

    while True:
        dir_x, dir_y = dirs[guard_dir]
        next_x, next_y = guard_x + dir_x, guard_y + dir_y
        # puede que el siguiente paso le saque del mapa
        if not (0 <= next_x < len(guard_map) and 0 <= next_y < len(guard_map[0])):
            break
        # o puede que sea un obstaculo
        if guard_map[next_x][next_y] == "#":
            guard_dir = next_dir(guard_dir)
        # y si no, es X o .
        else:
            guard_map[next_x][next_y] = "X"
            guard_x, guard_y = next_x, next_y


guard_map = []
for l in f.readlines():
    guard_map.append((list(l.strip())))

walk()
print(sum(row.count("X") for row in guard_map))