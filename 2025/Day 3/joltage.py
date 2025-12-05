# Part 1
def find_max_joltage(n):
    best = 0
    length = len(n)

    for i in range(length-1):
        for j in range(i+1, length):
            #concatenate the string of the two biggest numbers (found so far) into one
            value = int(n[i]+n[j])
            # replace the best number found so far
            if value > best:
                best = value
    return best

# Part 2
def find_max_12_joltage(bank):
    digits = []
    for d in bank:
        digits.append(int(d))
    n = len(digits)

    result = []
    start = 0

    for _ in range(12):
        # ensure that you cannot pick a digit too far right
        max_pos = n - (12 - len(result))

        best_digit = -1
        best_index = start

        for i in range(start, max_pos+1):
            # find max digit
            if digits[i] > best_digit: 
                best_digit = digits[i]
                best_index = i

        result.append(best_digit)
        start = best_index + 1
    # converting the list of integers into one string -> one integer 
    return int("".join(str(d) for d in result))


def calculate_joltage(filename):
    total = 0

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Part 1
            # total += find_max_joltage(line)

            # Part 2
            total += find_max_12_joltage(line)
    
    return total

# Part 1
# print("Total joltage: ", calculate_joltage("batteries.txt"))

# Part 2
print("Total joltage: ", calculate_joltage("batteries.txt"))
