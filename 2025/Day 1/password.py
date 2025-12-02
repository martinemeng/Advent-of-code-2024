def count_positions(filename):
    position = 50
    password = 0

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            direction = line[0]
            distance = int(line[1:])

            if direction == "L":
                position = (position-distance) % 100
            else:
                position = (position+distance) % 100

            if position == 0:
                password += 1


    return password


def count_2_positions(filename):
    position = 50
    password = 0
    step = 0

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            direction = line[0]
            distance = int(line[1:])

            if direction == "L":
                step = -1
            else:
                step = 1

            for _ in range(distance):
                position = (position+step) % 100
                if position == 0:
                    password += 1

    return password

    
                
# Part 1
print("Password: ", count_positions("directions.txt"))

# Part 2
print("Password: ", count_2_positions("directions.txt"))