f = open('input.txt', 'r')

def grow(grid, row, col, already_in):
    for (n_row, n_col) in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
        if (n_row, n_col) not in already_in:                
            if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]):
                if grid[n_row][n_col] == grid[row][col]:
                    already_in.append((n_row, n_col))
                    grow(grid, n_row, n_col, already_in)

def sides(grid, field):
    elem = grid[field[0][0]][field[0][1]]
    outward_corners = 0
    inward_corners = 0

    for tile in field:
        edge_up = False
        if tile[0]-1 < 0 or grid[tile[0]-1][tile[1]] != elem:
            edge_up = True
        edge_down = False
        if tile[0]+1 >= len(grid) or grid[tile[0]+1][tile[1]] != elem:
            edge_down = True
        edge_left = False
        if tile[1]-1 < 0 or grid[tile[0]][tile[1]-1] != elem:
            edge_left = True
        edge_right = False
        if tile[1]+1 >= len(grid[0]) or grid[tile[0]][tile[1]+1] != elem:
            edge_right = True
        
        edge_count = sum([edge_up, edge_down, edge_right, edge_left])
        if edge_count > 1:
            # Hay al menos 2 bordes, pueden existir esquinas
            if edge_count == 4:
                # 4 bordes es un cuadro cerrado
                outward_corners += 4
            elif edge_count == 3: 
                # con 3 bordes siempre habra 2 esquinas
                outward_corners += 2
            elif edge_up != edge_down and edge_left != edge_right:
                # hay 2 bordes y no son paralelos, luego forman 1 esquina
                outward_corners += 1
      
    # se acabaria aqui la historia de una forma muy bonita si las figuras fuesen cerradas! pero pueden tener otras figuras dentro
    # return (outward_corners * 2) - 4 

        if edge_up and tile[0] - 1 >= 0: # hay borde arriba y no termina ahi el mapa
            if not edge_right: # para una esquina inward, hace falta un elemento en la esquina, seria el vecino 
                if grid[tile[0]-1][tile[1]+1] == elem: # _|
                    inward_corners += 1
            if not edge_left: 
                if grid[tile[0]-1][tile[1]-1] == elem: # |_
                    inward_corners += 1
        if edge_down and tile[0] + 1 < len(grid):
            if not edge_right:
                if grid[tile[0]+1][tile[1]+1] == elem:
                    inward_corners += 1
            if not edge_left: 
                if grid[tile[0]+1][tile[1]-1] == elem:
                    inward_corners += 1

    return outward_corners + inward_corners

def calc_cost(grid):
    cost = 0
    grouped = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in grouped:
                tiles = [(row, col)]
                grow(grid, row, col, tiles)
                grouped += tiles
                cost += len(tiles) * sides(grid, tiles)
    return cost

grid = []
for l in f.readlines():
    grid.append(list(l.strip()))

print(calc_cost(grid))