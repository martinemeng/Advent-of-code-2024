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
                

print("Password: ", count_positions("directions.txt"))