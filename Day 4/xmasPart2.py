def count_xmas(filename):
    grid = []

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            grid.append(line.strip())

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    patterns = [
        ("M", "S", "M", "S"),  # M-S arm
        ("M", "M", "S", "S"),  # M-M arm
        ("S", "M", "S", "M"),  # S-M arm
        ("S", "S", "M", "M"),  # S-S arm
    ]

    def check_x_mas(x, y):
        """Check if an 'A' at (x, y) forms an X-MAS pattern."""
        for pattern in patterns:
                if (
                    grid[x - 1][y - 1] == pattern[0] and  # Top-left
                    grid[x - 1][y + 1] == pattern[1] and  # Top-right
                    grid[x + 1][y - 1] == pattern[2] and  # Bottom-left
                    grid[x + 1][y + 1] == pattern[3]      # Bottom-right
                ):
                    return True
        return False

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if grid[x][y] == "A" and check_x_mas(x, y):
                count += 1

    return count


print(count_xmas('Day 4/xmas.txt'))
