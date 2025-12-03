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


print("Sum of invalid IDs: ", sum_invalids("products.txt"))