import re

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
control_pattern = r'\bdo\(\)|\bdon\'t\(\)'



def multiplication(filename):
    total = 0
    mul_enabled = True

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
    
            tokens = re.finditer(f"{control_pattern}|{pattern}", line)

            for token in tokens:
                match = token.group()

                if match == "do()":
                    mul_enabled = True
                elif match == "don't()":
                    mul_enabled = False
                elif mul_enabled and match.startswith("mul("):
                    digit1, digit2 = map(int, re.findall(r'\d+', match))
                    total += digit1 * digit2

    return total

print(multiplication('Day 3/corruptedMemory.txt'))