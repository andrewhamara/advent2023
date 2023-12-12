def main():
    with open("input.txt") as f:
        lines = f.readlines()
        total = 0
        sumMaxPowers = 0
        for line in lines:
            b,n,mr,mg,mb = parseLine(line)
            if b:
                total += int(n)
            sumMaxPowers += (mr * mg * mb)
    print(total)
    print(sumMaxPowers)

def parseLine(line):
    gameNumber = line.split(" ")[1][:-1]
    vals = line.split(" ")[2:]
    reds, greens, blues = 0,0,0
    maxRed, maxGreen, maxBlue = -1,-1,-1
    valid = True
    for i in range(0, len(vals), 2):
        count = int(vals[i])
        color = vals[i+1]
        if color.startswith('r'):
            maxRed = max(maxRed, count)
            reds += count
        elif color.startswith('g'):
            maxGreen = max(maxGreen, count)
            greens += count
        elif color.startswith('b'):
            maxBlue = max(maxBlue, count)
            blues += count

        if reds > 12 or greens > 13 or blues > 14:
            valid = False
        if color.endswith(';'):
            reds, greens, blues = 0,0,0
    if valid:
        return [True, gameNumber, maxRed, maxGreen, maxBlue]
    return [False, gameNumber, maxRed, maxGreen, maxBlue]

if __name__ == "__main__":
    main()
