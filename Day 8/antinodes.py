def load_map(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [list(line.rstrip()) for line in f]

def find_antennas(grid):
    antennas = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '.':
                antennas.setdefault(cell, []).append((x, y))
    return antennas

def in_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height

def compute_antinodes(grid):
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0
    antennas = find_antennas(grid)
    antinodes = set()

    for _, positions in antennas.items():
        for i in range(len(positions)):
            x1, y1 = positions[i]
            for j in range(len(positions)):
                if i == j:
                    continue
                x2, y2 = positions[j]

                dx = x2 - x1
                dy = y2 - y1

                mx = x1 + dx * 2
                my = y1 + dy * 2
                ax = x1 - dx
                ay = y1 - dy

                if in_bounds(mx, my, width, height):
                    antinodes.add((mx, my))
                if in_bounds(ax, ay, width, height):
                    antinodes.add((ax, ay))
    return len(antinodes)


filename = "Day 8/map.txt" 
grid = load_map(filename)
result = compute_antinodes(grid)
print(f"Total antinode positions within bounds: {result}")
