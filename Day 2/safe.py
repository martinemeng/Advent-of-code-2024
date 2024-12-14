ALLOWED = [1,2,3,-1,-2,-3]

def checkSafe(filename):
    safe_reports = 0
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            numbers = list(map(int,line.strip().split()))
            differences = [numbers[i]-numbers[i+1] for i in range(len(numbers)-1)]
            if all(diff in ALLOWED for diff in differences):
                if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
                    safe_reports +=1
    return safe_reports



print(checkSafe('Day 2/nuclear.txt'))
