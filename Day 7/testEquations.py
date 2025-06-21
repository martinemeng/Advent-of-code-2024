import itertools

def evaluate(nums, ops): #tets combinations
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += nums[i+1]
        else:
            result *= nums[i+1]
    return result

def valid_eq(target, numbers):
    operators = ['+','*']
    for ops in itertools.product(operators, repeat = len(numbers)-1):
        if evaluate(numbers, ops) == target:
            return True 
    return False

def total(filename):
    total = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            target_num, numbers_part = line.strip().split(':')
            target = int(target_num.strip())
            numbers = list(map(int, numbers_part.strip().split()))
            if valid_eq(target,numbers):
                total += target
    return total

print(total('Day 7/equations.txt'))