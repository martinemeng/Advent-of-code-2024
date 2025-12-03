def load_map(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        grid = [list(line.strip()) for line in f]
    return grid


def find_guard(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '^':
                return (i, j), 0 
    return None, None
    

def simulate_patrol(grid, start_pos=None, start_dir=0):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

    if start_pos is None:
        start_pos, start_dir = find_guard(grid)
    if start_pos is None:
        return 0, False, set()

    pos = start_pos
    direction_index = start_dir
    visited = set()
    seen = set()

    visited.add(pos)
    seen.add((pos, direction_index))

    while True:
        dx, dy = directions[direction_index]
        nx, ny = pos[0] + dx, pos[1] + dy

        if not (0 <= nx < rows and 0 <= ny < cols):
            return len(visited), False, visited  #if agent goes off-grid

        if grid[nx][ny] == '#':
            direction_index = (direction_index + 1) % 4
        else:
            pos = (nx, ny)
            if (pos, direction_index) in seen:
                return len(visited), True, visited  #True: loop detected
            seen.add((pos, direction_index))
            visited.add(pos)


def find_loop(filename):
    map = load_map(filename)
    start_pos, start_dir = find_guard(map)

    _, _, visited = simulate_patrol(map, start_pos, start_dir) #collect all the visited positions from the map

    loop_count = 0

    for i, j in visited:
        if (i, j) == start_pos:
            continue

        test_map = []
        for row in map:
            new_row = row[:]
            test_map.append(new_row)
        test_map[i][j] = '#' #place obsticle at current position

        _, is_looping, _ = simulate_patrol(test_map, start_pos, start_dir) #run simulation to see if it creates a loop

        if is_looping:
            loop_count += 1

    return loop_count


print(find_loop('Day 6/map.txt'))
