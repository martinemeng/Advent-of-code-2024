def check_double_number(n):
    s = str(n)
    length = len(s)

    #check if the number has an even number of digits
    if length % 2 != 0:
        return False
    
    half = length // 2
    #check if first half is equal to second half
    if s[:half] == s[half:]:
        return True
    

def sum_invalids(filename):
    total = 0

    with open(filename, "r", encoding="utf-8") as f:
        line = f.read().strip()

    #knows it's one one line, each range separated by comma
    ranges = line.split(",")

    #ranges defined with -
    for r in ranges:
        if "-" not in r:
            continue

        #lower and upper part of range        
        a, b = r.split("-")
        start = int(a)
        end = int(b)

        for num in range(start, end+1):
            if check_double_number(num):
                total += num

    return total

def check_repeating(n):
    s = str(n)
    length = len(s)

    # try different possible pattern lengths, up to half of the length of the string
    for pattern_len in range(1, length//2 + 1):

        # the pattern must divide the length an even number of times if invalid
        if length % pattern_len != 0:
            continue

        # extract the pattern
        pattern = s[:pattern_len]

        # number of times it is repeated within the ID
        repeats = length // pattern_len

        # check if the pattern constructs the original ID
        if pattern * repeats == s:
            return True
        
    return False

def sum_invalids_pt2(filename):
    total = 0

    with open(filename, "r", encoding="utf-8") as f:
        line = f.read().strip()

    ranges = line.split(",")

    for r in ranges:
        if "-" not in r:
            continue
        
        a, b = r.split("-")
        start = int(a)
        end = int(b)

        for num in range(start, end+1):
            if check_repeating(num):
                total += num

    return total



# Part 1
print("Sum of invalid IDs, part 1: ", sum_invalids("products.txt"))

# Part 2
print("Sum of invalid IDs, part 2: ", sum_invalids_pt2("products.txt"))