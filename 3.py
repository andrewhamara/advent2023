def adjacentToSymbol(numberCoordinates, matrix) -> bool:
    matrixBoundY = len(matrix[0])
    matrixBoundX = len(matrix)

    toCheck = []

    leftMost = numberCoordinates[0]

    upLeft = [leftMost[0] - 1, leftMost[1] - 1]
    if upLeft[0] > -1 and upLeft[1] > -1:
        toCheck.append(upLeft)

    straightLeft = [leftMost[0] - 1, leftMost[1]]
    if straightLeft[0] > -1:
        toCheck.append(straightLeft)

    downLeft = [leftMost[0] - 1, leftMost[1] + 1]
    if downLeft[0] > -1 and downLeft[1] < matrixBoundY:
        toCheck.append(downLeft)

    straightDownFromLeft = [leftMost[0], leftMost[1] + 1]
    if straightDownFromLeft[1] < matrixBoundY:
        toCheck.append(straightDownFromLeft)

    straightUpFromLeft = [leftMost[0], leftMost[1] - 1]
    if straightUpFromLeft[1] > -1:
        toCheck.append(straightUpFromLeft)

    rightMost = numberCoordinates[-1]

    upRight = [rightMost[0] + 1, rightMost[1] - 1]
    if upRight[0] < matrixBoundX and upRight[1] > -1:
        toCheck.append(upRight)

    straightRight = [rightMost[0] + 1, rightMost[1]]
    if straightRight[0] < matrixBoundX:
        toCheck.append(straightRight)

    downRight = [rightMost[0] + 1, rightMost[1] + 1]
    if downRight[0] < matrixBoundX and downRight[1] < matrixBoundY:
        toCheck.append(downRight)

    straightUpFromRight = [rightMost[0], rightMost[1] - 1]
    if straightUpFromRight[1] > -1:
        toCheck.append(straightUpFromRight)

    straightDownFromRight = [rightMost[0], rightMost[1] + 1]
    if straightDownFromRight[1] < matrixBoundY:
        toCheck.append(straightDownFromRight)

    for i in range(1, len(numberCoordinates) - 1):
        cur = numberCoordinates[i]
        up = [cur[0], cur[1] - 1]
        if up[1] > -1:
            toCheck.append(up)
        down = [cur[0], cur[1] + 1]
        if down[1] < matrixBoundY:
            toCheck.append(down)

    for coord in toCheck:
        y,x = coord
        if matrix[x][y] == 1:
            return True
    return False

def main():
    with open("input.txt") as f:
        lines = [x.strip() for x in f.readlines()]

    matrix = []
    specials = "*#+$"

    for line in lines:
        cur = []
        for c in line:
            if c in specials:
                cur.append(1)
            else:
                cur.append(0)
        matrix.append(cur)

    total = 0
    for x,line in enumerate(lines):
        curNum = ''
        length = len(line)
        i = 0
        curCoordinates = []
        while length > i:
            while length > i and line[i].isnumeric():
                curCoordinates.append([i,x])
                curNum += line[i]
                i += 1
            if curNum:
                if adjacentToSymbol(curCoordinates, matrix):
                    total += int(curNum)
                curNum = ''
                curCoordinates = []
            i += 1
    print(total)

if __name__ == "__main__":
    main()
