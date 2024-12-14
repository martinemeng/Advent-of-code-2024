#day 1, part 1 & 2
def calcDistAndSim(filename):
    with open(filename, 'r', encoding='utf-8') as f:

        leftNumbers = []
        rightNumbers = []
        distances = []
        similarities = []
        
        for line in f:
            left, right = line.split()
            leftNumbers.append(int(left))
            rightNumbers.append(int(right))
        
        for number in leftNumbers:
            similarities.append(rightNumbers.count(number)*number)

        leftNumbers.sort()
        rightNumbers.sort()

        for i in range(len(leftNumbers)):
            distances.append(abs(leftNumbers[i]-rightNumbers[i]))

    return sum(distances), sum(similarities)

#print(calcDistAndSim("Day 1/wishlist.txt"))



