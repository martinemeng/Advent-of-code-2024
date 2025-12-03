def count_xmas(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        grid = []
        for line in f:
            grid.append(line.strip())

    rows = len(grid)
    cols = len(grid[0])
    target = "XMAS"
    target_length = len(target)
    count = 0

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)   
    ]

    def check(x, y, dx, dy):
        for i in range(target_length):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != target[i]:
                return False
        return True

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check(x, y, dx, dy):
                    count += 1

    return count

print(count_xmas('Day 4/xmas.txt'))
