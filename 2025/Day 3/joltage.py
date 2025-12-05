def find_max_joltage(n):
    best = 0
    length = len(n)

    for i in range(length-1):
        for j in range(i+1, length):
            value = int(n[i]+n[j])
            if value > best:
                best = value
    return best


def calculate_joltage(filename):
    total = 0

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            total += find_max_joltage(line)
    
    return total

print("Total joltage: ", calculate_joltage("batteries.txt"))
