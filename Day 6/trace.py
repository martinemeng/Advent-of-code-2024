def load_map(filename):
    with open(filename,'r',encoding='utf-8') as f:
        grid = [list(line.strip()) for line in f.readlines()]
        #print(grid)
    return grid


def find_guard(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '^':
                return (i,j), 0
            
    return None, None
    

def simulate_patrol(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    pos, direction_index = find_guard(grid)

    if pos is None:
        return 0

    visited = set()
    visited.add(pos)

    grid[pos[0]][pos[1]] = 'X'

    while True:
        dx, dy = directions[direction_index]
        nx, ny = pos[0] + dx, pos[1] + dy

        if not (0 <= nx < rows and 0 <= ny < cols):
            break
        
        if grid[nx][ny] == '#':
            direction_index = (direction_index + 1) % 4
        else:
            pos = (nx, ny)
            visited.add(pos)
            grid[nx][ny] = 'X'

    return len(visited)


map = load_map('Day 6/map.txt')
print(simulate_patrol(map))
