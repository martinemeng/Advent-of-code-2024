ALLOWED = [1,2,3,-1,-2,-3]

# helping function
def is_safe(differences):
    return all(diff in ALLOWED for diff in differences) and (all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences))

def checkSafe(filename):
    safe_reports = 0
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            numbers = list(map(int,line.strip().split()))
            differences = []
            for i in range(len(numbers)-1):
                differences.append(numbers[i]-numbers[i+1])

            if is_safe(differences):
                safe_reports +=1
            else:
                for i in range(len(numbers)):
                    # create new list to remove the single level, if safe without safe_reports+=1
                    new_numbers = numbers[:i] + numbers[i+1:]
                    new_differences = []
                    for j in range(len(new_numbers) - 1):
                        new_differences.append(new_numbers[j] - new_numbers[j + 1])
                    if is_safe(new_differences):
                        safe_reports += 1
                        break 
    return safe_reports



print(checkSafe('Day 2/nuclear.txt'))
