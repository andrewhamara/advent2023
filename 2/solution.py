def main():
    with open("input.txt") as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            b,n = parseLine(line)
            if b:
                total += int(n)
    print(total)

def parseLine(line):
    gameNumber = line.split(" ")[1][:-1]
    vals = line.split(" ")[2:]
    reds, greens, blues = 0,0,0
    for i in range(0, len(vals), 2):
        count = int(vals[i])
        color = vals[i+1]
        if color.startswith('r'):
            reds += count
        elif color.startswith('g'):
            greens += count
        elif color.startswith('b'):
            blues += count

        if reds > 12 or greens > 13 or blues > 14:
            return [False, gameNumber]
        if color.endswith(';'):
            reds, greens, blues = 0,0,0
    return [True, gameNumber]

if __name__ == "__main__":
    main()
