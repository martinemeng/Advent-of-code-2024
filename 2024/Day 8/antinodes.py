from math import gcd

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

def normalize(dx, dy):
    g = gcd(dx,dy)
    return (dx // g, dy // g)

def compute_antinodes(grid):
    height = len(grid)
    if height > 0:
        width = len(grid[0])
    else:
        width = 0
    # antennas = find_antennas(grid)
    antinodes = set()

    antennas = {}
    for y in range(height):
        for x in range(width):
            cell = grid[y][x]
            if cell != '.':
                antennas.setdefault(cell, []).append((x,y))

    for freq, points in antennas.items():
        n = len(points)
        if n<2:
            continue
    
        for i in range(n):
            for j in range(i+1,n):
                x1, y1= points[i]
                x2, y2 = points[j]
                dx, dy = x2-x1, y2-y1
                step_x, step_y = normalize(dx,dy)

                cx, cy = x1, y2
                while (cx, cy) != (x2, y2):
                    if in_bounds(cx, cy, width, height):
                        antinodes.add((cx, cy))
                    cx += step_x
                    cy += step_y
                
                if in_bounds(x2, y2, width, height):
                    antinodes.add((x2, y2))
    return len(antinodes)


filename = "Day 8/map.txt" 
grid = load_map(filename)
total = compute_antinodes(grid)
print(f"Total antinode positions within bounds: {total}")
