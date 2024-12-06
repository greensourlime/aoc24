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

def walk_test(): 
    path = []
    guard_x, guard_y, guard_dir = find_dude()
    if guard_x == -1:
        return 0    
    path.append((guard_x, guard_y, guard_dir))

    while True:
        dir_x, dir_y = dirs[guard_dir]
        next_x, next_y = guard_x + dir_x, guard_y + dir_y
        # puede que el siguiente paso le saque del mapa
        if not (0 <= next_x < len(guard_map) and 0 <= next_y < len(guard_map[0])):
            return 0
        # o puede que sea un obstaculo
        if guard_map[next_x][next_y] == "#":
            guard_dir = next_dir(guard_dir)
        # y si no, es X o .
        else:
            guard_x, guard_y = next_x, next_y            
            if (guard_x, guard_y, guard_dir) in path:
                return 1
            path.append((guard_x, guard_y, guard_dir))
    
    return 0 # no va a pasar nunca

def walk_unaltered(): 
    path = set()
    guard_x, guard_y, guard_dir = find_dude()
    if guard_x == -1:
        return path    
    path.add((guard_x, guard_y))

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
            guard_x, guard_y = next_x, next_y
            path.add((guard_x, guard_y))
    return path

guard_map = []
for l in f.readlines():
    guard_map.append((list(l.strip())))

# original_guard_map = [row[:] for row in guard_map]
original_path = walk_unaltered()
start_point = find_dude()
loop_count = 0
for tile in original_path: 
    if (start_point[0], start_point[1]) == (tile[0], tile[1]): # to skip the initial position where the guard is
        continue
    guard_map[tile[0]][tile[1]] = "#"
    loop_count += walk_test()
    guard_map[tile[0]][tile[1]] = "."

print(loop_count)